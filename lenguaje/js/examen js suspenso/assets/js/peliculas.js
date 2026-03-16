/*
*Pregunta 1

Los navegadores web son capaces de ejecutar codigo directamente en el lado del cliente,
sin necesidad de enviar la peticion a un servidor.

a) Indica que lenguaje de script de cliente es el estandar de facto en la web actual.
Explica brevemente en que se diferencia de un lenguaje de programacion de lado servidor como PHP o Python.
    - El lenguaje de script de cliente estandar es JavaScript.
    -   JavaScript se ejecuta en el navegador del usuario, permitiendo interactuar con la pagina o modificar el contenido sin comunicarse continuamente con el servidor.
        Lenguajes como PHP o Python se ejecutan en el servidor. Procesan la logica de la aplicacion y generan la respuesta (HTML, datos, etc.) que luego se envia al navegador del usuario.


b) Que ventaja aporta colocar la etiqueta que carga el script justo antes del cierre del <body>,
en lugar de en el <head>?
    - La etiqueta "defer" hace que el js cargue antes de la pagina web para que los eventos o los objetos que se
        hayan creado a traves de js se carguen antes de que el usario pueda ver la paagina para que no haya saltos
        raros de primero cargar el html y luego se cargue este script y se modifiquen cosas.
*/


/* Tarea 1 */

/* 1 */

// const fomulario = document.querySelector('#fomulario'); // MAL: el id correcto en el HTML es "formPelicula".
// const titulo = document.querySelector('#titulo'); // OK, pero lo dejamos con un nombre descriptivo abajo.
// const contenedorTarjetas = document.querySelector('#lista'); // OK, pero lo dejamos con un nombre descriptivo abajo.

// Referencias DOM requeridas por la tarea
const formularioPelicula = document.querySelector('#formPelicula');
const inputTitulo = document.querySelector('#titulo');
const contenedorTarjetas = document.querySelector('#lista');
const botonOscuro = document.querySelector('.btn-dark');


/* 2 */

// MAL: '#filtro' es un unico elemento <select>; para contar opciones hay que seleccionar sus <option>.
const opcionesFiltro = document.querySelectorAll('#filtro option');

console.log(opcionesFiltro.length);  /* Incluye "Todos" */


/* Tarea 2 */

const botonAnadir = document.querySelector('.btn-add');
const inputGenero = document.querySelector('#genero');
const inputNota = document.querySelector('#nota');

// Creamos un mensaje de error en el DOM (la tarea pide mostrarlo en la propia pagina).
const mensajeError = document.createElement('p');
formularioPelicula.appendChild(mensajeError);

/* MAL: no se hacia preventDefault, por eso el formulario se enviaba y recargaba la pagina. */
formularioPelicula.addEventListener("submit", function(event) {
    event.preventDefault();

    const titulo = inputTitulo.value.trim();
    const genero = inputGenero.value;
    const nota = inputNota.value;

    if (titulo === "") {
        // MAL: alert no cumple "mensaje en la propia pagina". Sustituimos por texto visible.
        mensajeError.textContent = "El titulo no puede estar vacio.";
        mensajeError.style.display = 'block';
        return;
    }

    mensajeError.style.display = 'none';

    const tarjeta = document.createElement("article");
    tarjeta.classList.add("pelicula");

    const btnEliminar = document.createElement("button");
    btnEliminar.classList.add("btn-eliminar");
    btnEliminar.type = "button";
    btnEliminar.textContent = "x";

    const h3 = document.createElement("h3");
    h3.textContent = titulo;

    const p = document.createElement("p");
    p.classList.add("genero");
    p.textContent = `${genero} - Nota: ${nota}/10`;

    const btnVista = document.createElement("button");
    btnVista.classList.add("btn-vista");
    btnVista.type = "button";
    btnVista.textContent = "Marcar como vista";

    tarjeta.appendChild(btnEliminar);
    tarjeta.appendChild(h3);
    tarjeta.appendChild(p);
    tarjeta.appendChild(btnVista);

    contenedorTarjetas.appendChild(tarjeta);

    // Tarea 3: eliminar tarjeta (boton activo desde que aparece).
    btnEliminar.addEventListener('click', function () {
        tarjeta.remove();
    });

    // Tarea 4B: marcar como vista (toggle de clase y texto).
    btnVista.addEventListener('click', function () {
        const esVista = tarjeta.classList.toggle('vista');
        btnVista.textContent = esVista ? 'Marcar como no vista' : 'Marcar como vista';
    });

    // Limpiar campos para la siguiente entrada.
    formularioPelicula.reset();
});


/* Tarea 3 */





/* Tarea 4 */

/* A */

/* MAL: se intentaba usar clases "body" y "body.dark". En CSS el modo oscuro se activa con "body.dark". */
const body = document.querySelector('body');

botonOscuro.addEventListener('click', function () {

    body.classList.toggle('dark');

    const modoOscuroActivo = body.classList.contains('dark');

    if (modoOscuroActivo) {
        botonOscuro.textContent = 'Modo claro';
    } else {
        botonOscuro.textContent = 'Modo oscuro';
    }

});

// Estado inicial del texto segun el modo actual.
actualizarTextoBotonModo();


/* B */

// MAL: seleccionar un unico boton no cubre tarjetas nuevas.
// MAL: se aplicaba clase "pelicula.vista" al boton, pero el CSS espera esa clase en el <article>.
// La funcionalidad correcta se implementa al crear cada tarjeta (ver arriba).
