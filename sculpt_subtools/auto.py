"""Actualización automática de miniaturas por eventos + fallback temporizado.

Amplía las capturas puntuales de los operadores a cambios globales de la escena,
ocurran por la vía que ocurran (Outliner, viewport, Shift+A...). Cubre:

1. Creación de un subtool/malla nuevo  -> handler de depsgraph (por conteo).
2. Cambio de orden de los subtools      -> lo encola `subtool_move` (operators.py).
3. Cambio del objeto activo (malla)     -> handler de depsgraph.
4. Nada de lo anterior                   -> timer: recaptura el activo cada `interval` s.

Regla de seguridad: el handler de depsgraph **solo marca "sucio"** (encola). La
captura real (que hace hide_set/mode_set) la ejecuta el timer, nunca el handler:
capturar dentro de un handler de depsgraph reentra el depsgraph y desestabiliza
Blender. En modo background no se registra nada (headless no tiene GPU ni timers
útiles para esto), así que el smoke test no se ve afectado.
"""

import time

import bpy
from bpy.app.handlers import persistent

# Cola de session_uid pendientes de recapturar.
_dirty: set = set()
# session_uid de las mallas ya conocidas (para detectar las nuevas).
_known: set = set()
# Conteo de objetos en la última pasada (atajo para no re-escanear en cada update).
_obj_count = -1
# session_uid del objeto activo en la última pasada (0 = ninguno).
_last_active = 0
# Marca de tiempo (monotónica) de la última captura, para el fallback temporizado.
_last_capture = 0.0

# Cada cuánto revisa la cola el timer (s). No es el intervalo del fallback (ese es
# la preferencia `auto_thumbnail_interval`); es solo la latencia de reacción.
_POLL = 1.0


def _interval() -> float:
    """Segundos del fallback temporizado (preferencia, por defecto 60)."""
    from . import utils
    prefs = utils.get_prefs()
    return float(getattr(prefs, "auto_thumbnail_interval", 60.0))


# --- API para los operadores --------------------------------------------------

def mark_dirty_obj(obj) -> None:
    """Encola la miniatura de un objeto para recaptura (usado por subtool_move)."""
    if obj is not None and getattr(obj, "type", None) == 'MESH':
        try:
            _dirty.add(obj.session_uid)
        except AttributeError:
            pass


# --- Resolución de la cola ----------------------------------------------------

def _objs_from_uids(uids):
    """Objetos malla vivos cuyos session_uid están en `uids` (descarta borrados)."""
    if not uids:
        return []
    return [
        o for o in bpy.data.objects
        if o.type == 'MESH' and getattr(o, "session_uid", None) in uids
    ]


def _drain():
    """Vacía la cola y devuelve los objetos vivos correspondientes."""
    global _dirty
    if not _dirty:
        return []
    uids = _dirty
    _dirty = set()
    return _objs_from_uids(uids)


# --- Handler de depsgraph (solo encola, nunca captura) ------------------------

def _scan_new_objects() -> None:
    """Detecta mallas nuevas por cambio de conteo y las encola (condición 1)."""
    global _obj_count, _known
    n = len(bpy.data.objects)
    if n == _obj_count:
        return
    cur = set()
    for o in bpy.data.objects:
        if o.type == 'MESH':
            uid = getattr(o, "session_uid", None)
            if uid is not None:
                cur.add(uid)
    if _known:  # en la primera pasada solo memorizamos: no capturar toda la escena
        _dirty.update(cur - _known)
    _known = cur
    _obj_count = n


def _check_active_change() -> None:
    """Detecta cambio de objeto activo y encola el que dejamos + el nuevo (cond. 3)."""
    global _last_active
    view_layer = bpy.context.view_layer
    active = view_layer.objects.active if view_layer is not None else None
    uid = getattr(active, "session_uid", 0) if active is not None else 0
    if uid == _last_active:
        return
    if _last_active:
        _dirty.add(_last_active)  # finalizar la miniatura del que dejamos
    if active is not None and active.type == 'MESH':
        _dirty.add(uid)           # asegurar miniatura fresca del nuevo activo
    _last_active = uid


@persistent
def _on_depsgraph(scene, depsgraph) -> None:
    """Se dispara muy a menudo: debe ser barato y no lanzar nunca."""
    if bpy.app.background:
        return
    try:
        _scan_new_objects()
        _check_active_change()
    except Exception:
        pass  # un handler de depsgraph jamás debe propagar excepciones


# --- Timer (hace la captura real, fuera del handler) --------------------------

def _tick():
    """Drena la cola y aplica el fallback temporizado. Devuelve la latencia de poll."""
    if bpy.app.background:
        return _POLL
    from . import preview
    if not preview._auto_on():
        _dirty.clear()
        return _POLL

    # No sacar al usuario de un modo de edición para capturar.
    mode = getattr(bpy.context, "mode", "")
    if mode.startswith('EDIT'):
        return _POLL

    global _last_capture
    now = time.monotonic()
    objs = _drain()
    if not objs and (now - _last_capture) >= _interval():
        # Condición 4: sin eventos, refrescar el subtool activo cada `interval` s.
        view_layer = bpy.context.view_layer
        active = view_layer.objects.active if view_layer is not None else None
        if active is not None and active.type == 'MESH':
            objs = [active]
    if objs:
        try:
            preview.maybe_capture_many(bpy.context, objs)
        except Exception:
            pass
        _last_capture = now
    return _POLL


# --- Registro -----------------------------------------------------------------

def register():
    # Headless: sin GPU ni sentido para el timer; no registramos nada.
    if bpy.app.background:
        return
    global _dirty, _known, _obj_count, _last_active, _last_capture
    _dirty = set()
    _known = set()
    _obj_count = -1
    _last_active = 0
    _last_capture = time.monotonic()  # el fallback no dispara nada más activar
    if _on_depsgraph not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(_on_depsgraph)
    if not bpy.app.timers.is_registered(_tick):
        bpy.app.timers.register(_tick, first_interval=_POLL, persistent=True)


def unregister():
    if _on_depsgraph in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(_on_depsgraph)
    if bpy.app.timers.is_registered(_tick):
        bpy.app.timers.unregister(_tick)
    _dirty.clear()
