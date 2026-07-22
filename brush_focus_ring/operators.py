"""Operador modal que sigue el ratón y activa/desactiva el dibujo."""

import bpy
from bpy.props import IntProperty

from . import draw, utils


def _region_under_mouse(context, mx, my):
    """(region, área es VIEW_3D) para la posición del ratón en la ventana."""
    screen = context.screen
    if screen is None:
        return None, False
    for area in screen.areas:
        if area.type != 'VIEW_3D':
            continue
        for region in area.regions:
            if region.type != 'WINDOW':
                continue
            if (region.x <= mx < region.x + region.width
                    and region.y <= my < region.y + region.height):
                return region, True
    return None, False


class SCULPT_EXT_OT_focus_ring_toggle(bpy.types.Operator):
    """Activa o desactiva la doble circunferencia de foco/influencia"""

    bl_idname = "sculpt_ext.focus_ring_toggle"
    bl_label = "Anillo de foco"
    bl_options = {'REGISTER'}

    _native_cursor_backup = None

    @classmethod
    def poll(cls, context):
        return context.area is not None and context.window is not None

    def invoke(self, context, event):
        st = utils.state
        if st["running"]:
            # Segundo invoke = apagar: el modal activo lo detecta y termina.
            st["running"] = False
            utils.tag_redraw_view3d(context)
            return {'CANCELLED'}

        st["running"] = True
        st["mouse"] = (event.mouse_region_x, event.mouse_region_y)
        draw.add_handler()
        if not utils.apply_focus_to_brush(context):
            self.report({'WARNING'}, "No se pudo aplicar el foco al pincel activo")
        self._maybe_hide_native_cursor(context)
        context.window_manager.modal_handler_add(self)
        self.report({'INFO'}, "Anillo de foco activado")
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        st = utils.state
        if not st["running"]:
            self._cleanup(context)
            return {'CANCELLED'}

        if event.type == 'MOUSEMOVE':
            region, in_v3d = _region_under_mouse(
                context, event.mouse_x, event.mouse_y
            )
            st["in_view3d"] = in_v3d
            if region is not None:
                st["region_id"] = region.as_pointer()
                st["mouse"] = (
                    event.mouse_x - region.x,
                    event.mouse_y - region.y,
                )
                region.tag_redraw()
        elif event.value in {'PRESS', 'RELEASE'} and st["in_view3d"]:
            # Otro atajo (tamaño de pincel con +/-, foco, etc.) pudo cambiar el
            # pincel: repintar el anillo para que refleje el nuevo radio al
            # instante, sin esperar a mover el ratón. El evento igualmente pasa.
            utils.tag_redraw_view3d(context)

        # Nunca consumir eventos: esculpir y navegar siguen funcionando.
        return {'PASS_THROUGH'}

    def _maybe_hide_native_cursor(self, context):
        prefs = utils.get_prefs(context)
        if prefs is None or not prefs.hide_native_cursor:
            return
        paint = context.tool_settings.sculpt
        if paint is not None:
            self._native_cursor_backup = paint.show_brush
            paint.show_brush = False

    def _restore_native_cursor(self, context):
        if self._native_cursor_backup is None:
            return
        paint = context.tool_settings.sculpt
        if paint is not None:
            paint.show_brush = self._native_cursor_backup
        self._native_cursor_backup = None

    def _cleanup(self, context):
        draw.remove_handler()
        self._restore_native_cursor(context)
        utils.state["in_view3d"] = False
        utils.tag_redraw_view3d(context)
        self.report({'INFO'}, "Anillo de foco desactivado")


class SCULPT_EXT_OT_focus_adjust(bpy.types.Operator):
    """Sube o baja el foco un paso (atajo de teclado opcional)"""

    bl_idname = "sculpt_ext.focus_adjust"
    bl_label = "Ajustar foco"
    bl_options = {'REGISTER', 'UNDO'}

    direction: IntProperty(
        name="Dirección",
        description="+1 sube el foco, -1 lo baja",
        default=1,
    )

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        prefs = utils.get_prefs(context)
        step = prefs.focus_step if prefs is not None else 0.05
        sign = 1 if self.direction >= 0 else -1
        current = context.scene.bfr_focus
        new_value = max(0.0, min(1.0, current + sign * step))
        # Escribir la propiedad dispara _on_focus_update: aplica al pincel y redibuja.
        context.scene.bfr_focus = new_value
        self.report({'INFO'}, f"Foco: {new_value:.2f}")
        return {'FINISHED'}


classes = (
    SCULPT_EXT_OT_focus_ring_toggle,
    SCULPT_EXT_OT_focus_adjust,
)
