"""Operadores del addon Sculpt Subtools (prefijo sculpt_ext.subtool_*)."""

import bmesh
import bpy
from bpy.app.translations import pgettext_rpt as rpt_
from bpy.props import EnumProperty, IntProperty, StringProperty

from . import preview, utils

# Nombres de atributo estándar en Blender 5.x (verificados en spike).
FACE_SET_ATTR = ".sculpt_face_set"
MASK_ATTR = ".sculpt_mask"


def _poll_mesh(context) -> bool:
    """Hay objeto activo, es malla y no está en modo Edit."""
    obj = context.object
    return obj is not None and obj.type == 'MESH' and obj.mode != 'EDIT'


def _multires_of(obj):
    """Primer modificador Multires del objeto, o None."""
    for mod in obj.modifiers:
        if mod.type == 'MULTIRES':
            return mod
    return None


def _object_from_faces(src_obj, keep_indices, name, collection):
    """Crea un objeto nuevo con solo las caras `keep_indices` de `src_obj`."""
    bm = bmesh.new()
    bm.from_mesh(src_obj.data)
    bm.faces.ensure_lookup_table()
    keep = set(keep_indices)
    to_delete = [f for f in bm.faces if f.index not in keep]
    bmesh.ops.delete(bm, geom=to_delete, context='FACES')
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    new_obj = bpy.data.objects.new(name, me)
    new_obj.matrix_world = src_obj.matrix_world.copy()
    collection.objects.link(new_obj)
    return new_obj


def _delete_faces_inplace(obj, face_indices):
    """Borra las caras indicadas del propio datablock de `obj`."""
    me = obj.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    drop = set(face_indices)
    bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.index in drop], context='FACES')
    bm.to_mesh(me)
    bm.free()
    me.update()


def _redraw(context):
    """Fuerza el refresco del área activa."""
    if context.area is not None:
        context.area.tag_redraw()


def _deselect_all(context):
    for o in context.selected_objects:
        o.select_set(False)


def _make_active(context, obj):
    """Deja `obj` como único seleccionado y activo."""
    _deselect_all(context)
    obj.select_set(True)
    context.view_layer.objects.active = obj


# --- Activar / ciclar ---------------------------------------------------------

class SCULPTEXT_OT_subtool_activate(bpy.types.Operator):
    """Makes this subtool active (jumps to it without leaving Sculpt)"""

    bl_idname = "sculpt_ext.subtool_activate"
    bl_label = "Activate Subtool"
    bl_options = {'REGISTER'}

    name: StringProperty()

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        obj = bpy.data.objects.get(self.name)
        if obj is None or obj.type != 'MESH':
            self.report({'WARNING'}, rpt_("Subtool not found"))
            return {'CANCELLED'}
        if obj == context.object and not obj.hide_get():
            return {'CANCELLED'}  # ya es el subtool activo y visible

        prefs = utils.get_prefs()
        was_sculpt = context.mode == 'SCULPT'
        leaving = context.object

        if obj.hide_get():
            obj.hide_set(False)

        # Rebote: para cambiar el objeto que se esculpe hay que salir a Objeto,
        # reasignar el activo y (opcionalmente) reentrar en Sculpt.
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')
        # Recapturar la miniatura del subtool que dejamos (ya en modo Objeto).
        if leaving is not None and leaving is not obj and leaving.type == 'MESH':
            preview.maybe_capture(context, leaving)
        _make_active(context, obj)
        if was_sculpt and prefs.switch_reenters_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')

        _redraw(context)
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_cycle(bpy.types.Operator):
    """Jumps to the previous or next subtool of the active Tool"""

    bl_idname = "sculpt_ext.subtool_cycle"
    bl_label = "Cycle Subtool"
    bl_options = {'REGISTER'}

    direction: EnumProperty(
        items=(
            ('PREV', "Previous", "Previous subtool"),
            ('NEXT', "Next", "Next subtool"),
        ),
        default='NEXT',
    )

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        prefs = utils.get_prefs()
        root = utils.get_tool_root(obj)
        chain = utils.all_subtools(root, prefs.sort_mode)
        if obj not in chain or len(chain) < 2:
            self.report({'INFO'}, rpt_("No other subtool to jump to"))
            return {'CANCELLED'}
        idx = chain.index(obj)
        step = -1 if self.direction == 'PREV' else 1
        target = chain[(idx + step) % len(chain)]
        bpy.ops.sculpt_ext.subtool_activate(name=target.name)
        return {'FINISHED'}


