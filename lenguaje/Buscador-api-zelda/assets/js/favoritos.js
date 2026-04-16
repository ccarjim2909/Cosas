const listaFavoritos = document.querySelector(".js-favoritos-lista");
const mensajeFavoritos = document.querySelector(".js-favoritos-mensaje");
const totalFavoritos = document.querySelector(".js-favoritos-total");
const botonVaciarFavoritos = document.querySelector(".js-favoritos-vaciar");

/* ============================= */

function actualizarCabeceraFavoritos(total) {
  totalFavoritos.textContent = String(total);
}

/* ============================= */

function pintarFavoritos() {

  const favoritos = obtenerFavoritos();

  actualizarCabeceraFavoritos(favoritos.length);

  if (!favoritos.length) {
    mensajeFavoritos.textContent = "Aún no tienes favoritos guardados.";

    listaFavoritos.innerHTML = `
      <li class="galeria__item">
        <p class="estado-vacio">
          Tu galería está vacía. Guarda elementos desde el buscador.
        </p>
      </li>
    `;
    return;
  }

  mensajeFavoritos.textContent = `Tienes ${favoritos.length} elementos guardados.`;

  listaFavoritos.innerHTML = favoritos
    .map(elemento => crearMarcadoTarjeta(elemento, true))
    .join("");
}

/* ============================= */

listaFavoritos.addEventListener("click", (evento) => {

  const botonFavorito = evento.target.closest("[data-favorito]");

  if (!botonFavorito) return;

  const nuevosFavoritos = obtenerFavoritos()
    .filter(el => el.uid !== botonFavorito.dataset.favorito);

  guardarFavoritos(nuevosFavoritos);

  pintarFavoritos();
});

/* ============================= */

botonVaciarFavoritos.addEventListener("click", () => {
  vaciarFavoritos();
  pintarFavoritos();
});

/* ============================= */

window.addEventListener("storage", pintarFavoritos);

/* ============================= */

pintarFavoritos();