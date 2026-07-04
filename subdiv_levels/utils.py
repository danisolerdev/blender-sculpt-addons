"""Helpers compartidos: acceso al modificador Multires, preferencias y estadísticas."""

import bpy

MULTIRES_NAME = "Multires"


class _FallbackPrefs:
    """Valores por defecto cuando las preferencias del addon no están disponibles
    (p. ej. al registrar el paquete manualmente en un smoke test)."""

    subdivision_mode = 'CATMULL_CLARK'
    sync_viewport = True
    sync_render = False
    max_auto_level = 7
    enable_hotkeys = True


_fallback_prefs = _FallbackPrefs()


def get_prefs():
    """Devuelve las preferencias del addon, o valores por defecto si no existen."""
    addon = bpy.context.preferences.addons.get(__package__)
    if addon is not None and addon.preferences is not None:
        return addon.preferences
    return _fallback_prefs


def prefs_are_real(prefs) -> bool:
    """True si `prefs` es un AddonPreferences real (dibujable en la UI)."""
    return isinstance(prefs, bpy.types.AddonPreferences)


def get_multires(obj):
    """Devuelve el primer modificador Multires del objeto, o None."""
    if obj is None or obj.type != 'MESH':
        return None
    for mod in obj.modifiers:
        if mod.type == 'MULTIRES':
            return mod
    return None


def create_multires(obj):
    """Crea un modificador Multires nuevo (nivel 0) en el objeto."""
    return obj.modifiers.new(name=MULTIRES_NAME, type='MULTIRES')


def set_level(obj, mod, level: int, prefs=None) -> int:
    """Fija el nivel activo con clamp [0, total_levels] y sincroniza según preferencias.

    Devuelve el nivel efectivo aplicado.
    """
    if prefs is None:
        prefs = get_prefs()
    level = max(0, min(level, mod.total_levels))
    mod.sculpt_levels = level
    if prefs.sync_viewport:
        mod.levels = level
    if prefs.sync_render:
        mod.render_levels = level
    obj.update_tag()
    return level


def estimate_faces(obj, level: int) -> int:
    """Recuento aproximado de caras del nivel dado: caras base × 4^nivel.

    No itera la malla evaluada (el panel se redibuja constantemente).
    """
    base = len(obj.data.polygons)
    return base * (4 ** max(0, level))


def format_faces(count: int) -> str:
    """Formatea un recuento de caras con separador de miles."""
    return f"{count:,}".replace(",", ".")
