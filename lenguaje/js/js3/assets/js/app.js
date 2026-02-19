const catalogo = [
    { id: 1, nombre: "Camiseta básica", precio: 15.99, categoria: "ropa" },
    { id: 2, nombre: "Pantalón vaquero", precio: 39.99, categoria: "ropa" },
    { id: 3, nombre: "Zapatillas running", precio: 89.99, categoria: "calzado" },
    { id: 4, nombre: "Sudadera con capucha", precio: 45.00, categoria: "ropa" },
    { id: 5, nombre: "Gorra deportiva", precio: 12.50, categoria: "accesorios" },
    { id: 6, nombre: "Mochila urbana", precio: 35.00, categoria: "accesorios" },
    { id: 7, nombre: "Calcetines pack 3", precio: 9.99, categoria: "ropa" },
    { id: 8, nombre: "Chanclas playa", precio: 14.99, categoria: "calzado" },
    { id: 9, nombre: "Tenis nike", precio: 44.99, categoria: "calzado" }
];


const footer = document.querySelector("footer");

const main = document.querySelector("main");




const seccion = document.createElement("section");
seccion.classList.add("seccion");



const enlace = document.createElement("a");
enlace.textContent = "Ver más";
enlace.href = "";
enlace.classList.add("suscripcion__enlace");

seccion.appendChild(enlace);



const aside = document.querySelector("aside");
const asideLista = document.querySelector(".aside__lista");


aside.after(seccion);



// parte nueva del aside
const categoriasUnicas = [];

for (const producto of catalogo) {
    if (!categoriasUnicas.includes(producto.categoria)) {
        categoriasUnicas.push(producto.categoria);
    }
}

// todas
const liTodas = document.createElement("li");
liTodas.textContent = "todas";
asideLista.appendChild(liTodas);

// las otras categorias con li
for (const i of categoriasUnicas) {
    const li = document.createElement("li");
    li.textContent = i;
    asideLista.appendChild(li);
}

// he metido ya todo el catalogo en una funcion para ir mostrando lo que quiera cuando haga el evento
function mostrarProductos(productos) {
    seccion.innerHTML = "";

    for (const producto of productos) {
        const articulo = document.createElement("article");
        articulo.classList.add("articulo__suscripcion");

        const h3 = document.createElement("h3");
        h3.textContent = producto.nombre;

        const precio = document.createElement("p");
        precio.textContent = `Precio: ${producto.precio} €`;

        const categoria = document.createElement("p");
        categoria.textContent = `Categoría: ${producto.categoria}`;

        articulo.append(h3, precio, categoria);
        seccion.appendChild(articulo);
    }

    seccion.appendChild(enlace);
}

// muestro el catalogo
mostrarProductos(catalogo);
