const formularioBusqueda = document.querySelector(".formulario-busqueda");
const entradaBusqueda = document.querySelector(".js-busqueda-entrada");
const listaResultados = document.querySelector(".js-resultados-lista");
const mensajeResultados = document.querySelector(".js-resultados-mensaje");
const botonesFiltro = document.querySelectorAll(".filtros__boton");
const listaSugerencias = document.querySelector(".js-busqueda-sugerencias");
const contenedorPaginacion = document.querySelector(".js-paginacion");

let paginaActual = 0;
let categoriaActual = "games";
let consultaActual = "";
let hayPaginaSiguiente = false;
let temporizadorSugerencias;

/* ============================= */
/* BOTONES ACTIVOS */
function actualizarBotonesActivos(categoria) {
  botonesFiltro.forEach((boton) => {
    boton.classList.toggle(
      "filtros__boton--activo",
      boton.dataset.categoria === categoria
    );
  });
}

/* ============================= */

function actualizarMensajeResultados(mensaje) {
  mensajeResultados.textContent = mensaje;
}

function ocultarSugerencias() {
  listaSugerencias.innerHTML = "";
  listaSugerencias.classList.remove("sugerencias--visible");
}

/* ============================= */

function pintarSugerencias(sugerencias) {
  if (!sugerencias.length) return ocultarSugerencias();

  listaSugerencias.innerHTML = sugerencias.map(s => `
    <li class="sugerencias__item">
      <button class="sugerencias__boton"
        data-nombre="${s.nombre}"
        data-categoria="${s.categoria}">
        <span class="sugerencias__titulo">${s.nombre}</span>
        <span class="sugerencias__meta">${s.etiquetaCategoria}</span>
      </button>
    </li>
  `).join("");

  listaSugerencias.classList.add("sugerencias--visible");
}

/* ============================= */

async function buscarSugerencias(consulta) {

  const texto = consulta.trim();

  if (texto.length < 2) {
    ocultarSugerencias();
    return;
  }

  try {
    const variantes = obtenerVariantesConsulta(texto);

    const peticiones = CATEGORIAS_SUGERENCIAS.flatMap(cat =>
      variantes.map(v =>
        fetch(construirUrlCategoria(cat, v, 3, 0))
          .then(r => r.ok ? r.json() : { data: [] })
          .catch(() => ({ data: [] }))
          .then(res => ({ res, cat }))
      )
    );

    const respuestas = await Promise.all(peticiones);

    const sugerencias = [];
    const usados = new Set();

    respuestas.forEach(({ res, cat }) => {
      (res.data || []).forEach(e => {

        const nombre = e.name || "";
        const clave = `${cat}-${limpiarTextoBusqueda(nombre)}`;

        if (!nombre || usados.has(clave) || !coincideTextoBusqueda(nombre, texto)) return;

        sugerencias.push({
          nombre,
          categoria: cat,
          etiquetaCategoria: CONFIGURACION_CATEGORIAS[cat].etiqueta
        });

        usados.add(clave);
      });
    });

    pintarSugerencias(sugerencias.slice(0, 8));

  } catch {
    ocultarSugerencias();
  }
}

/* ============================= */

async function buscarCategoria(categoria, consulta, pagina = 0) {

  categoriaActual = categoria;
  consultaActual = consulta;
  paginaActual = pagina;

  actualizarBotonesActivos(categoria); // 🔥 FIX

  actualizarMensajeResultados("Buscando...");
  listaResultados.innerHTML = "";

  try {

    const res = await fetch(construirUrlCategoria(categoria, consulta, 12, pagina));
    const data = await res.json();

    const elementos = data.data.map(e => normalizarElemento(e, categoria));

    listaResultados.innerHTML = elementos.map(e => crearMarcadoTarjeta(e)).join("");

    actualizarMensajeResultados("Resultados cargados");

  } catch (error) {

    listaResultados.innerHTML = `
      <li class="galeria__item">
        <p class="estado-vacio">
          Error al cargar datos de la API.
        </p>
      </li>
    `;

    actualizarMensajeResultados("Error de conexión");
  }
}

/* ============================= */

function construirElementoFavorito(tarjeta, botonFavorito) {

  const titulo = tarjeta.querySelector(".tarjeta-zelda__titulo")?.textContent || "";
  const descripcion = tarjeta.querySelector(".tarjeta-zelda__descripcion")?.textContent || "";
  const categoria = tarjeta.dataset.categoria;

  return {
    uid: botonFavorito.dataset.favorito,
    id: botonFavorito.dataset.favorito.split("-").slice(1).join("-"),
    category: categoria,
    categoryLabel: tarjeta.querySelector(".tarjeta-zelda__tipo")?.textContent || "",
    name: titulo,
    description: descripcion,
    detailUrl: "#",
    meta: []
  };
}

/* ============================= */
/* FAVORITOS */

listaResultados.addEventListener("click", (evento) => {

  const botonFavorito = evento.target.closest("[data-favorito]");

  if (!botonFavorito) return;

  const tarjeta = botonFavorito.closest(".tarjeta-zelda");

  const elemento = construirElementoFavorito(tarjeta, botonFavorito);

  const guardado = alternarFavorito(elemento);

  botonFavorito.classList.toggle("tarjeta-zelda__favorito--activo", guardado);

  botonFavorito.innerHTML = guardado ? "&#9733;" : "&#9734;";

  botonFavorito.setAttribute(
    "aria-label",
    guardado ? "Quitar de favoritos" : "Guardar en favoritos"
  );
});

/* ============================= */
/* EVENTOS */

formularioBusqueda.addEventListener("submit", (e) => {
  e.preventDefault();
  buscarCategoria(categoriaActual, entradaBusqueda.value, 0);
});

botonesFiltro.forEach(btn => {
  btn.addEventListener("click", () => {
    buscarCategoria(btn.dataset.categoria, entradaBusqueda.value, 0);
  });
});

entradaBusqueda.addEventListener("input", () => {
  clearTimeout(temporizadorSugerencias);
  temporizadorSugerencias = setTimeout(() => {
    buscarSugerencias(entradaBusqueda.value);
  }, 250);
});

entradaBusqueda.addEventListener("focus", () => {
  if (entradaBusqueda.value.length >= 2) {
    buscarSugerencias(entradaBusqueda.value);
  }
});

document.addEventListener("click", (e) => {
  if (!e.target.closest(".formulario-busqueda__campo")) {
    ocultarSugerencias();
  }
});

listaSugerencias.addEventListener("click", (e) => {

  const btn = e.target.closest(".sugerencias__boton");

  if (!btn) return;

  entradaBusqueda.value = btn.dataset.nombre;
  categoriaActual = btn.dataset.categoria;

  buscarCategoria(categoriaActual, entradaBusqueda.value, 0);
});

/* ============================= */

buscarCategoria("games", "", 0);