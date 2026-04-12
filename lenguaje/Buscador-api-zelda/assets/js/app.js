const formularioBusqueda = document.querySelector(".formulario-busqueda");
const entradaBusqueda = document.querySelector(".js-busqueda-entrada");
const selectorCategoria = document.querySelector(".js-busqueda-categoria");
const listaResultados = document.querySelector(".js-resultados-lista");
const mensajeResultados = document.querySelector(".js-resultados-mensaje");
const resumenFavoritos = document.querySelector(".js-resumen-favoritos");
const resumenCategoria = document.querySelector(".js-resumen-categoria");
const resumenEstado = document.querySelector(".js-resumen-estado");
const botonesFiltro = document.querySelectorAll(".filtros__boton");
const listaSugerencias = document.querySelector(".js-busqueda-sugerencias");
const contenedorPaginacion = document.querySelector(".js-paginacion");

let paginaActual = 0;
let categoriaActual = "games";
let consultaActual = "";
let hayPaginaSiguiente = false;
let temporizadorSugerencias;
let limiteResultadosActual = 10;

function actualizarContadorFavoritos() {
  resumenFavoritos.textContent = String(obtenerFavoritos().length);
}

function sincronizarCategoriaActiva(categoria) {
  selectorCategoria.value = categoria;
  resumenCategoria.textContent = CONFIGURACION_CATEGORIAS[categoria].etiqueta;

  botonesFiltro.forEach((boton) => {
    boton.classList.toggle("filtros__boton--activo", boton.dataset.categoria === categoria);
  });
}

function actualizarMensajeResultados(mensaje) {
  mensajeResultados.textContent = mensaje;
}

function ocultarSugerencias() {
  listaSugerencias.innerHTML = "";
  listaSugerencias.classList.remove("sugerencias--visible");
  entradaBusqueda.setAttribute("aria-expanded", "false");
}

function pintarSugerencias(sugerencias) {
  if (!sugerencias.length) {
    ocultarSugerencias();
    return;
  }

  listaSugerencias.innerHTML = sugerencias.map((sugerencia) => `
    <li class="sugerencias__item">
      <button
        class="sugerencias__boton"
        type="button"
        data-sugerencia-nombre="${sugerencia.nombre}"
        data-sugerencia-categoria="${sugerencia.categoria}"
      >
        <span class="sugerencias__titulo">${sugerencia.nombre}</span>
        <span class="sugerencias__meta">${sugerencia.etiquetaCategoria}</span>
      </button>
    </li>
  `).join("");

  listaSugerencias.classList.add("sugerencias--visible");
  entradaBusqueda.setAttribute("aria-expanded", "true");
}

function calcularColumnasVisibles() {
  const anchoContenedor = listaResultados.clientWidth || listaResultados.parentElement.clientWidth || window.innerWidth;
  const tamanoFuenteRaiz = Number.parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
  const anchoMinimoTarjeta = 15.63 * tamanoFuenteRaiz;
  return Math.max(1, Math.floor(anchoContenedor / anchoMinimoTarjeta));
}

function calcularLimiteResultados() {
  return calcularColumnasVisibles() * 3;
}

function construirBotonPaginacion(texto, pagina, opciones = {}) {
  const { activa = false, deshabilitada = false } = opciones;

  return `
    <button
      class="paginacion__boton ${activa ? "paginacion__boton--activa" : ""}"
      type="button"
      data-pagina="${pagina}"
      ${deshabilitada ? "disabled" : ""}
    >${texto}</button>
  `;
}

function pintarPaginacion() {
  const botones = [];

  botones.push(construirBotonPaginacion("Anterior", paginaActual - 1, { deshabilitada: paginaActual === 0 }));

  const inicio = Math.max(0, paginaActual - 1);
  const fin = hayPaginaSiguiente ? paginaActual + 1 : paginaActual;

  for (let pagina = inicio; pagina <= fin; pagina += 1) {
    botones.push(construirBotonPaginacion(String(pagina + 1), pagina, { activa: pagina === paginaActual }));
  }

  if (hayPaginaSiguiente) {
    botones.push(construirBotonPaginacion("Siguiente", paginaActual + 1));
  }

  contenedorPaginacion.innerHTML = botones.join("");
  contenedorPaginacion.classList.toggle("paginacion--oculta", botones.length <= 1);
}

function pintarResultados(elementos) {
  if (!elementos.length) {
    listaResultados.innerHTML = `
      <li class="galeria__item">
        <p class="estado-vacio">
          No se han encontrado resultados para esta busqueda. Prueba con otro nombre o cambia la categoria.
        </p>
      </li>
    `;
    return;
  }

  listaResultados.innerHTML = elementos.map((elemento) => crearMarcadoTarjeta(elemento)).join("");
}

