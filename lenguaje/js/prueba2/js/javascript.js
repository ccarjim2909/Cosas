"use strict";

// ============================================
// DATOS (catálogo, carrito, configuración)
// ============================================

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

const carrito = [
    { productoId: 1, cantidad: 3 },   // 3 camisetas
    { productoId: 3, cantidad: 1 },   // 1 zapatillas
    { productoId: 5, cantidad: 2 },   // 2 gorras
    { productoId: 7, cantidad: 4 }    // 4 packs calcetines
];

const codigoPromocional = "DESCUENTO20";
const esClientePremium = true;

// ============================================
// CONSTANTES DE CONFIGURACIÓN
// ============================================

const IVA = 0.21;
const UMBRAL_DESCUENTO_10 = 100;
const UMBRAL_DESCUENTO_15 = 200;
const UMBRAL_ENVIO_GRATIS = 100;
const UMBRAL_ENVIO_REDUCIDO = 50;
// ... añade más constantes según necesites

// ============================================
// PASO 1: Construir el carrito detallado
// ============================================

// TODO: Recorre el carrito y para cada item:
// - Busca el producto en el catálogo por su ID
// - Crea un objeto con: id, nombre, precioUnitario, cantidad, subtotal

// Pista: Puedes usar un bucle for...of o el método find()

let carritoDetallado = [];

for (const producto of carrito){
    for (const catalogoProducto of catalogo){
        if (producto.productoId === catalogoProducto.id){
            let productoFinal = {
                id:catalogoProducto.id,
                nombre:catalogoProducto.nombre,
                precioUnitario:catalogoProducto.precio,
                cantidad: producto.cantidad,
                subtotal: (catalogoProducto.precio * producto.cantidad)
            };
            console.log("productoFinal", productoFinal);
            carritoDetallado.push(productoFinal);
        }
    }
}

console.log(carritoDetallado);



// ============================================
// PASO 2: Calcular el subtotal del carrito
// ============================================

// TODO: Suma todos los subtotales de los productos
let sumaTotal = 0;

for (const producto of carritoDetallado){
    sumaTotal = sumaTotal + producto.subtotal;
}

console.log(sumaTotal);


// ============================================
// PASO 3: Calcular descuentos
// ============================================

// TODO: Determina qué descuento por volumen aplica (10% o 15%)

let descuento = 0;

if (sumaTotal > UMBRAL_DESCUENTO_15){
    descuento = 15;
}else if (sumaTotal > UMBRAL_DESCUENTO_10){
    descuento = 10;
}else {
    descuento = 0;
}

console.log(descuento);


// TODO: Comprueba si el código promocional es válido

const codigoPromocionalCliente = "DESCUENTO20";
let porcentajePromocional = 0
if (codigoPromocionalCliente === codigoPromocional){
    porcentajePromocional = 20
}


// TODO: Calcula el total después de descuentos

let descuentoTotal = descuento + porcentajePromocional;

console.log(descuentoTotal);

console.log(sumaTotal);

descuentoTotal = sumaTotal * descuentoTotal / 100;

sumaTotal = sumaTotal - descuentoTotal;

console.log(sumaTotal);


// ============================================
// PASO 4: Calcular IVA
// ============================================

// TODO: Calcula el IVA sobre el precio con descuentos

sumaTotal = (sumaTotal * IVA) + sumaTotal;


console.log(sumaTotal);

/*
// ============================================
// PASO 5: Calcular gastos de envío
// ============================================

// TODO: Determina los gastos de envío según el total y si es premium

if (esClientePremium){
    if (sumaTotal > 100){


    }else {


    }
}
*/

