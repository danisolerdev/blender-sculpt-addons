"""Preferencias del addon Subdiv Levels."""

import bpy
from bpy.props import BoolProperty, EnumProperty, IntProperty


def _update_hotkeys(self, context):
    """Reconstruye los keymaps al activar/desactivar los atajos."""
    from . import keymaps
    keymaps.unregister_keymaps()
    if self.enable_hotkeys:
        keymaps.register_keymaps()


class SubdivLevelsPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    subdivision_mode: EnumProperty(
        name="Modo de subdivisión",
        description="Algoritmo usado al crear un nivel nuevo",
        items=(
            ('CATMULL_CLARK', "Catmull-Clark", "Subdivisión suave (por defecto)"),
            ('SIMPLE', "Simple", "Subdivide sin suavizar"),
            ('LINEAR', "Lineal", "Subdivisión lineal"),
        ),
        default='CATMULL_CLARK',
    )
    sync_viewport: BoolProperty(
        name="Sincronizar viewport",
        description="Al cambiar de nivel, actualizar también el nivel del viewport",
        default=True,
    )
    sync_render: BoolProperty(
        name="Sincronizar render",
        description="Al cambiar de nivel, actualizar también el nivel de render",
        default=False,
    )
    max_auto_level: IntProperty(
        name="Nivel máximo automático",
        description="Ctrl+D no crea niveles nuevos por encima de este nivel",
        default=7,
        min=1,
        max=10,
    )
    enable_hotkeys: BoolProperty(
        name="Activar atajos",
        description="Registrar Ctrl+D / Shift+D / Alt+D",
        default=True,
        update=_update_hotkeys,
    )

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self, "subdivision_mode")
        col.prop(self, "max_auto_level")
        col.separator()
        col.prop(self, "sync_viewport")
        col.prop(self, "sync_render")
        col.separator()
        col.prop(self, "enable_hotkeys")


classes = (
    SubdivLevelsPreferences,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
