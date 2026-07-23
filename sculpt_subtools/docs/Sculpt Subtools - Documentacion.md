# Sculpt Subtools — Addon para Blender

> Paleta de **subtools estilo ZBrush** para gestionar las mallas de la escena sin salir de Sculpt.
> Versión **0.4.0** · Blender **5.0+** · Licencia GPL-3.0-or-later

---

## ¿Qué hace?

Añade una **paleta de subtools** en el modo Sculpt, igual que la de ZBrush: una lista siempre a
mano para saltar entre mallas, aislarlas, ocultarlas, duplicarlas, borrarlas, renombrarlas,
unirlas, partirlas, agruparlas y reordenarlas — todo sin ir y venir al Outliner.

Idea clave: **en Blender los subtools ya existen**. Cada objeto malla *es* un subtool y cada
colección *es* un "Tool". El addon no crea un modelo de datos propio: solo aporta la
**UX/paleta** que Blender no trae de serie para esculpir. Lo que ves en la paleta son objetos y
colecciones reales, también visibles en el Outliner.

---

## Instalación

1. Localiza el zip: `dist/sculpt_subtools-0.4.0.zip`.
2. En Blender: **Edit → Preferences → Get Extensions**.
3. Flecha desplegable (esquina superior derecha) → **Install from Disk…**
4. Selecciona el zip. Se instala y activa automáticamente.

Para actualizar, reconstruye el zip y repite *Install from Disk*:

```
blender --command extension build --source-dir sculpt_subtools --output-dir dist
```

---

## La paleta

Viewport 3D → barra lateral (`N`) → pestaña **Subtools**. Visible en Sculpt y en Objeto.

Muestra el árbol **Tool → Grupos → SubTools** del objeto activo:

- **Fila de grupo**: triángulo de plegado, ojito de visibilidad y nombre de la sub-colección.
- **Fila de subtool** (indentada): miniatura (opcional), ojito, marca de subtool activo, nombre
  editable en línea y botón de **Solo**. Al hacer clic en el nombre, ese subtool pasa a ser el
  activo.
- **Pie**: número de subtools y nombre + recuento de caras del activo.

La paleta no guarda estado propio: siempre refleja las colecciones y objetos reales.

---

## Acciones principales

| Acción | Qué hace |
|---|---|
| **Activar** (clic en el nombre) | Hace activo ese subtool. Desde Sculpt hace un "rebote" rápido Objeto→Sculpt y te deja de nuevo esculpiendo el nuevo subtool |
| **Ciclar** (prev/siguiente) | Salta al subtool anterior o siguiente en el orden del árbol |
| **Solo / aislar** | Oculta todo menos el subtool activo (o su grupo); al desactivarlo restaura exactamente la visibilidad previa |
| **Visibilidad** (ojito) | Muestra u oculta un subtool concreto |
| **Duplicar / Borrar** | Duplica el activo o lo elimina (con confirmación) |
| **Renombrar** | Edición en línea del nombre |
| **Subir / Bajar** | Reordena el subtool dentro de su colección |
| **Agrupar / Mover a grupo** | Crea sub-colecciones y mueve subtools entre ellas |
| **Merge** | Une los subtools seleccionados en el activo (avisa: el Multires no se conserva al unir) |
| **Split por partes sueltas** | Separa el activo en un subtool por cada parte suelta de la malla |

### Funciones avanzadas (fases 2–5, ya incluidas)

- **Añadir / Espejar**: crear una primitiva como subtool o una copia reflejada.
- **Split por Face Set** y **Split por máscara**: partir el activo según sus face sets o su
  máscara de esculpido.
- **Globales**: mostrar todos, encuadrar el activo en la vista.
- **Integración con Subdiv Levels**: si el subtool activo tiene Multires, la paleta muestra una
  fila de nivel para subir/bajar (autocontenida, sin dependencia dura del otro addon).
- **Booleanas**: rol por subtool (Add/Subtract/Intersect), previsualización con modificador
  Boolean, aplicar el resultado, y booleanas directas activo vs. seleccionados.
- **Miniaturas**: preview por subtool capturado del viewport, estilo ZBrush; refresco manual o
  automático al salir de un subtool y al crear/duplicar/separar.

---

## Preferencias

En **Preferences → Add-ons → Sculpt Subtools**:

| Opción | Por defecto | Descripción |
|---|---|---|
| Volver a Sculpt al saltar | ✅ | Tras cambiar de subtool desde Sculpt, vuelve a Sculpt |
| Solo incluye el grupo | ❌ | Solo mantiene visible todo el grupo del objetivo, no solo el objeto |
| Confirmar al borrar | ✅ | Pide confirmación antes de eliminar un subtool |
| Confirmar al unir (merge) | ✅ | Pide confirmación antes de unir subtools |
| Activar atajos | ❌ | Registra los atajos opcionales de ciclado (off por defecto, para no pisar Sculpt) |
| Modo de orden | Manual | Manual (arrastrar con subir/bajar) o por Nombre |
| Mostrar miniaturas | ✅ | Dibuja la preview de cada subtool |
| Miniaturas automáticas | ✅ | Recaptura al salir de un subtool y al crear/duplicar/separar |
| Escala de miniatura | 3.0 | Tamaño de la preview en la paleta |

---

## Atajos

Opcionales y **desactivados por defecto** (el keymap de Sculpt está muy poblado). Se activan en
preferencias:

| Atajo | Acción |
|---|---|
| `Alt+↑` | Subtool anterior |
| `Alt+↓` | Subtool siguiente |

---

## Estructura del código

```
sculpt_subtools/
├── blender_manifest.toml   # metadatos de la extensión (formato Blender 4.2+)
├── __init__.py             # register()/unregister()
├── operators.py            # operadores sculpt_ext.subtool_*
├── ui.py                   # paleta (árbol dibujado a mano)
├── properties.py           # propiedades sobre Object/Collection/Scene (orden, solo, expand)
├── preview.py              # miniaturas por subtool (GPUOffScreen)
├── auto.py                 # recaptura automática de miniaturas
├── keymaps.py              # atajos opcionales
├── preferences.py          # AddonPreferences
├── translations.py         # traducciones
└── utils.py                # Tool root, recorrido del árbol, validaciones
```

Para la especificación técnica completa (modelo de datos, cada operador, fases y decisiones de
diseño), ver **[Sculpt Subtools - Especificacion.md](Sculpt%20Subtools%20-%20Especificacion.md)**.

---

## Compatibilidad e idiomas

- Blender **5.0+** (desarrollado y validado sobre 5.1.0/5.1.2).
- Interfaz traducida a español, francés, alemán, chino simplificado, japonés, coreano,
  portugués e italiano.

---

## Historial

| Versión | Cambios |
|---|---|
| 0.4.0 | Fases 1–5: paleta, Solo, grupos, merge/split, booleanas, integración Multires, miniaturas |
