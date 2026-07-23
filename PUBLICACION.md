# Guía de publicación y comercialización de los addons

Paso a paso para llevar los addons de este repo (`subdiv_levels`, `sculpt_subtools`,
`brush_focus_ring`, `macropad_bridge`) desde el código a plataformas oficiales y
marketplaces reconocidos. Pensada para Blender 5.x y el formato de **extensión**.

> Regla de oro: **todo addon que usa la API `bpy` debe distribuirse como GPL-3.0**.
> Eso NO impide cobrar por él, pero sí obliga a que quien compra reciba el código
> con las mismas libertades (usar, modificar, redistribuir). Vender GPL es legal y
> habitual; lo que se vende es el *acceso a la descarga y el soporte*, no una licencia
> restrictiva.

---

## Fase 0 — Decisión de estrategia (por addon)

Antes de publicar, decide para cada addon una de estas tres rutas:

| Ruta | Dónde | Cobro | Ideal para |
|---|---|---|---|
| **A. Gratis oficial** | extensions.blender.org | No | Ganar reputación, base de usuarios, reseñas |
| **B. De pago en marketplace** | Superhive (ex-Blender Market) / Gumroad | Sí | Monetizar directamente |
| **C. Freemium** | Versión base gratis en la oficial + Pro de pago en marketplace | Sí | Lo mejor de ambos: visibilidad + ingresos |

Recomendación para tu catálogo:

- **`subdiv_levels`**: es el más "producto terminado". Candidato ideal a **freemium**
  (base gratis en la oficial para captar usuarios; Pro con extras en Superhive).
- **`sculpt_subtools`** y **`brush_focus_ring`**: empezar **gratis en la oficial**
  para construir marca antes de cobrar.
- **`macropad_bridge`**: por su naturaleza (hardware/puente) valora **Gumroad** con
  documentación, ya que el público es más de nicho.

---

## Fase 1 — Preparar el addon para publicar (checklist técnico)

Aplica a los cuatro. Un addon no pasa revisión si falla algo de esto.

- [ ] **`blender_manifest.toml` completo y correcto**: `id` único, `version`
      semántica (SemVer), `name`, `tagline` (máx. ~64 car.), `maintainer`,
      `type = "add-on"`, `tags`, `blender_version_min`, y
      `license = ["SPDX:GPL-3.0-or-later"]`.
- [ ] **Sin `bl_info`** (es del sistema clásico de addons, no de extensiones).
- [ ] **Código revisable**: nada de código ofuscado ni bytecode. La plataforma
      oficial rechaza cualquier cosa que no se pueda leer.
- [ ] **Autocontenido**: no descargar ni ejecutar código remoto. Si usas dependencias
      pip, empaquétalas como *wheels* dentro de la extensión (vendorizadas).
- [ ] **Sin telemetría oculta**: no enviar datos a servidores sin permiso explícito
      del usuario.
- [ ] **Activar/desactivar sin errores** repetidas veces (keymaps y clases limpiados
      en `unregister()`).
- [ ] **README** con: qué hace, cómo se instala, atajos, requisitos, changelog.
- [ ] **Licencia GPL** incluida (`LICENSE`) — ya está en el repo.
- [ ] **Smoke test en background** en verde
      (`blender --background --factory-startup --python tests/smoke_test.py`).
- [ ] **Probado en Blender limpio** (`--factory-startup`): el motivo #1 de rechazo es
      que el addon "no funciona" al convertirlo mal a extensión sin probar.

### Empaquetado (el .zip de extensión)

Blender genera el zip validando el manifest, no lo hagas a mano:

```bash
# Validar el manifest y el contenido
blender --command extension validate ./subdiv_levels

# Construir el paquete .zip listo para subir
blender --command extension build --source-dir ./subdiv_levels --output-dir ./dist
```

Repite para cada carpeta de addon. (Tu `build_addons.py` puede orquestar los cuatro.)

---

## Fase 2 — Publicar en la plataforma oficial (extensions.blender.org)

Es la ruta de mayor **visibilidad y confianza**, gratis, pero pasa revisión humana.

1. **Cuenta Blender ID**: inicia sesión en extensions.blender.org con tu Blender ID
   (el mismo de blender.org). No requiere cuenta de desarrollador aparte.
2. **Subir como borrador**: "Add Extension" → sube el `.zip` construido en la Fase 1.
   La plataforma valida el manifest automáticamente.
3. **Completar la ficha**: descripción larga, capturas/GIF de uso, categoría/tags,
   enlace al repositorio y al tracker de incidencias, versión de Blender soportada.
4. **Enviar a revisión (Approval Queue)**: un moderador comprueba que respeta los
   Términos de Servicio, que es GPL-compatible, que funciona con una prueba básica y
   que tú eres el autor/mantenedor.
5. **Atender el feedback**: si piden cambios, respondes en la cola de aprobación,
   subes nueva versión y se re-revisa. Suele ser un ida y vuelta rápido si el checklist
   de Fase 1 está limpio.
6. **Publicado**: aparece en el listado y es **instalable desde dentro de Blender**
   (Preferencias → Get Extensions). Las actualizaciones llegan solas a los usuarios.

> La plataforma oficial es **solo gratis**: no hay pasarela de pago. Para cobrar,
> usa la Fase 3 (marketplace). El modelo freemium combina ambas.

---

## Fase 3 — Vender en marketplaces reconocidos

### Opción 3A — Superhive (antes Blender Market)

Es el marketplace de referencia del ecosistema Blender (8+ años, +20 M$ pagados a
creadores).