# --- Visibilidad / Solo -------------------------------------------------------

class SCULPTEXT_OT_subtool_toggle_visible(bpy.types.Operator):
    """Shows or hides this subtool"""

    bl_idname = "sculpt_ext.subtool_toggle_visible"
    bl_label = "Subtool Visibility"
    bl_options = {'REGISTER'}

    name: StringProperty()

    def execute(self, context):
        obj = bpy.data.objects.get(self.name)
        if obj is None:
            return {'CANCELLED'}
        obj.hide_set(not obj.hide_get())
        _redraw(context)
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_solo(bpy.types.Operator):
    """Isolates this subtool by hiding the rest (toggle)"""

    bl_idname = "sculpt_ext.subtool_solo"
    bl_label = "Solo"
    bl_options = {'REGISTER'}

    name: StringProperty()

    def execute(self, context):
        obj = bpy.data.objects.get(self.name)
        if obj is None:
            return {'CANCELLED'}
        scene = context.scene
        prefs = utils.get_prefs()
        root = utils.get_tool_root(obj)
        subs = utils.all_subtools(root)

        if scene.subtool_solo_active == obj.name:
            # Desactivar Solo: restaurar visibilidad desde el snapshot.
            for o in subs:
                o.hide_set(o.subtool_prev_hidden)
            scene.subtool_solo_active = ""
        else:
            # Activar Solo. Tomar snapshot solo si no había otro Solo activo.
            if scene.subtool_solo_active == "":
                for o in subs:
                    o.subtool_prev_hidden = o.hide_get()
            keep = {obj}
            if prefs.solo_includes_group and obj.users_collection:
                keep.update(utils.all_subtools(obj.users_collection[0]))
            for o in subs:
                o.hide_set(o not in keep)
            scene.subtool_solo_active = obj.name

        _redraw(context)
        return {'FINISHED'}


# --- Duplicar / borrar --------------------------------------------------------

class SCULPTEXT_OT_subtool_duplicate(bpy.types.Operator):
    """Duplicates the active subtool"""

    bl_idname = "sculpt_ext.subtool_duplicate"
    bl_label = "Duplicate Subtool"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        _make_active(context, obj)
        bpy.ops.object.duplicate()
        dup = context.object  # duplicate deja el nuevo objeto como activo
        dup.subtool_order = obj.subtool_order + 1
        preview.maybe_capture(context, dup)

        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report({'INFO'}, rpt_("Duplicated: {}").format(dup.name))
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_delete(bpy.types.Operator):
    """Deletes the active subtool"""

    bl_idname = "sculpt_ext.subtool_delete"
    bl_label = "Delete Subtool"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def invoke(self, context, event):
        if utils.get_prefs().confirm_delete:
            return context.window_manager.invoke_confirm(self, event)
        return self.execute(context)

    def execute(self, context):
        obj = context.object
        was_sculpt = context.mode == 'SCULPT'
        root = utils.get_tool_root(obj)
        remaining = [o for o in utils.all_subtools(root) if o != obj]

        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        me = obj.data
        bpy.data.objects.remove(obj, do_unlink=True)
        if me is not None and me.users == 0:
            bpy.data.meshes.remove(me)

        if remaining:
            _make_active(context, remaining[0])
            if was_sculpt:
                bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report({'INFO'}, rpt_("Subtool deleted"))
        return {'FINISHED'}


# --- Orden / grupos -----------------------------------------------------------

