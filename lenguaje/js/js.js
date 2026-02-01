"use strict";

// ============================================
// DATOS INICIALES DEL INVENTARIO
// ============================================

const inventario = [
    {
        id: 1,
        nombre: "Laptop HP Pavilion",
        categoria: "portatiles",
        precio: 699.99,
        stock: 15,
        caracteristicas: { procesador: "Intel i5", ram: "8GB", almacenamiento: "512GB SSD" },
        activo: true
    },
    {
        id: 2,
        nombre: "Monitor Samsung 27\"",
        categoria: "monitores",
        precio: 249.99,
        stock: 23,
        caracteristicas: { resolucion: "2560x1440", panel: "IPS", tasaRefresco: "75Hz" },
        activo: true
    },
    {
        id: 3,
        nombre: "Teclado Mecánico Logitech",
        categoria: "perifericos",
        precio: 89.99,
        stock: 45,
        caracteristicas: { tipo: "mecánico", switches: "Cherry MX Red", retroiluminacion: true },
        activo: true
    },
    {
        id: 4,
        nombre: "Ratón Inalámbrico Logitech",
        categoria: "perifericos",
        precio: 34.99,
        stock: 0,
        caracteristicas: { tipo: "inalámbrico", dpi: 4000, botones: 6 },
        activo: false
    },
    {
        id: 5,
        nombre: "Laptop Dell XPS 15",
        categoria: "portatiles",
        precio: 1299.99,
        stock: 8,
        caracteristicas: { procesador: "Intel i7", ram: "16GB", almacenamiento: "1TB SSD" },
        activo: true
    },
    {
        id: 6,
        nombre: "Webcam HD Logitech",
        categoria: "perifericos",
        precio: 59.99,
        stock: 32,
        caracteristicas: { resolucion: "1080p", fps: 30, microfono: true },
        activo: true
    },
    {
        id: 7,
        nombre: "Monitor LG UltraWide 34\"",
        categoria: "monitores",
        precio: 449.99,
        stock: 5,
        caracteristicas: { resolucion: "3440x1440", panel: "IPS", tasaRefresco: "144Hz" },
        activo: true
    },
    {
        id: 8,
        nombre: "Auriculares Gaming HyperX",
        categoria: "audio",
        precio: 79.99,
        stock: 28,
        caracteristicas: { tipo: "over-ear", microfono: true, conexion: "USB/Jack 3.5mm" },
        activo: true
    }
];

// ============================================
// PASO 1: Buscar producto por ID
// ============================================

let idBuscado = 3;
let productoId = null;

for (const producto of inventario) {
    if (producto.id === idBuscado) {
        productoId = producto;
    }
}

console.log("Producto ID 3:", productoId);

// ============================================
// PASO 2: Buscar productos por nombre
// ============================================

let termino = "logitech";
let productosNombre = [];

for (const producto of inventario) {
    if (producto.nombre.toLowerCase().includes(termino.toLowerCase())) {
        productosNombre.push(producto);
    }
}

console.log("Productos con 'logitech':", productosNombre);

// ============================================
// PASO 3: Filtrar por categoría
// ============================================

let categoria = "monitores";
let productosCategoria = [];

for (const producto of inventario) {
    if (producto.categoria === categoria) {
        productosCategoria.push(producto);
    }
}

console.log("Monitores:", productosCategoria);

// ============================================
// PASO 4: Filtrar por rango de precio
// ============================================

let min = 50;
let max = 100;
let productosPrecio = [];

for (const producto of inventario) {
    if (producto.precio >= min && producto.precio <= max) {
        productosPrecio.push(producto);
    }
}

console.log("Entre 50 y 100€:", productosPrecio);

// ============================================
// PASO 5: Productos con stock bajo
// ============================================

let umbral = 10;
let stockBajo = [];

for (const producto of inventario) {
    if (producto.stock < umbral) {
        stockBajo.push(producto);
    }
}

console.log("Stock bajo:", stockBajo);

// ============================================
// PASO 6: Productos activos
// ============================================

let activos = [];

for (const producto of inventario) {
    if (producto.activo) {
        activos.push(producto);
    }
}

console.log("Productos activos:", activos);

// ============================================
// PASO 7: Lista simplificada
// ============================================

let listaSimplificada = [];

