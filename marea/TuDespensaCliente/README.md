# TuDespensa — Cliente Web (SPA)

Aplicación web para la gestión de inventario doméstico de alimentos y generación de recetas basadas en el stock disponible en casa. Proyecto desarrollado para el módulo de Desarrollo Web en Entorno Cliente (2º DAW).

---

## Planificación y Backlog

Funcionalidades divididas en piezas incrementales y ordenadas por prioridad de implementación:

| Prioridad | Historia / Pieza funcional | Descripción y criterio de prueba | Estado |
| :--- | :--- | :--- | :--- |
| **1 (Sprint 1)** | **Estructura, navegación y datos base** | Menú funcional entre vistas, módulo de datos con categorías, alimentos y recetas (≥10 registros) y configuración de ESLint sin errores. | Completado |
| **2 (Sprint 1)** | **Listado dinámico y vista de detalle** | Renderizado dinámico desde JS del catálogo de alimentos/recetas y apertura de ficha detallada al pulsar sobre un elemento. | Completado |
| **3 (Sprint 2)** | **Formularios, validación y persistencia (`localStorage` y Cookies)** | Capa de acceso a datos (`almacen.js`), módulo de validación (`validacion.js`), CRUD completo de usuarios en `Registro`, formulario de soporte con cookies en `Contacto` y confirmación con `<dialog>`. | Completado |
| **4 (Sprint 3)** | **Búsqueda y filtrado por categoría** | Filtro reactivo en tiempo real por nombre de ingrediente y por categoría (Lácteos, Verduras, Despensa, etc.). | Pendiente |
| **5 (Sprint 3)** | **Alta y baja de stock con validación** | Formulario para añadir nuevos alimentos al inventario con validación de campos, control de duplicados y eliminación de stock en `localStorage`. | Pendiente |
| **6 (Sprint 4)** | **Motor de sugerencia de recetas** | Cruce dinámico entre los ingredientes disponibles en stock y los ingredientes requeridos por cada receta. | Pendiente |
| **7 (Sprint 5)** | **Consumo de API externa y autenticación** | Conexión asíncrona (`fetch`) para carga de datos/recetas y gestión de sesión simulada en `Acceso`. | Pendiente |

---

## Hito 2: Formularios, Validación y Almacenamiento Local

### Mapa de validación (`js/validacion.js`)

| Formulario | Campo | Regla de validación | Mensaje de error |
| :--- | :--- | :--- | :--- |
| **Registro** | `usuario` | Obligatorio, entre 3 y 20 caracteres, solo letras (con tildes/ñ), números y guion bajo (`/^[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ]+$/`). | *"Este campo es obligatorio."* / *"El nombre de usuario debe tener al menos 3 caracteres."* / *"El nombre de usuario no puede superar 20 caracteres."* / *"Solo se permiten letras, números y guion bajo."* |
| **Registro** | `email` | Obligatorio y formato válido según expresión regular (`/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/`). | *"Este campo es obligatorio."* / *"Introduce un correo electrónico válido (ejemplo@dominio.com)."* |
| **Registro** | `fechaNacimiento` | Obligatorio, fecha válida, no futura y edad mínima de 16 años (`max="2010-11-24"`, `min="1920-01-01"`). | *"Este campo es obligatorio."* / *"Introduce una fecha válida."* / *"La fecha de nacimiento no puede ser futura."* / *"Debes tener al menos 16 años para gestionar tu despensa."* / *"La fecha introducida es demasiado antigua."* |
| **Registro** | `password` | Obligatorio, mínimo 8 caracteres, al menos 1 mayúscula y 1 número. No se guarda en `localStorage`. | *"Este campo es obligatorio."* / *"La contraseña debe tener al menos 8 caracteres."* / *"Debe incluir al menos una letra mayúscula y un número."* |
| **Registro** | `confirmar_password` | Obligatorio y coincidencia exacta con el campo `password`. | *"Este campo es obligatorio."* / *"Las contraseñas no coinciden."* |
| **Registro** | `condiciones` | Casilla (`checkbox`) marcada obligatoriamente. | *"Debes aceptar las condiciones de uso para continuar."* |
| **Contacto** | `nombre` | Obligatorio, entre 2 y 50 caracteres. | *"Este campo es obligatorio."* |
| **Contacto** | `email` | Obligatorio y formato válido según expresión regular (`/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/`). | *"Este campo es obligatorio."* / *"Introduce un correo electrónico válido (ejemplo@dominio.com)."* |
| **Contacto** | `telefono` | Opcional por defecto; obligatorio si se marca `prefieroLlamada`. Formato español de 9 dígitos (`/^(?:\+34\s?)?[6789]\d{8}$/`). | *"El teléfono es obligatorio si prefieres que te llamemos."* / *"Introduce un teléfono español válido de 9 dígitos."* |
| **Contacto** | `motivo` | Selección obligatoria dentro de las opciones de soporte de la aplicación. | *"Este campo es obligatorio."* |
| **Contacto** | `mensaje` | Obligatorio, entre 15 y 300 caracteres con contador en tiempo real. | *"Este campo es obligatorio."* / *"El mensaje debe tener al menos 15 caracteres."* / *"El mensaje no puede superar los 300 caracteres."* |

