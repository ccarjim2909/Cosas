const API_ZELDA_BASE = "https://zelda.fanapis.com/api";
const CLAVE_FAVORITOS = "zelda-favorites";

const CONFIGURACION_CATEGORIAS = {
  games: { etiqueta: "Juegos", endpoint: "games" },
  characters: { etiqueta: "Personajes", endpoint: "characters" },
  monsters: { etiqueta: "Monstruos", endpoint: "monsters" },
  bosses: { etiqueta: "Jefes", endpoint: "bosses" },
  dungeons: { etiqueta: "Mazmorras", endpoint: "dungeons" },
  places: { etiqueta: "Lugares", endpoint: "places" },
  items: { etiqueta: "Objetos", endpoint: "items" },
  staff: { etiqueta: "Staff", endpoint: "staff" }
};

const CATEGORIAS_SUGERENCIAS = ["characters", "bosses", "monsters", "games", "items", "places"];

function obtenerFavoritos() {
  try {
    const favoritosGuardados = localStorage.getItem(CLAVE_FAVORITOS);
    return favoritosGuardados ? JSON.parse(favoritosGuardados) : [];
  } catch (error) {
    console.error("No se pudieron leer los favoritos.", error);
    return [];
  }
}

function guardarFavoritos(favoritos) {
  localStorage.setItem(CLAVE_FAVORITOS, JSON.stringify(favoritos));
}

function esFavorito(uid) {
  return obtenerFavoritos().some((elemento) => elemento.uid === uid);
}

function alternarFavorito(elemento) {
  const favoritos = obtenerFavoritos();
  const yaExiste = favoritos.some((favorito) => favorito.uid === elemento.uid);

  if (yaExiste) {
    guardarFavoritos(favoritos.filter((favorito) => favorito.uid !== elemento.uid));
    return false;
  }

  guardarFavoritos([elemento, ...favoritos]);
  return true;
}

function vaciarFavoritos() {
  localStorage.removeItem(CLAVE_FAVORITOS);
}

function construirUrlBusqueda(categoria, consulta, limite) {
  return construirUrlCategoria(categoria, consulta, limite, 0);
}

function construirUrlCategoria(categoria, consulta, limite, pagina = 0) {
  const parametros = new URLSearchParams({
    limit: String(limite),
    page: String(pagina)
  });

  if (consulta.trim()) {
    parametros.set("name", consulta.trim());
  }

  return `${API_ZELDA_BASE}/${CONFIGURACION_CATEGORIAS[categoria].endpoint}?${parametros.toString()}`;
}

function formatearCantidadRelacionada(valor) {
  if (!Array.isArray(valor) || valor.length === 0) {
    return "";
  }

  return `${valor.length} relacionados`;
}

function obtenerVariantesConsulta(consulta) {
  const texto = consulta.trim();

  if (!texto) {
    return [""];
  }

  const textoMinusculas = texto.toLowerCase();
  const palabrasEnlace = new Set(["de", "del", "la", "las", "el", "los", "y", "e", "of", "the", "and", "a", "an", "to"]);
  const palabras = textoMinusculas.split(/\s+/);
  const textoCapitalizado = palabras
    .map((palabra, indice) => {
      if (indice > 0 && palabrasEnlace.has(palabra)) {
        return palabra;
      }

      return palabra.charAt(0).toUpperCase() + palabra.slice(1);
    })
    .join(" ");
  const palabraClave = palabras.find((palabra) => palabra.length >= 3 && !palabrasEnlace.has(palabra)) || palabras[0];
  const palabraClaveCapitalizada = palabraClave.charAt(0).toUpperCase() + palabraClave.slice(1);

  return [...new Set([texto, textoMinusculas, textoCapitalizado, palabraClave, palabraClaveCapitalizada])];
}

function limpiarTextoBusqueda(texto) {
  return texto
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase();
}

