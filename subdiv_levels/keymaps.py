"""Registro y limpieza de atajos del addon Subdiv Levels.

Ctrl+D  → sculpt_ext.subdiv_smart  (Sculpt y Object Mode)
Shift+D → sculpt_ext.level_down    (solo Sculpt: en Object colisiona con Duplicar)
Alt+D   → sculpt_ext.level_up      (solo Sculpt)
"""

import bpy

from . import utils

# Pares (keymap, keymap_item) creados por el addon, para limpiarlos en unregister().
addon_keymaps = []


def register_keymaps():
    """Crea los atajos si están habilitados en las preferencias."""
    prefs = utils.get_prefs()
    if not prefs.enable_hotkeys:
        return

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc is None:  # modo background: no hay keyconfig de addon
        return

    km_sculpt = kc.keymaps.new(name="Sculpt", space_type='EMPTY')
    for idname, key, kwargs in (
        ("sculpt_ext.subdiv_smart", 'D', {"ctrl": True}),
        ("sculpt_ext.level_down", 'D', {"shift": True}),
        ("sculpt_ext.level_up", 'D', {"alt": True}),
    ):
        kmi = km_sculpt.keymap_items.new(idname, key, 'PRESS', **kwargs)
        addon_keymaps.append((km_sculpt, kmi))

    km_object = kc.keymaps.new(name="Object Mode", space_type='EMPTY')
    kmi = km_object.keymap_items.new("sculpt_ext.subdiv_smart", 'D', 'PRESS', ctrl=True)
    addon_keymaps.append((km_object, kmi))


def unregister_keymaps():
    """Elimina todos los atajos creados por el addon."""
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def register():
    register_keymaps()


def unregister():
    unregister_keymaps()
