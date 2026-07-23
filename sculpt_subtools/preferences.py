"""Preferencias del addon Sculpt Subtools."""

import bpy
from bpy.props import BoolProperty, EnumProperty, FloatProperty


def _update_hotkeys(self, context):
    """Reconstruye los keymaps al activar/desactivar los atajos."""
    from . import keymaps
    keymaps.unregister_keymaps()
    if self.enable_hotkeys:
        keymaps.register_keymaps()


class SculptSubtoolsPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    switch_reenters_sculpt: BoolProperty(
        name="Re-enter Sculpt when Jumping",
        description="When activating another subtool from Sculpt, return to Sculpt mode "
        "(if disabled, the jump leaves the object in Object mode)",
        default=True,
    )
    solo_includes_group: BoolProperty(
        name="Solo Includes the Group",
        description="When isolating (Solo), keep the subtool's whole group visible, "
        "not just the object",
        default=False,
    )
    confirm_delete: BoolProperty(
        name="Confirm Delete",
        description="Asks for confirmation before deleting a subtool",
        default=True,
    )
    confirm_merge: BoolProperty(
        name="Confirm Merge",
        description="Asks for confirmation before merging subtools",
        default=True,
    )
    enable_hotkeys: BoolProperty(
        name="Enable Hotkeys",
        description="Registers the hotkeys to cycle subtools (Alt+↑ / Alt+↓)",
        default=False,
        update=_update_hotkeys,
    )
    sort_mode: EnumProperty(
        name="List Order",
        description="How to sort the subtools within each group",
        items=(
            ('MANUAL', "Manual", "By the assigned order (move up/down)"),
            ('NAME', "Name", "Alphabetical by name"),
        ),
        default='MANUAL',
    )
    show_thumbnails: BoolProperty(
        name="Show Thumbnails",
        description="Draws a thumbnail of each subtool in the palette "
        "(ZBrush style). Requires GPU",
        default=True,
    )
    auto_thumbnails: BoolProperty(
        name="Automatic Thumbnails",
        description="Regenerates the thumbnail automatically: when creating a mesh, "
        "switching the active subtool, reordering, and periodically. Disable it "
        "if sculpting stutters",
        default=True,
    )
    auto_thumbnail_interval: FloatProperty(
        name="Automatic Interval (s)",
        description="How many seconds between recaptures of the active subtool's "
        "thumbnail if no other event has occurred",
        default=60.0,
        min=5.0,
        max=600.0,
    )
    thumbnail_scale: FloatProperty(
        name="Thumbnail Size",
        description="Scale of the thumbnail in the palette",
        default=3.0,
        min=1.0,
        max=8.0,
    )

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(self, "switch_reenters_sculpt")
        col.prop(self, "solo_includes_group")
        col.prop(self, "sort_mode")
        col.separator()
        col.prop(self, "confirm_delete")
        col.prop(self, "confirm_merge")
        col.separator()
        col.prop(self, "show_thumbnails")
        sub = col.column()
        sub.enabled = self.show_thumbnails
        sub.prop(self, "auto_thumbnails")
        sub2 = sub.column()
        sub2.enabled = self.auto_thumbnails
        sub2.prop(self, "auto_thumbnail_interval")
        sub.prop(self, "thumbnail_scale")
        col.separator()
        col.prop(self, "enable_hotkeys")


classes = (
    SculptSubtoolsPreferences,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
