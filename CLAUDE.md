# Instructivo técnico — Addon "Subdiv Levels" para Blender

Documento de instrucciones para Claude Code. Sigue este documento como especificación
única del proyecto. Si algo no está definido aquí, pregunta antes de asumir.

## 1. Contexto y objetivo

Crear un addon (extensión) para **Blender 5.1.2** que replique el flujo de **niveles de
subdivisión de ZBrush / Nomad Sculpt**: subir y bajar de nivel con atajos, añadir un
nivel nuevo, y borrar niveles superiores, todo sin salir del modo Sculpt.

En Blender esto se implementa sobre el **modificador Multiresolution (Multires)**.
El addon NO reimplementa subdivisión: orquesta el modificador Multires con una UX
rápida (atajos + panel), que es lo que Blender no ofrece de serie.

Flujo objetivo del usuario:

1. Selecciona una malla y entra en modo Sculpt.
2. Pulsa `Ctrl+D`: si no hay modificador Multires, se crea; si está en el nivel máximo,
   se añade un nivel nuevo (Catmull-Clark); si no, sube un nivel.
3. `Shift+D` baja un nivel (sin destruir nada, como en ZBrush).
4. `Alt+D` sube un nivel (sin crear niveles nuevos).
5. Desde el panel puede borrar niveles superiores, aplicar la base y ver estadísticas.

## 2. Alcance del MVP

Incluido:

- Creación automática del modificador Multires si no existe (nombre: `"Multires"`).
- Subir / bajar / añadir nivel, borrar niveles superiores, aplicar base.
- Panel en la barra lateral (N) del Viewport 3D, pestaña "Subdiv", visible en modo
  Sculpt y modo Objeto.
- Atajos de teclado registrados por el addon y configurables en las preferencias.
- Estadísticas: nivel actual / total y recuento aproximado de caras del nivel activo.
- Sincronización de `levels`, `sculpt_levels` y `render_levels` (opción en preferencias,
  activada por defecto: al cambiar de nivel se actualizan viewport y sculpt a la vez).

Fuera de alcance (NO implementar sin pedirlo):

- Unsubdivide / reconstruir niveles inferiores (`multires_rebuild_subdiv`): dejar
  preparado el hueco en la UI pero como fase 2.
- Bake de displacement, soporte multi-objeto simultáneo, Geometry Nodes.

## 3. Estructura del proyecto

Usar el formato de **extensión** de Blender 4.2+ (vigente en 5.x), no el addon clásico:

```
subdiv_levels/
├── blender_manifest.toml
├── __init__.py          # register()/unregister(), importa los módulos
├── operators.py         # todos los bpy.types.Operator
├── ui.py                # panel lateral (bpy.types.Panel)
├── keymaps.py           # registro/limpieza de atajos
├── preferences.py       # AddonPreferences
└── utils.py             # helpers: obtener/crear multires, validaciones
```

`blender_manifest.toml` mínimo:

```toml
schema_version = "1.0.0"
id = "subdiv_levels"
version = "0.1.0"
name = "Subdiv Levels"
tagline = "Niveles de subdivision estilo ZBrush/Nomad para Sculpt"
maintainer = "Dani <danielsolerdev@gmail.com>"
type = "add-on"
tags = ["Sculpt", "Mesh"]
blender_version_min = "5.0.0"
license = ["SPDX:GPL-3.0-or-later"]
```

No usar `bl_info` (es del sistema clásico). El `id` del manifest define el paquete.

## 4. API de Blender relevante

Modificador (`bpy.types.MultiresModifier`):

- `levels` — nivel visible en viewport (int).
- `sculpt_levels` — nivel activo en modo Sculpt (int).
- `render_levels` — nivel en render (int).
- `total_levels` — niveles almacenados (solo lectura). Es el techo para subir de nivel.

Operadores nativos (requieren el objeto activo y el nombre del modificador):

- `bpy.ops.object.multires_subdivide(modifier="Multires", mode='CATMULL_CLARK')`
  — añade un nivel. `mode` admite `'CATMULL_CLARK'`, `'SIMPLE'`, `'LINEAR'`.
- `bpy.ops.object.multires_higher_levels_delete(modifier="Multires")`
  — borra los niveles por encima del actual.
- `bpy.ops.object.multires_base_apply(modifier="Multires")`
  — aplica el desplazamiento a la malla base.

Notas de contexto:

- Estos operadores funcionan en modo Objeto y Sculpt, pero verifican `context.object`.
  En los operadores propios usar `poll()` que compruebe: hay objeto activo, es `'MESH'`,
  y no está en modo Edit.
- Subir/bajar nivel NO usa operadores nativos: se hace asignando `sculpt_levels` /
  `levels` directamente, con clamp entre 0 y `total_levels`.
- Para forzar refresco del viewport tras cambiar propiedades desde un atajo:
  `context.object.update_tag()` y `context.area.tag_redraw()` si hace falta.

## 5. Operadores a implementar

Prefijo de `bl_idname`: `sculpt_ext.*`. Todos con `bl_options = {'REGISTER', 'UNDO'}`.

