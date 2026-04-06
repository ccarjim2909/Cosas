const USUARIO = "jose";
const CONTRASEÑA = "jose";

const botonLogin = document.querySelector(".cabecera__boton-login");
const menuLogin = document.querySelector(".login");
const botonEnviarLogin = document.querySelector(".login__boton");
const mensajeLogin = document.querySelector(".login__mensaje");

botonLogin.addEventListener("click", () => {
    menuLogin.classList.toggle("login--oculto");
});

botonEnviarLogin.addEventListener("click", () => {
    const usuario = document.querySelector(".login__input--usuario").value;
    const contraseña = document.querySelector(".login__input--contraseña").value;

    if (usuario === USUARIO && contraseña === CONTRASEÑA) {
        mensajeLogin.style.color = "green";
        mensajeLogin.textContent = "Inicio de sesión correcto";

        setTimeout(() => {
            location.href = "logeado.html";
        }, 1000);
    } else {
        mensajeLogin.style.color = "red";
        mensajeLogin.textContent = "Usuario o contraseña incorrectos";

        document.querySelector(".login__input--usuario").value = "";
        document.querySelector(".login__input--contraseña").value = "";
    }
});