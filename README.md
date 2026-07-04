# Subdiv Levels

Addon (extensión) para **Blender 5.x** que replica el flujo de niveles de subdivisión de **ZBrush / Nomad Sculpt**: subir y bajar de nivel con atajos, añadir un nivel nuevo y borrar niveles superiores, todo sin salir del modo Sculpt.

El addon no reimplementa la subdivisión: orquesta el modificador **Multiresolution (Multires)** de Blender con una UX rápida (atajos + panel lateral), que es justo lo que Blender no ofrece de serie.

## Características

- **Ctrl+D inteligente**: si no hay modificador Multires, lo crea; si estás en el nivel máximo, añade un nivel nuevo (Catmull-Clark); si no, sube un nivel.
- **Shift+D** baja un nivel y **Alt+D** sube un nivel, sin destruir el detalle esculpido (como en ZBrush).
- Panel en la barra lateral (N) del Viewport 3D, pestaña **Subdiv**, visible en modo Sculpt y modo Objeto.
- Borrar niveles superiores y aplicar la base desde el panel (con confirmación).
- Estadísticas: nivel actual / total y recuento aproximado de caras del nivel activo.
- Sincronización opcional de `levels`, `sculpt_levels` y `render_levels`.
- Atajos configurables y desactivables desde las preferencias del addon.
- Límite de seguridad configurable (`max_auto_level`, por defecto 7) para no crear niveles nuevos por accidente.

## Atajos por defecto

| Atajo | Acción | Modos |
|---|---|---|
| `Ctrl+D` | Subdividir inteligente (crear / subir / añadir nivel) | Sculpt y Objeto |
| `Shift+D` | Bajar un nivel | Sculpt |
| `Alt+D` | Subir un nivel | Sculpt |

> `Shift+D` y `Alt+D` solo se registran en modo Sculpt para no colisionar con Duplicar en modo Objeto.

## Requisitos

- Blender **5.0** o superior (desarrollado y probado en 5.1.2).

## Instalación

1. Descarga el zip de la extensión (`subdiv_levels-x.y.z.zip`) desde [Releases](../../releases), o genera uno comprimiendo la carpeta `subdiv_levels/` (el `blender_manifest.toml` debe quedar en la raíz del zip).
2. En Blender: `Edit → Preferences → Get Extensions → ⌄ (menú desplegable) → Install from Disk…` y selecciona el zip.
3. Activa la extensión **Subdiv Levels** si no se activa automáticamente.

## Uso

1. Selecciona una malla y entra en modo Sculpt.
2. Pulsa `Ctrl+D` para crear el Multires y subir al nivel 1 en un solo gesto.
3. Sigue pulsando `Ctrl+D` para añadir niveles a medida que necesites más detalle.
4. Usa `Shift+D` / `Alt+D` para moverte entre niveles sin perder el esculpido.
5. En el panel **Subdiv** (tecla N) tienes el slider de nivel, las opciones avanzadas (borrar niveles superiores, aplicar base, modo de subdivisión) y las estadísticas.

## Estructura del proyecto

```
subdiv_levels/
├── blender_manifest.toml   # manifest de extensión (Blender 4.2+)
├── __init__.py             # register()/unregister()
├── operators.py            # operadores (sculpt_ext.*)
├── ui.py                   # panel lateral
├── keymaps.py              # registro/limpieza de atajos
├── preferences.py          # AddonPreferences
└── utils.py                # helpers de Multires
tests/
└── smoke_test.py           # test sin GUI
```

## Desarrollo y tests

Smoke test sin interfaz gráfica:

```
blender --background --factory-startup --python tests/smoke_test.py
```

El script activa el addon, crea un cubo, subdivide tres veces, baja niveles y borra los superiores, verificando el estado del modificador en cada paso. Sale con código distinto de 0 si algo falla.

## Licencia

Este proyecto se distribuye bajo la licencia **GPL-3.0-or-later**, como requiere el ecosistema de addons de Blender. Consulta el archivo [LICENSE](LICENSE) para el texto completo.
