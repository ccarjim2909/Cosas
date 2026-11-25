# Órbita 2: sistema visual de TuDespensa

## Enlaces

| Qué | Enlace |
|---|---|
| Archivo de Figma (versión "Entrega Órbita 2") | [Proyecto TuDespensa](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa) |
| Prototipo mobile | [Abrir prototipo mobile](https://www.figma.com/proto/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=665-247&t=WkevuDWBiTp2hl1o-0&scaling=min-zoom&content-scaling=fixed&page-id=596%3A6&starting-point-node-id=665%3A247&show-proto-sidebar=1) |
| Prototipo mobile(oscuro) | [Abrir prototipo mobile (oscuro)](https://www.figma.com/proto/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=751-1750&t=WkevuDWBiTp2hl1o-0&scaling=min-zoom&content-scaling=fixed&page-id=596%3A6&starting-point-node-id=751%3A1750&show-proto-sidebar=1) |
| Prototipo desktop | [Abrir prototipo desktop](https://www.figma.com/proto/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=665-303&t=WkevuDWBiTp2hl1o-0&scaling=min-zoom&content-scaling=fixed&page-id=596%3A6&starting-point-node-id=665%3A303&show-proto-sidebar=1) |
| Prototipo desktop(oscuro) | [Abrir prototipo desktop (oscuro)](https://www.figma.com/proto/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=751-2108&t=WkevuDWBiTp2hl1o-0&scaling=min-zoom&content-scaling=fixed&page-id=596%3A6&starting-point-node-id=751%3A2108&show-proto-sidebar=1) |


## Dónde está cada cosa en Figma

| Entregable | Página y sección del archivo |
|---|---|
| Inventario de decisiones | [Orbita 2](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=584-6&p=f&t=WkevuDWBiTp2hl1o-0) |
| Wireframes rediseñados con sus notas | [Wireframes (Mobile)](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=4-6&p=f&t=WkevuDWBiTp2hl1o-0) y [Wireframes (Desktop)](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=549-12&p=f&t=WkevuDWBiTp2hl1o-0)|
| Componentes | [Componentes](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=597-7&p=f&t=WkevuDWBiTp2hl1o-0) |
| Mockups del happy path | [Mobile](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=665-247&t=WkevuDWBiTp2hl1o-0) y [Desktop](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=665-303&t=WkevuDWBiTp2hl1o-0) |
| Pantallas en modo oscuro | [Mobile](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=751-1750&t=WkevuDWBiTp2hl1o-0) y [Desktop](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=751-2108&t=WkevuDWBiTp2hl1o-0) |
| Guía de estilo | [Guía](https://www.figma.com/design/195GvADRkNIFLydCVnL7qa/Proyecto-TuDespensa?node-id=771-120&t=WkevuDWBiTp2hl1o-0) |

## Lista de comprobación de Figma

- [x] Variables en dos colecciones (primitivos y semánticos), con alias, modos claro y oscuro, ámbito, descripción y sintaxis de código.
- [x] Estilos de texto, efecto y retícula vinculados a las variables. 
- [x] Componentes con Auto layout, variables, propiedades y variantes de estado. 
- [x] Mockups construidos enteros con Auto layout y espacios sacados de variables. 
- [x] Pantalla principal en un segundo ancho, con los mismos componentes. 
- [x] Modo oscuro aplicado con el selector de modo. 
- [x] Prototipo que recorre el happy path completo. 
- [x] Prueba 1 superada: al cambiar `color/primario`, cambian todas las pantallas a la vez. 
- [x] Prueba 2 superada: con todos los mockups en modo oscuro, nada desaparece contra el fondo.

## Resumen de decisiones

### Rediseño de los wireframes

Se prepararon mockups móviles de Inicio, Inventario, Recetas, Escáner, Acceso y Registro, y sus versiones de escritorio donde corresponden. El cambio principal fue convertir los flujos prioritarios en pantallas de alta fidelidad y conectarlos mediante componentes reutilizables, manteniendo el estilo del trabajo previo. Se priorizó móvil y se conservaron el inventario y las recetas como tareas centrales del producto.

### Color

El color principal documentado es el verde `color/primario` (`#1C5E3A`); como apoyo se usan la superficie verde suave `color/superficie` (`#F1F8F3`) y el carbón `color/acento` (`#161E19`). La paleta mantiene una identidad natural coherente con una aplicación de despensa y alimentos, mas explicado en la guía de estilos.

### Tipografía

La guía identifica IBM Plex Serif para títulos, IBM Plex Sans para textos e IBM Plex Sans Condensed para feedback. Los botones usan IBM Plex Sans Medium. La combinación diferencia los encabezados del texto funcional y mantiene una lectura clara en los controles.

### Espaciado y retícula

La escala usa una base de **8 px** y micro-pasos de **4 px**. Para el ancho móvil principal (frames actuales de 412 px) se aplica una retícula de **4 columnas**, medianil de **16 px** y márgenes de **16 px**. Para escritorio hay 12 columnas, medianil de 24 px y márgenes de 64 px. No se añadieron pantallas Tablet.

### Componentes

- **Botón Primario, Secundario** Mediano y Grande; Reposo, Al pasar y Deshabilitado.
- **Enlace de navegación:** Pequeño y Mediano; Reposo y Activo.
- **Pestaña y Opción de menú:** Activo y Reposo.
- **Escanér:** Visor de camara y marco del enfoque.
- **Tarjetas de contenido:** Banner / Recetas, Tarjeta / Acceso, Recetas Sugeridas y Propuesta / 1–2. Reutilizadas en Inicio y Recetas.
- **Ilustraciones de alimentos:** Iconos añadidos por libreria.

### Responsive y modo oscuro

La pantalla principal está representada en 412 px y 1440 px. La adaptación se realizó mediante layouts separados para móvil y escritorio, en Inventario de escritorio se quitó el acceso al Escáner y se amplió la entrada manual de alimentos.

Las variables documentan modos Claro/Oscuro.

## Uso de IA

La mayor parte de redactar la documentacion ha sido por parte de la IA. El detalle está en el [CHANGELOG.md](CHANGELOG.md).

## Lo que ha quedado pendiente

- La acción manual «Añadir alimento» en Inventario de escritorio no tiene una pantalla de confirmación verificada.