class SCULPTEXT_OT_subtool_move(bpy.types.Operator):
    """Moves the active subtool up or down within its group"""

    bl_idname = "sculpt_ext.subtool_move"
    bl_label = "Move Subtool"
    bl_options = {'REGISTER', 'UNDO'}

    direction: EnumProperty(
        items=(
            ('UP', "Up", "Move up"),
            ('DOWN', "Down", "Move down"),
        ),
        default='UP',
    )

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        if not obj.users_collection:
            return {'CANCELLED'}
        coll = obj.users_collection[0]
        siblings = utils.subtools_of(coll, 'MANUAL')
        # Normalizar el orden para garantizar valores distintos antes de intercambiar.
        for i, o in enumerate(siblings):
            o.subtool_order = i
        idx = siblings.index(obj)
        swap = idx - 1 if self.direction == 'UP' else idx + 1
        if swap < 0 or swap >= len(siblings):
            self.report({'INFO'}, rpt_("The subtool is already at the end"))
            return {'CANCELLED'}
        other = siblings[swap]
        obj.subtool_order, other.subtool_order = other.subtool_order, obj.subtool_order
        # Condición 2: al reordenar, encolar los dos subtools para recaptura.
        from . import auto
        auto.mark_dirty_obj(obj)
        auto.mark_dirty_obj(other)
        _redraw(context)
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_group_new(bpy.types.Operator):
    """Creates a group (sub-collection) inside the active Tool"""

    bl_idname = "sculpt_ext.subtool_group_new"
    bl_label = "New Group"
    bl_options = {'REGISTER', 'UNDO'}

    name: StringProperty(name="Name", default="Group")

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        root = utils.get_tool_root(context.object)
        group = bpy.data.collections.new(self.name)
        root.children.link(group)
        _redraw(context)
        self.report({'INFO'}, rpt_("Group created: {}").format(group.name))
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_move_to_group(bpy.types.Operator):
    """Moves the active subtool to the given group"""

    bl_idname = "sculpt_ext.subtool_move_to_group"
    bl_label = "Move to Group"
    bl_options = {'REGISTER', 'UNDO'}

    group: StringProperty()

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        target = bpy.data.collections.get(self.group)
        if target is None:
            self.report({'WARNING'}, rpt_("Group not found"))
            return {'CANCELLED'}
        if obj.name in target.objects:
            return {'CANCELLED'}
        for c in list(obj.users_collection):
            c.objects.unlink(obj)
        target.objects.link(obj)
        _redraw(context)
        self.report({'INFO'}, rpt_("Moved to {}").format(target.name))
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_toggle_expand(bpy.types.Operator):
    """Collapses or expands a group in the palette"""

    bl_idname = "sculpt_ext.subtool_toggle_expand"
    bl_label = "Collapse/Expand Group"
    bl_options = {'REGISTER'}

    collection: StringProperty()

    def execute(self, context):
        coll = bpy.data.collections.get(self.collection)
        if coll is None:
            return {'CANCELLED'}
        coll.subtool_expanded = not coll.subtool_expanded
        _redraw(context)
        return {'FINISHED'}


# --- Merge / split ------------------------------------------------------------

class SCULPTEXT_OT_subtool_merge(bpy.types.Operator):
    """Merges the selected subtools into the active one"""

    bl_idname = "sculpt_ext.subtool_merge"
    bl_label = "Merge Subtools"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if not _poll_mesh(context):
            return False
        meshes = [o for o in context.selected_objects if o.type == 'MESH']
        return len(meshes) >= 2

    def invoke(self, context, event):
        if utils.get_prefs().confirm_merge:
            return context.window_manager.invoke_confirm(self, event)
        return self.execute(context)

    def execute(self, context):
        active = context.object
        selected = [o for o in context.selected_objects if o.type == 'MESH']
        has_multires = any(
            any(m.type == 'MULTIRES' for m in o.modifiers) for o in selected
        )
        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        context.view_layer.objects.active = active
        result = bpy.ops.object.join()

        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        if 'FINISHED' not in result:
            self.report({'WARNING'}, rpt_("Could not merge the subtools"))
            return {'CANCELLED'}
        _redraw(context)
        if has_multires:
            self.report({'WARNING'},
                        rpt_("Subtools merged; the Multires is not preserved when merging"))
        else:
            self.report({'INFO'}, rpt_("Subtools merged"))
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_split_loose(bpy.types.Operator):
    """Splits the active subtool into its loose parts"""

    bl_idname = "sculpt_ext.subtool_split_loose"
    bl_label = "Split by Loose Parts"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        was_sculpt = context.mode == 'SCULPT'
        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        _make_active(context, obj)
        before = set(bpy.data.objects)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.mode_set(mode='OBJECT')
        new_objs = [o for o in bpy.data.objects if o not in before]
        preview.maybe_capture_many(context, new_objs + [obj])

        if was_sculpt:
            _make_active(context, obj)
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        if new_objs:
            self.report(
                {'INFO'}, rpt_("Split into {} subtools").format(len(new_objs) + 1)
            )
        else:
            self.report({'INFO'}, rpt_("The subtool has no loose parts"))
        return {'FINISHED'}


