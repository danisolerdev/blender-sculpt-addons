"""Empaqueta addons como zip de extension Blender (carpeta en la raiz del zip).

Uso:
    python build_addons.py                 # empaqueta todos los cambiados abajo
    python build_addons.py macropad_bridge # empaqueta solo uno

Lee la version del blender_manifest.toml de cada addon para nombrar el zip.
Excluye __pycache__ y archivos .pyc.
"""

import os
import re
import sys
import zipfile

# Addons a empaquetar por defecto (los que cambiamos).
DEFAULT_ADDONS = ("macropad_bridge", "brush_focus_ring")

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")


def read_version(addon: str) -> str:
    manifest = os.path.join(ROOT, addon, "blender_manifest.toml")
    with open(manifest, encoding="utf-8") as fh:
        text = fh.read()
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    if not match:
        raise SystemExit(f"No encuentro version en {manifest}")
    return match.group(1)


def build(addon: str) -> str:
    version = read_version(addon)
    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, f"{addon}-{version}.zip")
    src = os.path.join(ROOT, addon)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for base, dirs, files in os.walk(src):
            dirs[:] = [d for d in dirs if d != "__pycache__"]
            for name in files:
                if name.endswith(".pyc"):
                    continue
                full = os.path.join(base, name)
                arc = os.path.relpath(full, ROOT).replace(os.sep, "/")
                zf.write(full, arc)
    return out


def main() -> None:
    addons = sys.argv[1:] or list(DEFAULT_ADDONS)
    for addon in addons:
        out = build(addon)
        with zipfile.ZipFile(out) as zf:
            count = len([n for n in zf.namelist() if not n.endswith("/")])
        print(f"OK  {os.path.relpath(out, ROOT)}  ({count} archivos)")


if __name__ == "__main__":
    main()
