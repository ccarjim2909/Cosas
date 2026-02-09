const catalogo = [
    { id: 1, nombre: "Camiseta básica", precio: 15.99, categoria: "ropa" },
    { id: 2, nombre: "Pantalón vaquero", precio: 39.99, categoria: "ropa" },
    { id: 3, nombre: "Zapatillas running", precio: 89.99, categoria: "calzado" },
    { id: 4, nombre: "Sudadera con capucha", precio: 45.00, categoria: "ropa" },
    { id: 5, nombre: "Gorra deportiva", precio: 12.50, categoria: "accesorios" },
    { id: 6, nombre: "Mochila urbana", precio: 35.00, categoria: "accesorios" },
    { id: 7, nombre: "Calcetines pack 3", precio: 9.99, categoria: "ropa" },
    { id: 8, nombre: "Chanclas playa", precio: 14.99, categoria: "calzado" }
];


const footer = document.querySelector("footer");


const seccion = document.createElement("section");
seccion.classList.add("seccion");


for (const producto of catalogo) {


    const articulo = document.createElement("article");
    articulo.classList.add("articulo__subscripcion");


    const h2 = document.createElement("h3");
    h2.textContent = producto.nombre;


    const precio = document.createElement("p");
    precio.textContent = `Precio: ${producto.precio} €`;


    const categoria = document.createElement("p");
    categoria.textContent = `Categoría: ${producto.categoria}`;


    articulo.appendChild(h2);
    articulo.appendChild(precio);
    articulo.appendChild(categoria);


    seccion.appendChild(articulo);
}

const enlace = document.createElement("a");
enlace.textContent = "Ver más";
enlace.href = "";
enlace.classList.add("subscripcion__enlace");

seccion.appendChild(enlace);


footer.before(seccion);
