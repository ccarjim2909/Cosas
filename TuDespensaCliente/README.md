# TuDespensa — Cliente Web (SPA)

Aplicación web para la gestión de inventario doméstico de alimentos y generación de recetas basadas en el stock disponible en casa. Proyecto desarrollado para el módulo de Desarrollo Web en Entorno Cliente (2º DAW).

---

## Planificación y Backlog

Funcionalidades divididas en piezas incrementales y ordenadas por prioridad de implementación:

| Prioridad | Historia / Pieza funcional | Descripción y criterio de prueba | Estado |
| :--- | :--- | :--- | :--- |
| **1 (Sprint 1)** | **Estructura, navegación y datos base** | Menú funcional entre vistas, módulo de datos con categorías, alimentos y recetas (≥10 registros) y configuración de ESLint sin errores. | En curso |
| **2 (Sprint 1)** | **Listado dinámico y vista de detalle** | Renderizado dinámico desde JS del catálogo de alimentos/recetas y apertura de ficha detallada al pulsar sobre un elemento. | En curso |
| **3 (Sprint 2)** | **Búsqueda y filtrado por categoría** | Filtro reactivo en tiempo real por nombre de ingrediente y por categoría (Lácteos, Verduras, Despensa, etc.). | Pendiente |
| **4 (Sprint 3)** | **Alta y baja de stock con validación** | Formulario para añadir nuevos alimentos al inventario con validación de campos, control de duplicados y eliminación de stock. | Pendiente |
| **5 (Sprint 3)** | **Persistencia local (`localStorage`)** | Almacenamiento del inventario del usuario y sus preferencias de tema (claro/oscuro) en el navegador. | Pendiente |
| **6 (Sprint 4)** | **Motor de sugerencia de recetas** | Cruce dinámico entre los ingredientes disponibles en stock y los ingredientes requeridos por cada receta. | Pendiente |
| **7 (Sprint 5)** | **Consumo de API externa y autenticación** | Conexión asíncrona (`fetch`) para carga de datos/recetas y gestión de sesión simulada en `Acceso` y `Registro`. | Pendiente |

---

## Mapa de Pantallas

| Vista / Archivo | Ruta (Sprint 1) | Datos que muestra |
| :--- | :--- | :--- |
| **Inicio** | `index.html` | Banner de acción rápida, resumen del estado de la despensa y accesos directos a las secciones principales. |
| **Mi Inventario** | `inventario.html` | Listado dinámico de alimentos en stock (nombre, categoría, cantidad, caducidad), buscador/filtro, formulario de alta y panel/modal de **detalle del alimento** al hacer clic. |
| **Recetas Sugeridas** | `recetas.html` | Listado de recetas compatibles con el stock (título, tiempo, dificultad, ingredientes usados) y **ficha de detalle de la receta** (pasos de preparación e ingredientes completos). |
| **Acceso** | `acceso.html` | Formulario de inicio de sesión (correo electrónico y contraseña) y enlace a recuperación/registro. |
| **Registro** | `registro.html` | Formulario de creación de cuenta nueva con confirmación de contraseña. |

---

## Estructura del Proyecto

```text
├── index.html          # Pantalla principal
├── inventario.html     # Gestión de stock y detalle de alimentos
├── recetas.html        # Listado y detalle de recetas
├── acceso.html         # Inicio de sesión
├── registro.html       # Registro de usuario
├── css/
│   └── main.css        # Estilos compilados
├── scss/               # Arquitectura ITCSS + BEM
│   ├── elements/        
│   ├── generic/           
│   ├── objects/         
│   ├── settings/        
│   ├── tools/           
│   └── main.scss         
├── js/
│   ├── datos.js        # Entidades relacionadas (categorías, alimentos, recetas)
│   ├── ui.js           # Funciones de renderizado en el DOM y vista detalle
│   └── main.js         # Punto de entrada y gestión de eventos
├── BRIEF.md            # Brief orbita 1 de Alejandro
├── ORBITA2.md          # Orbita 2 de Alejandro
├── CHANGELOG.md        
├── README.md           
├── eslint.config.js    # Configuración de ESLint
└── package.json        # Dependencias de desarrollo

```


---

### Configuración de ESLint

Ejecuta en la terminal dentro de la carpeta del proyecto para inicializar `package.json` e instalar ESLint:

```bash
npm init -y
npm install --save-dev eslint @eslint/js globals
```


--------
# 👤 Autor
* **Alumno:** Cristian Carrasco Jiménez
* **Curso:** 2º DAW — IES Rafael Alberti
