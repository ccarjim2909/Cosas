# Brief de Proyecto — TuDespensa

## 1. El problema que resuelve la aplicación
A través de la investigación inicial y las entrevistas a usuarios reales (como el perfil principal, María), identificamos dos problemas cotidianos fundamentales en los hogares: la **"pereza"** asociada a la planificación diaria de las comidas ("¿qué hago hoy de comer?") y el **desperdicio involuntario de alimentos** por olvido de productos en el fondo de la despensa o caducidad.

La investigación reveló que los usuarios no buscan un recetario genérico con cientos de opciones complejas, sino una solución práctica e inmediata que les diga qué preparar **basándose exclusivamente en el stock real** que ya tienen en casa, reduciendo el tiempo de decisión y optimizando la compra.

---

## 2. Alcance (MVP)
Para esta primera entrega (Órbita 1), el alcance de la aplicación se enfoca en el flujo mínimo viable (*Happy Path*):

### Dentro del alcance (MVP):
* **Autenticación:** Pantallas básicas de Iniciar Sesión y Registro (`Acceso` y `Registro`).
* **Gestión de Stock:** Visualización del inventario en despensa (`Mi Inventario`).
* **Entrada Dual de Alimentos:** 
  * Entrada manual rápida con autocompletado de texto.
  * Captura/escaneo visual con cámara e IA (`Escanear Alimento`).
* **Motor de Recomendación con IA:** Generación de propuestas de recetas adaptadas al stock disponible (`Recetas Sugeridas`).
* **Caso Límite:** Acción de regenerar o solicitar nuevas alternativas si las propuestas no convencen.

### Fuera del alcance (Fases posteriores):
* Asistente interactivo de cocina paso a paso con temporizadores integrados.
* Planificador semanal de menús o lista de la compra automática.
* Red social para compartir recetas o valoraciones de la comunidad.

---

## 3. Personas
El diseño de la arquitectura y la interfaz se sostiene sobre dos perfiles de usuario extraídos de las entrevistas:

1. **María (User Persona Principal):** Ama de casa. Busca practicidad, rapidez y cero fatiga mental al cocinar. Es el eje central del *Happy Path*.
   * *Enlace a la ficha en FigJam:* [Ficha de María - FigJam](https://www.figma.com/board/DJwMlzohkiN2MRl1iydHln/ideas-proyecto-dise%C3%B1o?node-id=7-248&t=8CbKoGoWE2fL6xe9-0)
2. **Manuela (User Persona Secundaria / Caso Límite):** Limpiadora con horario apretado. Prefiere la búsqueda y entrada manual directa en lugar del escáner por cámara.
   * *Enlace a la ficha en FigJam:* [Ficha de Manuela - FigJam](https://www.figma.com/board/DJwMlzohkiN2MRl1iydHln/ideas-proyecto-dise%C3%B1o?node-id=7-319&t=8CbKoGoWE2fL6xe9-0)

---

## 4. Criterios de éxito
Para verificar la usabilidad y eficiencia del diseño durante las pruebas de usuario (Órbita 5), se establecen los siguientes criterios cuantificables:

1. **Eficiencia en el menú (María):** María puede consultar las 3 propuestas de recetas recomendadas por la IA en **menos de 3 clics y en menos de 15 segundos** desde que abre la pantalla de inicio.
2. **Entrada de datos (Manuela):** Manuela puede añadir un nuevo alimento mediante búsqueda manual e incorporarlo a su despensa sin cometer errores de navegación en **menos de 10 segundos**.
3. **Casos Límite:** Un usuario con la despensa vacía o a quien no le convengan las primeras recetas puede solicitar nuevas sugerencias mediante el botón *"Generar otras recetas"* sin tener que reiniciar el flujo.

---

## 5. Restricciones

### Tecnológicas
* Integración de la interfaz web/móvil con el backend desarrollado en DWES/DWEC.
* Conexión mediante API a un modelo de lenguaje para la generación de recetas en tiempo real a partir del listado de ingredientes.

### De tiempo y usuario
* El desarrollo se acoge al marco temporal de 4 semanas establecido para la Órbita 1.
* Mantenimiento de objetivos táctiles de gran tamaño (mínimo 48px de altura) e interfaces de baja densidad de elementos para facilitar su uso a usuarios con menor destreza digital.

### Ambientales / Sostenibilidad Web (Criterio 2.4 WSG)
* **Presupuesto de Peso de Página:** Para minimizar la huella de carbono y garantizar un rendimiento óptimo en dispositivos móviles con conexiones lentas, el peso total de assets por pantalla no superará los **500 KB**.
* Uso estricto de componentes vectoriales, tipografías del sistema e imágenes optimizadas en escala de grises para reducir el consumo energético en pantallas OLED y el tráfico de datos en red.