function coincideTextoBusqueda(textoBase, consulta) {
  const baseNormalizada = limpiarTextoBusqueda(textoBase);
  const terminos = limpiarTextoBusqueda(consulta)
    .split(/\s+/)
    .filter(Boolean);

  return terminos.every((termino) => baseNormalizada.includes(termino));
}

function normalizarElemento(elementoApi, categoria) {
  const entradasExtra = [
    ["Desarrollador", elementoApi.developer],
    ["Publisher", elementoApi.publisher],
    ["Fecha", elementoApi.released_date],
    ["Genero", elementoApi.gender],
    ["Raza", elementoApi.race],
    ["Apariciones", formatearCantidadRelacionada(elementoApi.appearances)],
    ["Mazmorras", formatearCantidadRelacionada(elementoApi.dungeons)],
    ["Habitantes", formatearCantidadRelacionada(elementoApi.inhabitants)],
    ["Juegos", formatearCantidadRelacionada(elementoApi.games)],
    ["Trabajos", formatearCantidadRelacionada(elementoApi.worked_on)]
  ].filter((entrada) => entrada[1]);

  return {
    uid: `${categoria}-${elementoApi.id}`,
    id: elementoApi.id,
    category: categoria,
    categoryLabel: CONFIGURACION_CATEGORIAS[categoria].etiqueta,
    name: elementoApi.name || "Sin nombre",
    description: elementoApi.description || "Sin descripcion disponible en la API.",
    detailUrl: `${API_ZELDA_BASE}/${CONFIGURACION_CATEGORIAS[categoria].endpoint}/${elementoApi.id}`,
    meta: entradasExtra.slice(0, 4)
  };
}

function crearMarcadoTarjeta(elemento, incluirTextoGestion = false) {
  const marcadoMetadatos = elemento.meta.length
    ? elemento.meta.map((metadato) => `
        <li class="tarjeta-zelda__metadato">
          <span class="tarjeta-zelda__clave">${metadato[0]}</span>
          <span>${metadato[1]}</span>
        </li>
      `).join("")
    : `
      <li class="tarjeta-zelda__metadato">
        <span class="tarjeta-zelda__clave">Ficha</span>
        <span>Sin datos adicionales destacados.</span>
      </li>
    `;

  const simboloFavorito = esFavorito(elemento.uid) ? "&#9733;" : "&#9734;";
  const tituloFavorito = esFavorito(elemento.uid) ? "Quitar de favoritos" : "Guardar en favoritos";
  const notaTarjeta = incluirTextoGestion ? "Gestiona tu coleccion" : "Guarda lo que quieras revisar luego";

  return `
    <li class="galeria__item">
      <article class="tarjeta-zelda" data-uid="${elemento.uid}" data-categoria="${elemento.category}">
        <header class="tarjeta-zelda__cabecera">
          <p class="tarjeta-zelda__tipo">${elemento.categoryLabel}</p>
          <button
            class="tarjeta-zelda__favorito ${esFavorito(elemento.uid) ? "tarjeta-zelda__favorito--activo" : ""}"
            type="button"
            data-favorito="${elemento.uid}"
            aria-label="${tituloFavorito}"
            title="${tituloFavorito}"
          >${simboloFavorito}</button>
        </header>

        <section class="tarjeta-zelda__cuerpo">
          <h3 class="tarjeta-zelda__titulo">${elemento.name}</h3>
          <p class="tarjeta-zelda__descripcion">${elemento.description}</p>
        </section>

        <ul class="tarjeta-zelda__metadatos">${marcadoMetadatos}</ul>

        <footer class="tarjeta-zelda__pie">
          <a class="tarjeta-zelda__enlace" href="${elemento.detailUrl}" target="_blank" rel="noreferrer">Abrir ficha API</a>
          <span class="tarjeta-zelda__nota">${notaTarjeta}</span>
        </footer>
      </article>
    </li>
  `;
}