1. **Solicitar ser Creator/vendedor**: alta y aprobación de la cuenta de creador.
2. **Elegir plan de suscripción de creador**: define tu comisión y las *merchant fees*.
   - Sin suscripción: comisión por defecto **70%** para ti.
   - Con suscripción de pago: sube hasta **~90%** y bajan las tarifas de transacción.
   - **No hay exclusividad**: puedes vender el mismo addon también en Gumroad o tu web.
3. **Crear el producto**: título, descripción, precio, versiones de Blender, categoría,
   imágenes/vídeo de demo, y el `.zip` de la extensión. Recuerda: la licencia sigue
   siendo GPL, así que déjalo claro en la ficha.
4. **Publicar y mantener**: sube nuevas versiones, responde reseñas y soporte.

### Opción 3B — Gumroad (tienda propia, control total)

Ideal para 0% de comisión de marketplace (Gumroad cobra su fee de plataforma) y control
del precio, cupones y email de clientes.

1. Crea cuenta de creador en Gumroad.
2. Producto digital → sube el `.zip`, precio (o "pay what you want"), portada y demo.
3. Enlaza tu Gumroad desde tu web, YouTube, redes y desde la ficha de la extensión
   oficial (versión Pro).
4. Entrega automática del archivo tras el pago; añade changelog para avisar de updates.

> Legalidad GPL en marketplaces: perfectamente válido. Vendes descarga + soporte, y el
> comprador recibe el código bajo GPL con derecho a usarlo, modificarlo y redistribuirlo.
> No puedes imponer una licencia más restrictiva ni DRM sobre el código.

---

## Fase 4 — Modelo freemium (recomendado para `subdiv_levels`)

1. **Versión Free**: funcionalidad núcleo (subir/bajar/añadir nivel, panel básico).
   Publícala en extensions.blender.org (Fase 2). Es tu canal de captación.
2. **Versión Pro**: extras de valor (fase 2 del roadmap: unsubdivide/rebuild, bake de
   displacement, presets, multi-objeto, remesh guiado por Face Sets como upsell).
   Véndela en Superhive/Gumroad (Fase 3).
3. **Puente entre ambas**: en el panel de la versión Free añade un botón/enlace discreto
   "Consigue la versión Pro" hacia tu página de venta.
4. **IDs distintos**: la Free y la Pro deben tener `id` de manifest diferentes para
   convivir instaladas sin colisionar.

---

## Fase 5 — Marketing y lanzamiento

- **Material de demo**: un GIF corto por addon mostrando el flujo clave (p. ej. `Ctrl+D`
  creando y subiendo nivel de un gesto). Es lo que más convierte.
- **Página de producto**: descripción orientada al beneficio ("niveles de subdivisión
  estilo ZBrush/Nomad dentro de Blender"), no solo a la lista de features.
- **Comunidad**: publica en r/blender, BlenderArtists, foros de escultura y grupos de
  Discord/Telegram de Blender en español. Vídeo demo en YouTube/TikTok.
- **Precio**: investiga addons similares en Superhive antes de fijarlo. Para utilidades
  de sculpt, rangos habituales de ~5–25 $. Considera un precio de lanzamiento con
  descuento las primeras semanas.
- **Changelog público** y respuesta rápida a reseñas: reputación = ventas recurrentes.

---

## Fase 6 — Mantenimiento post-publicación

- **Versionado SemVer** en cada release (`0.1.0` → `0.2.0` funcionalidad, `0.1.1` fix).
- **Compatibilidad**: prueba con cada versión LTS/nueva de Blender; actualiza
  `blender_version_min` cuando toque.
- **Soporte**: canal claro de incidencias (issues del repo o email).
- **Sincroniza versiones** entre la oficial y los marketplaces para no confundir a
  usuarios.

---

## Orden de ataque sugerido

1. Deja los cuatro addons pasando el checklist de **Fase 1** (empaquetado + smoke test).
2. Publica primero **gratis en la oficial** el más pulido (`subdiv_levels`) para validar
   el proceso de revisión de punta a punta.
3. Con la experiencia, sube el resto a la oficial.
4. Monta la **versión Pro** de `subdiv_levels` en **Superhive** y/o **Gumroad**.
5. Lanza marketing (GIFs + demo en vídeo + posts de comunidad).

---

## Fuentes

- [Creating Extensions — Blender 5.1 Manual](https://docs.blender.org/manual/en/latest/advanced/extensions/index.html)
- [Extensions — Blender Developer Documentation](https://developer.blender.org/docs/handbook/extensions/)
- [Guidelines de moderación — Blender Developer Docs](https://developer.blender.org/docs/features/extensions/moderation/guidelines/)
- [Hosting on blender.org — Blender Developer Docs](https://developer.blender.org/docs/handbook/extensions/hosted/)
- [extensions.blender.org](https://extensions.blender.org/)
- [Terms of Service — Blender Extensions](https://extensions.blender.org/terms-of-service/)
- [Superhive — Pricing](https://superhivemarket.com/pricing)
- [Cómo se calculan las comisiones — Superhive Docs](https://support.superhivemarket.com/article/32-how-commission-earnings-are-calculated)
- [Quién puede vender en Superhive — Superhive Docs](https://support.superhivemarket.com/article/55-who-can-sell-products-on-blender-market)
- [License — Blender.org](https://www.blender.org/about/license/)
- [How to Sell GPL Software — Orange Turbine](https://orangeturbine.com/how-to-sell-gpl-software-and-avoid-being-a-jerk-about-it/)