async function buscarSugerencias(consulta) {
  const texto = consulta.trim();

  if (texto.length < 2) {
    ocultarSugerencias();
    return;
  }

  try {
    const variantesConsulta = obtenerVariantesConsulta(texto);
    const solicitudes = CATEGORIAS_SUGERENCIAS.flatMap((categoria) =>
      variantesConsulta.map((variante) =>
        fetch(construirUrlCategoria(categoria, variante, 3, 0))
          .then((respuesta) => (respuesta.ok ? respuesta.json() : { data: [] }))
          .catch(() => ({ data: [] }))
          .then((respuesta) => ({ respuesta, categoria }))
      )
    );
    const respuestas = await Promise.all(solicitudes);

    const sugerencias = [];
    const nombresVistos = new Set();

    respuestas.forEach(({ respuesta, categoria }) => {

      (respuesta.data || []).forEach((elementoApi) => {
        const nombre = elementoApi.name || "";
        const clave = `${categoria}-${limpiarTextoBusqueda(nombre)}`;

        if (!nombre || nombresVistos.has(clave) || !coincideTextoBusqueda(nombre, texto)) {
          return;
        }

        sugerencias.push({
          nombre,
          categoria,
          etiquetaCategoria: CONFIGURACION_CATEGORIAS[categoria].etiqueta
        });
        nombresVistos.add(clave);
      });
    });

    const consultaNormalizada = limpiarTextoBusqueda(texto);
    sugerencias.sort((a, b) => {
      const aEmpieza = limpiarTextoBusqueda(a.nombre).startsWith(consultaNormalizada) ? 0 : 1;
      const bEmpieza = limpiarTextoBusqueda(b.nombre).startsWith(consultaNormalizada) ? 0 : 1;
      return aEmpieza - bEmpieza || a.nombre.localeCompare(b.nombre);
    });

    pintarSugerencias(sugerencias.slice(0, 8));
  } catch (error) {
    console.error(error);
    ocultarSugerencias();
  }
}

async function buscarCategoria(categoria, consulta, pagina = 0) {
  limiteResultadosActual = calcularLimiteResultados();
  categoriaActual = categoria;
  consultaActual = consulta;
  paginaActual = pagina;
  sincronizarCategoriaActiva(categoria);
  actualizarContadorFavoritos();
  resumenEstado.textContent = "Consultando API";
  actualizarMensajeResultados(`Buscando en ${CONFIGURACION_CATEGORIAS[categoria].etiqueta.toLowerCase()}...`);
  listaResultados.innerHTML = "";
  ocultarSugerencias();

  try {
    let elementos = [];

    if (consulta.trim()) {
      const variantesConsulta = obtenerVariantesConsulta(consulta).slice(0, 5);
      const tamanoMuestra = Math.max(limiteResultadosActual * 2, 24);
      const respuestasConsulta = await Promise.all(
        variantesConsulta.map((variante) =>
          fetch(construirUrlCategoria(categoria, variante, tamanoMuestra, 0))
        )
      );

      if (respuestasConsulta.some((respuesta) => !respuesta.ok)) {
        throw new Error("La API respondio con un estado no valido.");
      }

      const bloquesDatos = await Promise.all(respuestasConsulta.map((respuesta) => respuesta.json()));
      const mapaCoincidencias = new Map();

      bloquesDatos.forEach((bloqueDatos) => {
        (bloqueDatos.data || []).forEach((elementoApi) => {
          const elementoNormalizado = normalizarElemento(elementoApi, categoria);
          const textoComparacion = `${elementoNormalizado.name} ${elementoNormalizado.description}`;

          if (coincideTextoBusqueda(textoComparacion, consulta)) {
            mapaCoincidencias.set(elementoNormalizado.uid, elementoNormalizado);
          }
        });
      });

      const todosLosElementos = Array.from(mapaCoincidencias.values());
      const inicio = pagina * limiteResultadosActual;
      const fin = inicio + limiteResultadosActual;
      elementos = todosLosElementos.slice(inicio, fin);
      hayPaginaSiguiente = fin < todosLosElementos.length;
    } else {
      const [respuestaActual, respuestaSiguiente] = await Promise.all([
        fetch(construirUrlCategoria(categoria, consulta, limiteResultadosActual, pagina)),
        fetch(construirUrlCategoria(categoria, consulta, limiteResultadosActual, pagina + 1))
      ]);

      if (!respuestaActual.ok || !respuestaSiguiente.ok) {
        throw new Error(`La API respondio con estado ${respuestaActual.status}/${respuestaSiguiente.status}.`);
      }

      const datosActuales = await respuestaActual.json();
      const datosSiguientes = await respuestaSiguiente.json();
      elementos = Array.isArray(datosActuales.data)
        ? datosActuales.data.map((elementoApi) => normalizarElemento(elementoApi, categoria))
        : [];

      hayPaginaSiguiente = Array.isArray(datosSiguientes.data) && datosSiguientes.data.length > 0;
    }

    pintarResultados(elementos);
    if (elementos.length) {
      pintarPaginacion();
    } else {
      contenedorPaginacion.innerHTML = "";
      contenedorPaginacion.classList.add("paginacion--oculta");
    }

    if (consulta.trim()) {
      actualizarMensajeResultados(`Resultados para "${consulta}" en ${CONFIGURACION_CATEGORIAS[categoria].etiqueta.toLowerCase()}.`);
    } else {
      actualizarMensajeResultados(`Explorando ${CONFIGURACION_CATEGORIAS[categoria].etiqueta.toLowerCase()}.`);
    }

    resumenEstado.textContent = "Resultados cargados";
  } catch (error) {
    console.error(error);
    listaResultados.innerHTML = `
      <li class="galeria__item">
        <p class="estado-vacio">
          No se pudo conectar con la API de Zelda. Comprueba la conexion y vuelve a intentarlo.
        </p>
      </li>
    `;
    actualizarMensajeResultados("Ha ocurrido un problema al consultar la API.");
    resumenEstado.textContent = "Error de conexion";
    contenedorPaginacion.innerHTML = "";
    contenedorPaginacion.classList.add("paginacion--oculta");
  }
}