### Resumen del Hito 2

* **Qué se ha hecho:**
  * Creación de la capa de persistencia `js/almacen.js` (`obtenerTodos`, `obtenerPorId`, `crear`, `actualizar`, `borrar`) centralizando el acceso a `localStorage`.
  * Implementación del módulo `js/validacion.js` reutilizable en todos los formularios, validando en `blur` y en `input`/`change` tras el primer foco, con atributos de accesibilidad (`aria-invalid`, `aria-describedby` y `role="alert"`).
  * CRUD completo de usuarios en `registro.html` (sin almacenar la contraseña en el navegador) reutilizando el mismo formulario para creación y edición, y listado dinámico con delegación de eventos.
  * Formulario de soporte en `contacto.html` con validación cruzada entre casilla de llamada y teléfono, contador de caracteres, listado de mensajes enviados y persistencia de nombre y correo mediante cookies con caducidad de 7 días.
  * Confirmación previa al borrado mediante el elemento nativo `<dialog>` en ambos listados.
* **Qué falta:**
  * Conectar el formulario de alta de alimentos de `inventario.html` con `almacen.js` para persistir el stock del usuario.
  * Implementar el buscador y filtrado por categorías en tiempo real.
  * Desarrollar la lógica de inicio de sesión en `acceso.html` y el cruce de ingredientes para sugerir recetas en `recetas.html`.
* **Qué ha costado más:**
  * Coordinar el estado de edición en `registro.html` para que el mismo formulario sirva tanto para crear como para actualizar un usuario existente sin perder las validaciones ni dejar errores residuales al cancelar la edición.
  * Gestionar la validación cruzada en `contacto.html` (hacer obligatorio el teléfono dinámicamente al marcar «Prefiero que me llaméis» y reevaluar su estado al desmarcarlo).

---

## Mapa de Pantallas

| Vista / Archivo | Ruta | Datos que muestra |
| :--- | :--- | :--- |
| **Inicio** | `index.html` | Banner de acción rápida, resumen del estado de la despensa y accesos directos a las secciones principales. |
| **Mi Inventario** | `inventario.html` | Listado dinámico de alimentos en stock (nombre, categoría, cantidad, caducidad), formulario de alta y panel de **detalle del alimento** al hacer clic. |
| **Recetas Sugeridas** | `recetas.html` | Listado de recetas compatibles con el stock (título, tiempo, dificultad, ingredientes usados). |
| **Acceso** | `acceso.html` | Formulario de inicio de sesión (correo electrónico y contraseña) y enlace a registro. |
| **Registro** | `registro.html` | Formulario de creación y edición de cuentas de usuario con validación completa y listado de usuarios registrados en `localStorage`. |
| **Contacto** | `contacto.html` | Formulario de soporte y sugerencias con validación cruzada, cookies para recordar datos y listado de mensajes enviados. |

---

## Estructura del Proyecto

```text
├── index.html          # Pantalla principal
├── inventario.html     # Gestión de stock y detalle de alimentos
├── recetas.html        # Listado de recetas sugeridas
├── acceso.html         # Inicio de sesión
├── registro.html       # Registro y gestión CRUD de usuarios
├── contacto.html       # Soporte, sugerencias y mensajes enviados
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
│   ├── almacen.js      # Capa de persistencia sobre localStorage
│   ├── validacion.js   # Funciones de validación de formularios
│   ├── datos.js        # Entidades base (categorías y alimentos)
│   ├── ui.js           # Funciones de renderizado en el DOM
│   └── main.js         # Punto de entrada, eventos y cookies
├── BRIEF.md            # Brief órbita 1
├── ORBITA2.md          # Sistema visual órbita 2
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