# --- Crear / espejar ----------------------------------------------------------

class SCULPTEXT_OT_subtool_add(bpy.types.Operator):
    """Adds a new primitive mesh as a subtool of the active Tool"""

    bl_idname = "sculpt_ext.subtool_add"
    bl_label = "Add Subtool"
    bl_options = {'REGISTER', 'UNDO'}

    kind: EnumProperty(
        items=(
            ('CUBE', "Cube", "Add a cube"),
            ('SPHERE', "Sphere", "Add a sphere"),
            ('CYLINDER', "Cylinder", "Add a cylinder"),
            ('PLANE', "Plane", "Add a plane"),
        ),
        default='CUBE',
    )

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'SCULPT'}

    def execute(self, context):
        active = context.object
        if active is not None and active.users_collection:
            coll = active.users_collection[0]
        else:
            coll = context.scene.collection

        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        adders = {
            'CUBE': bpy.ops.mesh.primitive_cube_add,
            'SPHERE': bpy.ops.mesh.primitive_uv_sphere_add,
            'CYLINDER': bpy.ops.mesh.primitive_cylinder_add,
            'PLANE': bpy.ops.mesh.primitive_plane_add,
        }
        adders[self.kind]()
        new_obj = context.active_object

        # Reubicar el objeto nuevo en la colección del Tool.
        for c in list(new_obj.users_collection):
            if c != coll:
                c.objects.unlink(new_obj)
        if new_obj.name not in coll.objects:
            coll.objects.link(new_obj)
        preview.maybe_capture(context, new_obj)

        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report({'INFO'}, rpt_("Subtool added: {}").format(new_obj.name))
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_mirror(bpy.types.Operator):
    """Creates a mirrored copy of the active subtool across an axis"""

    bl_idname = "sculpt_ext.subtool_mirror"
    bl_label = "Mirror Subtool"
    bl_options = {'REGISTER', 'UNDO'}

    axis: EnumProperty(
        items=(
            ('X', "X", "Mirror across the X axis"),
            ('Y', "Y", "Mirror across the Y axis"),
            ('Z', "Z", "Mirror across the Z axis"),
        ),
        default='X',
    )

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        _make_active(context, obj)
        bpy.ops.object.duplicate()
        dup = context.object
        index = {'X': 0, 'Y': 1, 'Z': 2}[self.axis]
        dup.scale[index] *= -1.0
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        # La escala negativa invierte las normales: recomponerlas.
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.flip_normals()
        bpy.ops.object.mode_set(mode='OBJECT')
        dup.subtool_order = obj.subtool_order + 1
        preview.maybe_capture(context, dup)

        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report({'INFO'}, rpt_("Mirror created: {}").format(dup.name))
        return {'FINISHED'}


# --- Acciones globales --------------------------------------------------------

class SCULPTEXT_OT_subtool_show_all(bpy.types.Operator):
    """Shows all the Tool's subtools and turns off Solo"""

    bl_idname = "sculpt_ext.subtool_show_all"
    bl_label = "Show All Subtools"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        root = utils.get_tool_root(context.object)
        for o in utils.all_subtools(root):
            o.hide_set(False)
        context.scene.subtool_solo_active = ""
        _redraw(context)
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_frame_active(bpy.types.Operator):
    """Frames the view on the active subtool"""

    bl_idname = "sculpt_ext.subtool_frame_active"
    bl_label = "Frame Active"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def execute(self, context):
        try:
            bpy.ops.view3d.view_selected('INVOKE_DEFAULT')
        except RuntimeError as error:
            self.report({'WARNING'}, rpt_("Could not frame: {}").format(error))
            return {'CANCELLED'}
        return {'FINISHED'}


# --- Splits avanzados (bmesh sobre atributos) ---------------------------------