function construirElementoFavorito(tarjeta, botonFavorito) {
  const tituloTarjeta = tarjeta.querySelector(".tarjeta-zelda__titulo")?.textContent || "Elemento";
  const etiquetaCategoria = tarjeta.querySelector(".tarjeta-zelda__tipo")?.textContent || "";
  const descripcionTarjeta = tarjeta.querySelector(".tarjeta-zelda__descripcion")?.textContent || "";
  const enlaceTarjeta = tarjeta.querySelector(".tarjeta-zelda__enlace")?.getAttribute("href") || "#";
  const metadatos = Array.from(tarjeta.querySelectorAll(".tarjeta-zelda__metadato")).map((bloque) => {
    const clave = bloque.querySelector(".tarjeta-zelda__clave")?.textContent || "";
    const valor = bloque.querySelectorAll("span")[1]?.textContent || "";
    return [clave, valor];
  }).filter((entrada) => entrada[0] && entrada[1]);

  return {
    uid: botonFavorito.dataset.favorito,
    id: botonFavorito.dataset.favorito.split("-").slice(1).join("-"),
    category: tarjeta.dataset.categoria || selectorCategoria.value,
    categoryLabel: etiquetaCategoria,
    name: tituloTarjeta,
    description: descripcionTarjeta,
    detailUrl: enlaceTarjeta,
    meta: metadatos
  };
}

formularioBusqueda.addEventListener("submit", (evento) => {
  evento.preventDefault();
  buscarCategoria(selectorCategoria.value, entradaBusqueda.value, 0);
});

botonesFiltro.forEach((boton) => {
  boton.addEventListener("click", () => {
    buscarCategoria(boton.dataset.categoria, entradaBusqueda.value, 0);
  });
});

entradaBusqueda.addEventListener("input", () => {
  clearTimeout(temporizadorSugerencias);
  temporizadorSugerencias = window.setTimeout(() => {
    buscarSugerencias(entradaBusqueda.value);
  }, 250);
});

entradaBusqueda.addEventListener("focus", () => {
  if (entradaBusqueda.value.trim().length >= 2) {
    buscarSugerencias(entradaBusqueda.value);
  }
});

document.addEventListener("click", (evento) => {
  if (!evento.target.closest(".formulario-busqueda__campo")) {
    ocultarSugerencias();
  }
});

window.addEventListener("resize", () => {
  const nuevoLimite = calcularLimiteResultados();

  if (nuevoLimite !== limiteResultadosActual) {
    buscarCategoria(categoriaActual, consultaActual, 0);
  }
});

listaSugerencias.addEventListener("click", (evento) => {
  const botonSugerencia = evento.target.closest(".sugerencias__boton");

  if (!botonSugerencia) {
    return;
  }

  entradaBusqueda.value = botonSugerencia.dataset.sugerenciaNombre;
  selectorCategoria.value = botonSugerencia.dataset.sugerenciaCategoria;
  buscarCategoria(botonSugerencia.dataset.sugerenciaCategoria, botonSugerencia.dataset.sugerenciaNombre, 0);
});

contenedorPaginacion.addEventListener("click", (evento) => {
  const botonPagina = evento.target.closest(".paginacion__boton");

  if (!botonPagina || botonPagina.disabled) {
    return;
  }

  const paginaDestino = Number(botonPagina.dataset.pagina);

  if (paginaDestino < 0) {
    return;
  }

  buscarCategoria(categoriaActual, consultaActual, paginaDestino);
});

listaResultados.addEventListener("click", (evento) => {
  const botonFavorito = evento.target.closest("[data-favorito]");

  if (!botonFavorito) {
    return;
  }

  const tarjeta = botonFavorito.closest(".tarjeta-zelda");
  const elemento = construirElementoFavorito(tarjeta, botonFavorito);
  const guardado = alternarFavorito(elemento);

  botonFavorito.classList.toggle("tarjeta-zelda__favorito--activo", guardado);
  botonFavorito.innerHTML = guardado ? "&#9733;" : "&#9734;";
  botonFavorito.setAttribute("aria-label", guardado ? "Quitar de favoritos" : "Guardar en favoritos");
  botonFavorito.setAttribute("title", guardado ? "Quitar de favoritos" : "Guardar en favoritos");

  actualizarContadorFavoritos();
  resumenEstado.textContent = guardado ? "Favorito guardado" : "Favorito eliminado";
});

window.addEventListener("storage", actualizarContadorFavoritos);

actualizarContadorFavoritos();
buscarCategoria("games", "", 0);
