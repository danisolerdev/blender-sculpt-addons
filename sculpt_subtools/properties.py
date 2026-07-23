"""Propiedades registradas sobre tipos nativos de Blender.

Se registran sobre Object / Collection / Scene y se borran por completo en
unregister() para que el addon pueda activarse/desactivarse sin fugas.
"""

import bpy
from bpy.props import BoolProperty, EnumProperty, IntProperty, StringProperty


def register():
    bpy.types.Object.subtool_order = IntProperty(
        name="Order",
        description="Position of the subtool within its group",
        default=0,
    )
    bpy.types.Object.subtool_prev_hidden = BoolProperty(
        name="Previously Hidden",
        description="Visibility snapshot to restore after leaving Solo",
        default=False,
    )
    bpy.types.Object.subtool_bool_op = EnumProperty(
        name="Boolean Role",
        description="How this subtool participates in the live boolean",
        items=(
            ('NONE', "None", "Does not participate in the boolean"),
            ('ADD', "Add", "Joins the result (union)"),
            ('SUBTRACT', "Subtract", "Is subtracted from the result (difference)"),
            ('INTERSECT', "Intersect", "Keeps only the common volume (intersection)"),
        ),
        default='NONE',
    )
    bpy.types.Object.subtool_is_bool_result = BoolProperty(
        name="Boolean Result",
        description="Marks the live preview result object",
        default=False,
    )
    bpy.types.Collection.subtool_expanded = BoolProperty(
        name="Expanded",
        description="Whether the group is expanded in the palette",
        default=True,
    )
    bpy.types.Scene.subtool_solo_active = StringProperty(
        name="Active Solo",
        description="Name of the isolated subtool (empty = no Solo)",
        default="",
    )
    bpy.types.Scene.subtool_bool_active = StringProperty(
        name="Boolean Preview",
        description="Name of the preview result object (empty = no preview)",
        default="",
    )


def unregister():
    del bpy.types.Scene.subtool_bool_active
    del bpy.types.Scene.subtool_solo_active
    del bpy.types.Collection.subtool_expanded
    del bpy.types.Object.subtool_is_bool_result
    del bpy.types.Object.subtool_bool_op
    del bpy.types.Object.subtool_prev_hidden
    del bpy.types.Object.subtool_order
