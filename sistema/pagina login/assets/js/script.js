const USUARIO = "jose";
const CONTRASENA = "jose";

const botonesLogin = document.querySelectorAll(".cabecera__boton-login");
const menuLogin = document.querySelector(".login");
const panelLogin = document.querySelector(".login__panel"); 
const botonEnviarLogin = document.querySelector(".login__boton");
const mensajeLogin = document.querySelector(".login__mensaje");
const inputUsuario = document.querySelector(".login__input--usuario");
const inputContrasena = document.querySelector(".login__input--contrasena");


if (botonesLogin.length > 0 && menuLogin) {
    botonesLogin.forEach((boton) => {
        boton.addEventListener("click", () => {
            menuLogin.classList.toggle("login--oculto");
        });
    });
}


if (menuLogin && panelLogin) {
    menuLogin.addEventListener("click", () => {
        menuLogin.classList.add("login--oculto");
    });


    panelLogin.addEventListener("click", (e) => {
        e.stopPropagation();
    });
}


if (botonEnviarLogin && mensajeLogin && inputUsuario && inputContrasena) {
    botonEnviarLogin.addEventListener("click", () => {
        const usuario = inputUsuario.value;
        const contrasena = inputContrasena.value;

        if (usuario === USUARIO && contrasena === CONTRASENA) {
            mensajeLogin.style.color = "#86efac";
            mensajeLogin.textContent = "Inicio de sesion correcto";

            setTimeout(() => {
                location.href = "logeado.html";
            }, 1000);
        } else {
            mensajeLogin.style.color = "#fda4af";
            mensajeLogin.textContent = "Usuario o contrasena incorrectos";

            inputUsuario.value = "";
            inputContrasena.value = "";
        }
    });
}