class SCULPTEXT_OT_subtool_split_faceset(bpy.types.Operator):
    """Splits the active subtool into one subtool per Face Set"""

    bl_idname = "sculpt_ext.subtool_split_faceset"
    bl_label = "Split by Face Sets"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        me = obj.data
        attr = me.attributes.get(FACE_SET_ATTR)
        if attr is None:
            self.report({'WARNING'}, rpt_("The mesh has no Face Sets"))
            return {'CANCELLED'}

        groups = {}
        for i in range(len(me.polygons)):
            groups.setdefault(attr.data[i].value, []).append(i)
        if len(groups) < 2:
            self.report({'INFO'}, rpt_("There is only one Face Set: nothing to split"))
            return {'CANCELLED'}

        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        coll = obj.users_collection[0] if obj.users_collection else context.scene.collection
        base_name = obj.name
        base_order = obj.subtool_order
        new_objs = []
        for offset, (value, faces) in enumerate(sorted(groups.items())):
            piece = _object_from_faces(obj, faces, f"{base_name}_fs{value}", coll)
            piece.subtool_order = base_order + offset
            new_objs.append(piece)

        # Sustituir el original por las piezas.
        old_mesh = obj.data
        bpy.data.objects.remove(obj, do_unlink=True)
        if old_mesh is not None and old_mesh.users == 0:
            bpy.data.meshes.remove(old_mesh)

        preview.maybe_capture_many(context, new_objs)
        _make_active(context, new_objs[0])
        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report(
            {'INFO'},
            rpt_("Split into {} subtools by Face Set").format(len(new_objs)),
        )
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_split_mask(bpy.types.Operator):
    """Splits the masked area of the active subtool into a new subtool"""

    bl_idname = "sculpt_ext.subtool_split_mask"
    bl_label = "Split by Mask"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        obj = context.object
        me = obj.data
        attr = me.attributes.get(MASK_ATTR)
        if attr is None:
            self.report({'WARNING'}, rpt_("The mesh has no Sculpt mask"))
            return {'CANCELLED'}

        mask = [attr.data[i].value for i in range(len(me.vertices))]
        masked_faces = []
        for poly in me.polygons:
            verts = poly.vertices
            avg = sum(mask[v] for v in verts) / len(verts)
            if avg >= 0.5:
                masked_faces.append(poly.index)

        if not masked_faces:
            self.report({'INFO'}, rpt_("There is no masked area"))
            return {'CANCELLED'}
        if len(masked_faces) == len(me.polygons):
            self.report({'INFO'}, rpt_("The whole mesh is masked: nothing to split"))
            return {'CANCELLED'}

        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        coll = obj.users_collection[0] if obj.users_collection else context.scene.collection
        piece = _object_from_faces(obj, masked_faces, f"{obj.name}_mask", coll)
        piece.subtool_order = obj.subtool_order + 1
        _delete_faces_inplace(obj, masked_faces)
        preview.maybe_capture_many(context, [piece, obj])

        _make_active(context, piece)
        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report({'INFO'}, rpt_("Masked area split into a new subtool"))
        return {'FINISHED'}


# --- Integración con Multires / Subdiv Levels ---------------------------------

class SCULPTEXT_OT_subtool_multires_step(bpy.types.Operator):
    """Raises or lowers the Multires level of the active subtool"""

    bl_idname = "sculpt_ext.subtool_multires_step"
    bl_label = "Multires Level"
    bl_options = {'REGISTER', 'UNDO'}

    delta: IntProperty(default=1)

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context) and _multires_of(context.object) is not None

    def execute(self, context):
        obj = context.object
        mod = _multires_of(obj)
        level = max(0, min(mod.sculpt_levels + self.delta, mod.total_levels))
        mod.sculpt_levels = level
        mod.levels = level
        obj.update_tag()
        _redraw(context)
        return {'FINISHED'}


# --- Booleanas ----------------------------------------------------------------

_BOOL_OP_TO_MOD = {'ADD': 'UNION', 'SUBTRACT': 'DIFFERENCE', 'INTERSECT': 'INTERSECT'}
# Orden de aplicación: primero unir (sembrar volumen), luego intersecar, luego restar.
_BOOL_ORDER = {'ADD': 0, 'INTERSECT': 1, 'SUBTRACT': 2}


def _bool_operands(root):
    """Subtools con rol booleano (excluye el objeto de resultado), en orden de aplicación."""
    ops = [o for o in utils.all_subtools(root)
           if not o.subtool_is_bool_result and o.subtool_bool_op != 'NONE']
    return sorted(ops, key=lambda o: (_BOOL_ORDER[o.subtool_bool_op], o.subtool_order))


