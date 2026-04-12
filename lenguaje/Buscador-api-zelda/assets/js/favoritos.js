const listaFavoritos = document.querySelector(".js-favoritos-lista");
const mensajeFavoritos = document.querySelector(".js-favoritos-mensaje");
const totalFavoritos = document.querySelector(".js-favoritos-total");
const estadoFavoritos = document.querySelector(".js-favoritos-estado");
const botonVaciarFavoritos = document.querySelector(".js-favoritos-vaciar");

function actualizarCabeceraFavoritos(total) {
  totalFavoritos.textContent = String(total);
  estadoFavoritos.textContent = total ? "Coleccion actualizada" : "Sin favoritos";
}

function pintarFavoritos() {
  const favoritos = obtenerFavoritos();
  actualizarCabeceraFavoritos(favoritos.length);

  if (!favoritos.length) {
    mensajeFavoritos.textContent = "Aun no has marcado favoritos. Ve al buscador y guarda algunos con la estrella.";
    listaFavoritos.innerHTML = `
      <li class="galeria__item">
        <p class="estado-vacio">
          Tu galeria esta vacia por ahora. Cuando marques favoritos en el buscador, apareceran aqui.
        </p>
      </li>
    `;
    return;
  }

  mensajeFavoritos.textContent = `Tienes ${favoritos.length} elementos guardados en tu coleccion.`;
  listaFavoritos.innerHTML = favoritos.map((elemento) => crearMarcadoTarjeta(elemento, true)).join("");
}

listaFavoritos.addEventListener("click", (evento) => {
  const botonFavorito = evento.target.closest("[data-favorito]");

  if (!botonFavorito) {
    return;
  }

  const favoritosActualizados = obtenerFavoritos().filter((elemento) => elemento.uid !== botonFavorito.dataset.favorito);
  guardarFavoritos(favoritosActualizados);
  pintarFavoritos();
});

botonVaciarFavoritos.addEventListener("click", () => {
  vaciarFavoritos();
  pintarFavoritos();
});

window.addEventListener("storage", pintarFavoritos);

pintarFavoritos();
