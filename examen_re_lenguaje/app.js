const ciudades = [
    { nombre: 'Madrid',    temp: 38, humedad: 22, estado: 'soleado.'  },
    { nombre: 'A Coruña',  temp: 16, humedad: 85, estado: 'nublado.'  },
    { nombre: 'Sevilla',   temp: 42, humedad: 18, estado: 'soleado.'  },
    { nombre: 'Bilbao',    temp: 19, humedad: 78, estado: 'lluvioso.' },
    { nombre: 'Valencia',  temp: 31, humedad: 55, estado: 'nublado.'  },
];


/* 1 */
const listaCiudades = document.querySelector("#lista-ciudades");


for (let ciudad in ciudades){
    let x = document.createElement("li")
    x.innerHTML = `${ciudades[ciudad].nombre} - ${ciudades[ciudad].temp}°C`; 
    
    // Esto genera exactamente: data-nombre="Madrid"
    x.dataset.nombre = ciudades[ciudad].nombre; 
    
    listaCiudades.appendChild(x);
}

let estadoCarga = document.querySelector("#estado-carga");

estadoCarga.innerHTML = ciudades.length + " Ciudades cargadas";





/* 2 */

let detalle  = document.querySelector("#detalle");



listaCiudades.addEventListener("click", function(e) {
    if (e.target.tagName === "LI") {
        const nombreCiudad = e.target.dataset.nombre;

        for (let ciudad in ciudades) {
            if (ciudades[ciudad].nombre === nombreCiudad) {
                detalle.innerHTML = `
                    <h3>${ciudades[ciudad].nombre}</h3>
                    <p>Temperatura: ${ciudades[ciudad].temp}°C</p>
                    <p>Humedad: ${ciudades[ciudad].humedad}%</p>
                    <p>Estado: ${ciudades[ciudad].estado}</p>
                `;
            }
        }
    }
});





/* 3 */

const buscador  = document.querySelector("#buscador");


buscador.addEventListener("input", (e) => {
    const textoUsuario = e.target.value.toLowerCase();
    const items = listaCiudades.children;

    for (let i = 0; i < items.length; i++) {
        let li = items[i];

        let nombreCiudad = li.dataset.nombre.toLowerCase();

        if (nombreCiudad.includes(textoUsuario)) {
            li.style.display = ""; 
        } else {
            li.style.display = "none";
        }
    }
});





/* 4 */

const btn = document.querySelector("#btn-alerta");


btn.addEventListener("click", function() {

    const retraso = new Promise((resolve) => {
        setTimeout(resolve, 1500);
    });

    retraso.then(() => {
        let ciudadesExtremas = [];

        for (let i in ciudades) {
            if (ciudades[i].temp > 350) {
                ciudadesExtremas.push(ciudades[i].nombre);
            }
        }

        if (ciudadesExtremas.length > 0) {
            detalle.innerHTML = `
                <p><strong>Aviso: temperatura extrema</strong></p>
                <ul>${ciudadesExtremas.map(c => `<li>${c}</li>`).join('')}</ul>
            `;
        } else {
            detalle.innerHTML = "<p>Temperaturas dentro del rango normal</p>";
        }
    });
});




/* ----- Pregunta 1 -------  */

// te muestra primero A, luego como hay un temporizador hasta que la cuenta no llegue a 0 no escribiria B osea que
// escribiria C y luego cuando acabe la cuenta escribiria B
// quedarias asi:
// A
// C
// B


/* ----- Pregunta 2 -------  */

// el contador solo muestra por consola cuando el bucle for ha terminado y no en cada interaccion

/*
for (var i = 0; i < 3; i++) {
    console.log("1")
    setTimeout(() => console.log(i), 1000);
    console.log("2")
}
*/