def _build_bool_result(root, operands):
    """Crea el objeto de resultado con un modificador Boolean por operando."""
    me = bpy.data.meshes.new(f"{root.name}_bool")
    res = bpy.data.objects.new(f"{root.name}_bool", me)
    res.subtool_is_bool_result = True
    root.objects.link(res)
    for operand in operands:
        mod = res.modifiers.new(name=f"bool_{operand.name}", type='BOOLEAN')
        mod.operation = _BOOL_OP_TO_MOD[operand.subtool_bool_op]
        mod.object = operand
        mod.solver = 'EXACT'
    return res


def _remove_object(obj):
    if obj is None:
        return
    me = obj.data
    bpy.data.objects.remove(obj, do_unlink=True)
    if me is not None and me.users == 0:
        bpy.data.meshes.remove(me)


class SCULPTEXT_OT_subtool_bool_set_op(bpy.types.Operator):
    """Sets this subtool's boolean role (click the active role to clear it)"""

    bl_idname = "sculpt_ext.subtool_bool_set_op"
    bl_label = "Boolean Role"
    bl_options = {'REGISTER', 'UNDO'}

    target: StringProperty()
    role: EnumProperty(
        items=(
            ('ADD', "Add", "Joins the result (union)"),
            ('SUBTRACT', "Subtract", "Is subtracted from the result (difference)"),
            ('INTERSECT', "Intersect", "Keeps only the common volume (intersection)"),
        ),
        default='ADD',
    )

    def execute(self, context):
        obj = bpy.data.objects.get(self.target)
        if obj is None:
            return {'CANCELLED'}
        # Clic en el rol ya activo = quitarlo (vuelve a NONE).
        obj.subtool_bool_op = 'NONE' if obj.subtool_bool_op == self.role else self.role
        _redraw(context)
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_bool_preview(bpy.types.Operator):
    """Toggles the Tool's live boolean preview"""

    bl_idname = "sculpt_ext.subtool_bool_preview"
    bl_label = "Live Boolean Preview"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        scene = context.scene
        root = utils.get_tool_root(context.object)

        if scene.subtool_bool_active:
            # Desactivar: eliminar el resultado y mostrar los operandos.
            _remove_object(bpy.data.objects.get(scene.subtool_bool_active))
            scene.subtool_bool_active = ""
            for o in utils.all_subtools(root):
                if not o.subtool_is_bool_result:
                    o.hide_set(False)
            _redraw(context)
            return {'FINISHED'}

        operands = _bool_operands(root)
        if not any(o.subtool_bool_op == 'ADD' for o in operands):
            self.report({'WARNING'}, rpt_("Mark at least one subtool as 'Add'"))
            return {'CANCELLED'}

        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        res = _build_bool_result(root, operands)
        for o in operands:
            o.hide_set(True)
        scene.subtool_bool_active = res.name
        _make_active(context, res)

        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report(
            {'INFO'}, rpt_("Boolean preview: {} operands").format(len(operands))
        )
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_bool_apply(bpy.types.Operator):
    """Bakes the boolean: applies the result and removes the operands"""

    bl_idname = "sculpt_ext.subtool_bool_apply"
    bl_label = "Apply Boolean"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return _poll_mesh(context)

    def execute(self, context):
        scene = context.scene
        root = utils.get_tool_root(context.object)
        operands = _bool_operands(root)
        if not any(o.subtool_bool_op == 'ADD' for o in operands):
            self.report({'WARNING'}, rpt_("Mark at least one subtool as 'Add'"))
            return {'CANCELLED'}

        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        # Reutilizar el resultado del preview si existe; si no, construir uno.
        res = bpy.data.objects.get(scene.subtool_bool_active) if scene.subtool_bool_active else None
        if res is None:
            res = _build_bool_result(root, operands)
        scene.subtool_bool_active = ""

        _make_active(context, res)
        for mod_name in [m.name for m in res.modifiers]:
            try:
                bpy.ops.object.modifier_apply(modifier=mod_name)
            except RuntimeError as error:
                self.report(
                    {'WARNING'}, rpt_("Could not apply {}: {}").format(mod_name, error)
                )

        res.subtool_is_bool_result = False
        res.subtool_bool_op = 'NONE'
        for operand in operands:
            _remove_object(operand)

        _make_active(context, res)
        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        self.report({'INFO'}, rpt_("Boolean applied"))
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_bool_direct(bpy.types.Operator):
    """Direct boolean: applies the other selected subtools to the active one and deletes them"""

    bl_idname = "sculpt_ext.subtool_bool_direct"
    bl_label = "Direct Boolean"
    bl_options = {'REGISTER', 'UNDO'}

    op: EnumProperty(
        items=(
            ('UNION', "Union", "Union with the active"),
            ('DIFFERENCE', "Difference", "Subtract from the active"),
            ('INTERSECT', "Intersection", "Keep the common volume"),
        ),
        default='DIFFERENCE',
    )

    @classmethod
    def poll(cls, context):
        if not _poll_mesh(context):
            return False
        meshes = [o for o in context.selected_objects if o.type == 'MESH']
        return len(meshes) >= 2

    def execute(self, context):
        active = context.object
        others = [o for o in context.selected_objects
                  if o.type == 'MESH' and o != active]
        if not others:
            self.report(
                {'WARNING'}, rpt_("Select the active and at least one other subtool")
            )
            return {'CANCELLED'}

        was_sculpt = context.mode == 'SCULPT'
        if was_sculpt:
            bpy.ops.object.mode_set(mode='OBJECT')

        context.view_layer.objects.active = active
        added = []
        for operand in others:
            mod = active.modifiers.new(name="bool_direct", type='BOOLEAN')
            mod.operation = self.op
            mod.object = operand
            mod.solver = 'EXACT'
            added.append(mod.name)

        failed = False
        for mod_name in added:
            try:
                bpy.ops.object.modifier_apply(modifier=mod_name)
            except RuntimeError:
                failed = True

        for operand in others:
            _remove_object(operand)

        if was_sculpt:
            bpy.ops.object.mode_set(mode='SCULPT')
        _redraw(context)
        if failed:
            self.report({'WARNING'},
                        rpt_("Some boolean was not applied (Multires in the active's stack?)"))
        else:
            self.report({'INFO'}, rpt_("Boolean {} applied").format(self.op))
        return {'FINISHED'}