| bl_idname | Comportamiento |
|---|---|
| `sculpt_ext.subdiv_smart` | El "Ctrl+D inteligente": sin multires → crearlo con nivel 0; en nivel < total → subir 1; en nivel máximo → `multires_subdivide` (modo según preferencias, por defecto Catmull-Clark). Límite de seguridad: no crear niveles nuevos si el nivel actual ≥ `max_auto_level` de preferencias (por defecto 7); en ese caso, `self.report({'WARNING'}, ...)`. |
| `sculpt_ext.level_up` | Sube 1 nivel (clamp a `total_levels`). Nunca crea niveles. |
| `sculpt_ext.level_down` | Baja 1 nivel (clamp a 0). |
| `sculpt_ext.level_set` | Propiedad `level: IntProperty`. Fija el nivel exacto (para el slider del panel). |
| `sculpt_ext.delete_higher` | Confirma con `invoke_confirm`, luego `multires_higher_levels_delete`. |
| `sculpt_ext.apply_base` | Confirma con `invoke_confirm`, luego `multires_base_apply`. |

"Cambiar de nivel" significa: escribir `sculpt_levels` y, si la sincronización está
activa en preferencias, también `levels` (y `render_levels` solo si la opción
`sync_render` está activa, por defecto desactivada).

## 6. Panel (ui.py)

`bpy.types.Panel`, `bl_space_type='VIEW_3D'`, `bl_region_type='UI'`,
`bl_category='Subdiv'`. Contenido de arriba a abajo:

1. Si no hay multires: botón grande "Añadir Multires" (`sculpt_ext.subdiv_smart`).
2. Nivel actual como texto: `Nivel 3 / 5` + botones `−` / `+` en fila.
3. Botón principal "Subdividir (Ctrl+D)" → `sculpt_ext.subdiv_smart`.
4. Caja plegable "Avanzado": borrar superiores, aplicar base, selector de modo de
   subdivisión, y los sliders nativos del modificador (`levels`, `render_levels`).
5. Pie: recuento de caras estimado: caras base × 4^nivel (calculado en `utils.py`,
   no iterar la malla evaluada en cada draw — el panel se redibuja constantemente).

## 7. Atajos (keymaps.py)

Registrar en el keymap `"Sculpt"` y también en `"Object Mode"`:

- `Ctrl+D` → `sculpt_ext.subdiv_smart`
- `Shift+D` → `sculpt_ext.level_down`
- `Alt+D` → `sculpt_ext.level_up`

Advertencias conocidas: `Shift+D` en modo Objeto colisiona con Duplicar. Solución:
en `"Object Mode"` registrar solo `Ctrl+D`; `Shift+D`/`Alt+D` solo en `"Sculpt"`.
Guardar las entradas creadas en una lista global `addon_keymaps` y eliminarlas en
`unregister()` (patrón estándar). Los atajos deben poder desactivarse desde las
preferencias del addon.

## 8. Preferencias (preferences.py)

`AddonPreferences` con `bl_idname = __package__`. Propiedades:

- `subdivision_mode`: EnumProperty (`CATMULL_CLARK` por defecto, `SIMPLE`, `LINEAR`).
- `sync_viewport`: Bool, default True — sincronizar `levels` con `sculpt_levels`.
- `sync_render`: Bool, default False.
- `max_auto_level`: Int, default 7, min 1, max 10.
- `enable_hotkeys`: Bool, default True.

## 9. Compatibilidad Blender 5.x — reglas obligatorias

- **No usar acceso tipo diccionario** a propiedades definidas con `bpy.props`
  (p. ej. `obj['mi_prop']`): eliminado en 5.0. Usar siempre acceso por atributo.
- No importar módulos internos (`bl_console_utils`, `bl_rna_utils`, etc.).
- Registro con listas: `classes = (...)` + bucle `bpy.utils.register_class` en
  `register()` y orden inverso en `unregister()`.
- El addon debe poder activarse/desactivarse repetidamente sin errores ni fugas
  (keymaps y clases limpiados por completo en `unregister()`).
- Anotaciones de propiedades con `:` (annotation syntax), nunca `=`.

## 10. Convenciones de código

- Python con type hints donde aporte claridad; docstrings breves en español.
- Nada de `print()` en el código final: usar `self.report()` en operadores.
- Ningún operador debe lanzar excepción con contexto inválido: `poll()` estricto.
- Mensajes de UI en español (strings centralizados no necesarios en el MVP).

## 11. Pruebas y verificación

- Smoke test sin GUI (crear `tests/smoke_test.py`):
  `blender --background --factory-startup --python tests/smoke_test.py`
  El script: activa el addon, crea un cubo, llama a `subdiv_smart` 3 veces, comprueba
  `total_levels == 3`, baja 2 niveles, comprueba `sculpt_levels == 1`, borra
  superiores, comprueba `total_levels == 1`. Salir con código ≠ 0 si algo falla.
- Verificación manual mínima: atajos en modo Sculpt, panel visible, activar/desactivar
  el addon dos veces seguidas sin errores en consola.

## 12. Criterios de aceptación

1. `Ctrl+D` en una malla sin multires: crea el modificador y sube a nivel 1 en un solo gesto.
2. Subir/bajar nivel es instantáneo y no destruye el detalle esculpido de niveles altos.
3. El panel refleja siempre el estado real del modificador (sin estado duplicado propio).
4. Instalable como extensión (zip con `blender_manifest.toml`) en Blender 5.1.2.
5. El smoke test pasa en modo background.
