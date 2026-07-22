"""Preferencias del addon: colores, grosor, comportamiento y atajos."""

import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    FloatVectorProperty,
)


def _event_type_items():
    """Lista de teclas disponibles para los desplegables de atajos."""
    items = []
    seen = set()
    for it in bpy.types.KeyMapItem.bl_rna.properties["type"].enum_items:
        if it.identifier in seen:
            continue
        seen.add(it.identifier)
        items.append((it.identifier, it.name, ""))
    return items


# Se calcula una vez al importar el módulo (bpy ya está disponible al registrar).
_EVENT_TYPE_ITEMS = _event_type_items()


def _rebuild_keymaps(self, context):
    """Reconstruye los atajos al cambiar la casilla maestra o cualquier tecla."""
    from . import keymaps  # import perezoso: evita import circular en carga
    keymaps.rebuild_keymaps()


class BrushFocusRingPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    outer_color: FloatVectorProperty(
        name="Color exterior (influencia)",
        subtype='COLOR',
        size=4,
        min=0.0,
        max=1.0,
        default=(1.0, 0.35, 0.1, 0.9),
    )
    inner_color: FloatVectorProperty(
        name="Color interior (foco)",
        subtype='COLOR',
        size=4,
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0, 0.9),
    )
    line_width: FloatProperty(
        name="Grosor de línea",
        min=1.0,
        max=5.0,
        default=1.5,
    )
    min_inner_ratio: FloatProperty(
        name="Radio interior mínimo",
        description="Fracción del radio exterior visible aunque el foco sea 0",
        min=0.0,
        max=0.5,
        default=0.05,
    )
    hide_native_cursor: BoolProperty(
        name="Ocultar cursor nativo en Sculpt",
        description="Desactiva el círculo de Blender mientras el anillo está activo",
        default=True,
    )
    enable_hotkeys: BoolProperty(
        name="Activar atajos del encoder",
        description=(
            "Registra las tres teclas del encoder de foco en el modo Sculpt. "
            "Cambia cada tecla en los desplegables de abajo"
        ),
        default=True,
        update=_rebuild_keymaps,
    )
    # Modificador común a los tres atajos (el encoder del macropad lo envía junto).
    mod_ctrl: BoolProperty(name="Ctrl", default=True, update=_rebuild_keymaps)
    mod_alt: BoolProperty(name="Alt", default=True, update=_rebuild_keymaps)
    mod_shift: BoolProperty(name="Shift", default=True, update=_rebuild_keymaps)
    key_down: EnumProperty(
        name="Bajar foco",
        description="Tecla para bajar el foco (girar el encoder a la izquierda)",
        items=_EVENT_TYPE_ITEMS,
        default='Z',
        update=_rebuild_keymaps,
    )
    key_toggle: EnumProperty(
        name="Activar / desactivar anillo",
        description="Tecla para encender o apagar el anillo (pulsar el encoder)",
        items=_EVENT_TYPE_ITEMS,
        default='X',
        update=_rebuild_keymaps,
    )
    key_up: EnumProperty(
        name="Subir foco",
        description="Tecla para subir el foco (girar el encoder a la derecha)",
        items=_EVENT_TYPE_ITEMS,
        default='C',
        update=_rebuild_keymaps,
    )
    focus_step: FloatProperty(
        name="Paso de foco",
        description="Cuánto cambia el foco en cada muesca del encoder",
        min=0.01,
        max=0.5,
        default=0.05,
    )

    def draw(self, context):
        col = self.layout.column()
        col.prop(self, "outer_color")
        col.prop(self, "inner_color")
        col.prop(self, "line_width")
        col.prop(self, "min_inner_ratio")
        col.prop(self, "hide_native_cursor")

        col.separator()
        col.label(text="Atajos del encoder de foco (modo Sculpt):")
        col.prop(self, "enable_hotkeys")
        if self.enable_hotkeys:
            col.prop(self, "focus_step")
            self._draw_keymaps(context, col)

    def _draw_keymaps(self, context, layout):
        """Dibuja las tres asignaciones como propiedades normales (persisten)."""
        box = layout.box()
        row = box.row(align=True)
        row.label(text="Modificadores:")
        row.prop(self, "mod_ctrl", toggle=True)
        row.prop(self, "mod_alt", toggle=True)
        row.prop(self, "mod_shift", toggle=True)
        box.prop(self, "key_down")
        box.prop(self, "key_toggle")
        box.prop(self, "key_up")


classes = (BrushFocusRingPreferences,)