for (const producto of inventario) {
    listaSimplificada.push({
        id: producto.id,
        nombre: producto.nombre,
        precio: producto.precio,
        disponible: producto.stock > 0
    });
}

console.log("Lista simplificada:", listaSimplificada);

// ============================================
// PASO 8: Aplicar descuento a periféricos
// ============================================

let porcentaje = 15;
let inventarioDescuento = [];

for (const producto of inventario) {
    let copia = { ...producto };

    if (producto.categoria === "perifericos") {
        copia.precio = +(producto.precio * (1 - porcentaje / 100)).toFixed(2);
    }

    inventarioDescuento.push(copia);
}

console.log("Periféricos con descuento:", inventarioDescuento);

// ============================================
// PASO 9: Nombres formateados
// ============================================

let nombres = [];

for (const producto of inventario) {
    nombres.push(`${producto.nombre} - ${producto.precio}€`);
}

console.log("Nombres formateados:", nombres);

// ============================================
// PASO 10: Valor total del inventario
// ============================================

let valorTotal = 0;

for (const producto of inventario) {
    valorTotal += producto.precio * producto.stock;
}

console.log("Valor total:", valorTotal.toFixed(2));

// ============================================
// PASO 11: Precio promedio
// ============================================

let sumaPrecios = 0;

for (const producto of inventario) {
    sumaPrecios += producto.precio;
}

let promedio = sumaPrecios / inventario.length;
console.log("Precio promedio:", promedio.toFixed(2));

// ============================================
// PASO 12: Contar productos por categoría
// ============================================

let conteo = {};

for (const producto of inventario) {
    if (!conteo[producto.categoria]) {
        conteo[producto.categoria] = 0;
    }
    conteo[producto.categoria]++;
}

console.log("Conteo categorías:", conteo);

// ============================================
// PASO 13: Resumen del inventario
// ============================================

let masCaro = inventario[0];
let masBarato = inventario[0];
let stockTotal = 0;

for (const producto of inventario) {
    if (producto.precio > masCaro.precio) masCaro = producto;
    if (producto.precio < masBarato.precio) masBarato = producto;
    stockTotal += producto.stock;
}

let resumen = {
    totalProductos: inventario.length,
    productosActivos: activos.length,
    valorTotal: valorTotal.toFixed(2),
    productoMasCaro: masCaro,
    productoMasBarato: masBarato,
    stockTotal: stockTotal
};

console.log("Resumen:", resumen);

// ============================================
// PASO 14: Actualizar stock
// ============================================

let actualizado = false;

for (const producto of inventario) {
    if (producto.id === 3) {
        producto.stock = 40;
        actualizado = true;
    }
}

console.log("Stock actualizado:", actualizado);

// ============================================
// PASO 15: Registrar venta
// ============================================

let resultadoVenta = {};

for (const producto of inventario) {
    if (producto.id === 4) {
        if (producto.stock >= 2) {
            producto.stock -= 2;
            resultadoVenta = { exito: true, mensaje: "Venta registrada", nuevoStock: producto.stock };
        } else {
            resultadoVenta = { exito: false, mensaje: `Stock insuficiente (disponible: ${producto.stock})`, nuevoStock: producto.stock };
        }
    }
}

console.log("Resultado venta:", resultadoVenta);

// ============================================
// PASO 16: Añadir nuevo producto
// ============================================

let maxId = 0;

for (const producto of inventario) {
    if (producto.id > maxId) maxId = producto.id;
}

let nuevoProducto = {
    id: maxId + 1,
    nombre: "Altavoces Bluetooth",
    categoria: "audio",
    precio: 99.99,
    stock: 20,
    caracteristicas: { potencia: "20W", conexion: "Bluetooth" },
    activo: true
};

inventario.push(nuevoProducto);
console.log("Producto añadido:", nuevoProducto);

// ============================================
// PASO 17: Exportar a JSON
// ============================================

let json = JSON.stringify(inventario, null, 2);
console.log("Inventario JSON:\n", json);

// ============================================
// PASO 18: Generar informe
// ============================================

let informe = "";

for (const producto of inventario) {
    informe +=
`ID: ${producto.id}
Producto: ${producto.nombre}
Categoría: ${producto.categoria}
Precio: ${producto.precio}€
Stock: ${producto.stock}
Activo: ${producto.activo ? "Sí" : "No"}
--------------------------
`;
}

console.log("Informe:\n", informe);