class SCULPTEXT_OT_subtool_rename(bpy.types.Operator):
    """Renames this subtool"""

    bl_idname = "sculpt_ext.subtool_rename"
    bl_label = "Rename Subtool"
    bl_options = {'REGISTER', 'UNDO'}

    target: StringProperty()
    new_name: StringProperty(name="Name")

    def invoke(self, context, event):
        obj = bpy.data.objects.get(self.target)
        if obj is None:
            return {'CANCELLED'}
        self.new_name = obj.name
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        self.layout.prop(self, "new_name")

    def execute(self, context):
        obj = bpy.data.objects.get(self.target)
        if obj is None:
            self.report({'WARNING'}, rpt_("Subtool not found"))
            return {'CANCELLED'}
        if self.new_name:
            obj.name = self.new_name
        _redraw(context)
        return {'FINISHED'}


classes = (
    SCULPTEXT_OT_subtool_activate,
    SCULPTEXT_OT_subtool_rename,
    SCULPTEXT_OT_subtool_cycle,
    SCULPTEXT_OT_subtool_toggle_visible,
    SCULPTEXT_OT_subtool_solo,
    SCULPTEXT_OT_subtool_duplicate,
    SCULPTEXT_OT_subtool_delete,
    SCULPTEXT_OT_subtool_move,
    SCULPTEXT_OT_subtool_group_new,
    SCULPTEXT_OT_subtool_move_to_group,
    SCULPTEXT_OT_subtool_toggle_expand,
    SCULPTEXT_OT_subtool_merge,
    SCULPTEXT_OT_subtool_split_loose,
    SCULPTEXT_OT_subtool_add,
    SCULPTEXT_OT_subtool_mirror,
    SCULPTEXT_OT_subtool_show_all,
    SCULPTEXT_OT_subtool_frame_active,
    SCULPTEXT_OT_subtool_split_faceset,
    SCULPTEXT_OT_subtool_split_mask,
    SCULPTEXT_OT_subtool_multires_step,
    SCULPTEXT_OT_subtool_bool_set_op,
    SCULPTEXT_OT_subtool_bool_preview,
    SCULPTEXT_OT_subtool_bool_apply,
    SCULPTEXT_OT_subtool_bool_direct,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
