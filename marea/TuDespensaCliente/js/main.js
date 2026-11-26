function guardarCookie(nombre, valor, diasCaducidad) {
  const fecha = new Date();
  fecha.setTime(fecha.getTime() + diasCaducidad * 24 * 60 * 60 * 1000);
  const expiracion = "expires=" + fecha.toUTCString();
  document.cookie = nombre + "=" + encodeURIComponent(valor) + ";" + expiracion + ";path=/;SameSite=Lax";
}

function leerCookie(nombre) {
  const prefijo = nombre + "=";
  const partes = document.cookie.split(";");
  let resultado = "";
  let i = 0;

  while (i < partes.length && resultado === "") {
    const c = partes[i].trim();
    if (c.indexOf(prefijo) === 0) {
      resultado = decodeURIComponent(c.substring(prefijo.length));
    }
    i = i + 1;
  }

  return resultado;
}

function mostrarEstadoCampo(campo, mensajeError) {
  const idError = campo.getAttribute("aria-describedby");
  const contenedorError = idError ? document.getElementById(idError.split(" ")[0]) : null;

  if (mensajeError !== null) {
    campo.setAttribute("aria-invalid", "true");
    if (contenedorError) {
      contenedorError.textContent = mensajeError;
    }
  } else {
    campo.setAttribute("aria-invalid", "false");
    if (contenedorError) {
      contenedorError.textContent = "";
    }
  }
}

function limpiarEstadoFormulario(formulario) {
  const campos = formulario.querySelectorAll("input, select, textarea");
  for (let i = 0; i < campos.length; i = i + 1) {
    campos[i].dataset.tocado = "false";
    campos[i].removeAttribute("aria-invalid");
    const idError = campos[i].getAttribute("aria-describedby");
    if (idError) {
      const span = document.getElementById(idError.split(" ")[0]);
      if (span) {
        span.textContent = "";
      }
    }
  }
}

function pedirConfirmacion(mensaje, callbackAceptar) {
  const dialogo = document.getElementById("dialogo-confirmacion");

  if (!dialogo || typeof dialogo.showModal !== "function") {
    if (window.confirm(mensaje)) {
      callbackAceptar();
    }
    return;
  }

  const texto = document.getElementById("dialogo-confirmacion-texto");
  const btnCancelar = document.getElementById("btn-dialogo-cancelar");
  const btnAceptar = document.getElementById("btn-dialogo-aceptar");

  texto.textContent = mensaje;

  btnCancelar.onclick = () => {
    dialogo.close();
  };

  btnAceptar.onclick = () => {
    dialogo.close();
    callbackAceptar();
  };

  dialogo.showModal();
}

function inicializarRegistro() {
  const form = document.getElementById("formulario-registro");
  if (!form) {
    return;
  }

  const inputId = document.getElementById("registro-id");
  const inputUsuario = document.getElementById("registro-usuario");
  const inputEmail = document.getElementById("registro-email");
  const inputFecha = document.getElementById("registro-fecha");
  const inputPassword = document.getElementById("registro-password");
  const inputConfirmar = document.getElementById("registro-confirmar");
  const inputCondiciones = document.getElementById("registro-condiciones");

  const btnSubmit = document.getElementById("btn-submit-registro");
  const btnCancelarEdicion = document.getElementById("btn-cancelar-edicion");
  const listaUsuarios = document.getElementById("lista-usuarios");
  const contadorUsuarios = document.getElementById("contador-usuarios");

  const camposValidables = [
    inputUsuario,
    inputEmail,
    inputFecha,
    inputPassword,
    inputConfirmar,
    inputCondiciones
  ];

  function validarUnCampo(campo) {
    let error = null;

    if (campo === inputUsuario) {
      error = validarUsuario(campo.value, campo);
    } else if (campo === inputEmail) {
      error = validarEmail(campo.value, campo);
    } else if (campo === inputFecha) {
      error = validarFechaNacimiento(campo.value, campo);
    } else if (campo === inputPassword) {
      error = validarContrasena(campo.value, campo);
      if (inputConfirmar.dataset.tocado === "true") {
        mostrarEstadoCampo(
          inputConfirmar,
          validarRepetirContrasena(inputConfirmar.value, inputPassword.value, inputConfirmar)
        );
      }
    } else if (campo === inputConfirmar) {
      error = validarRepetirContrasena(campo.value, inputPassword.value, campo);
    } else if (campo === inputCondiciones) {
      error = validarAceptacion(campo.checked, campo);
    }

    mostrarEstadoCampo(campo, error);
    return error === null;
  }

  for (let i = 0; i < camposValidables.length; i = i + 1) {
    const campo = camposValidables[i];

    campo.addEventListener("blur", () => {
      campo.dataset.tocado = "true";
      validarUnCampo(campo);
    });

    const eventoTiempoReal = campo.type === "checkbox" || campo.type === "date" ? "change" : "input";
    campo.addEventListener(eventoTiempoReal, () => {
      if (campo.dataset.tocado === "true") {
        validarUnCampo(campo);
      }
    });
  }

  function salirModoEdicion() {
    form.reset();
    inputId.value = "";
    btnSubmit.textContent = "Crear cuenta";
    btnCancelarEdicion.hidden = true;
    limpiarEstadoFormulario(form);
  }

  btnCancelarEdicion.addEventListener("click", () => {
    salirModoEdicion();
  });

  form.addEventListener("submit", (evento) => {
    evento.preventDefault();
    let primerInvalido = null;

    for (let i = 0; i < camposValidables.length; i = i + 1) {
      const campo = camposValidables[i];
      campo.dataset.tocado = "true";
      const esValido = validarUnCampo(campo);

      if (!esValido && primerInvalido === null) {
        primerInvalido = campo;
      }
    }

    if (primerInvalido !== null) {
      primerInvalido.focus();
      return;
    }

    const fechaISO = new Date(inputFecha.value + "T00:00:00").toISOString().split("T")[0];

    const datosUsuario = {
      usuario: inputUsuario.value.trim(),
      email: inputEmail.value.trim(),
      fechaNacimiento: fechaISO,
      condiciones: Boolean(inputCondiciones.checked)
    };

    if (inputId.value !== "") {
      actualizar("usuarios", inputId.value, datosUsuario);
    } else {
      crear("usuarios", datosUsuario);
    }

    salirModoEdicion();
    renderizarUsuarios(listaUsuarios, obtenerTodos("usuarios"), contadorUsuarios);
  });

  listaUsuarios.addEventListener("click", (evento) => {
    const boton = evento.target.closest("button[data-accion]");
    if (!boton) {
      return;
    }

    const accion = boton.dataset.accion;
    const id = boton.dataset.id;

    if (accion === "editar") {
      const usuario = obtenerPorId("usuarios", id);
      if (usuario !== null) {
        limpiarEstadoFormulario(form);
        inputId.value = usuario.id;
        inputUsuario.value = usuario.usuario;
        inputEmail.value = usuario.email;
        inputFecha.value = usuario.fechaNacimiento;
        inputCondiciones.checked = Boolean(usuario.condiciones);
        inputPassword.value = "";
        inputConfirmar.value = "";

        btnSubmit.textContent = "Guardar cambios";
        btnCancelarEdicion.hidden = false;
        form.scrollIntoView({ behavior: "smooth" });
        inputUsuario.focus();
      }
    } else if (accion === "borrar") {
      pedirConfirmacion("¿Seguro que quieres eliminar este usuario?", () => {
        borrar("usuarios", id);
        if (String(inputId.value) === String(id)) {
          salirModoEdicion();
        }
        renderizarUsuarios(listaUsuarios, obtenerTodos("usuarios"), contadorUsuarios);
      });
    }
  });

  renderizarUsuarios(listaUsuarios, obtenerTodos("usuarios"), contadorUsuarios);
}

function inicializarContacto() {
  const form = document.getElementById("formulario-contacto");
  if (!form) {
    return;
  }

  const inputNombre = document.getElementById("contacto-nombre");
  const inputEmail = document.getElementById("contacto-email");
  const checkLlamar = document.getElementById("contacto-llamar");
  const inputTelefono = document.getElementById("contacto-telefono");
  const etiquetaTelefono = document.getElementById("etiqueta-telefono-opcional");
  const selectMotivo = document.getElementById("contacto-motivo");
  const areaMensaje = document.getElementById("contacto-mensaje");
  const contadorCaracteres = document.getElementById("contador-caracteres-mensaje");

  const listaMensajes = document.getElementById("lista-mensajes");
  const contadorMensajes = document.getElementById("contador-mensajes");

  const nombreGuardado = leerCookie("td_contacto_nombre");
  const emailGuardado = leerCookie("td_contacto_email");

  if (nombreGuardado !== "") {
    inputNombre.value = nombreGuardado;
  }
  if (emailGuardado !== "") {
    inputEmail.value = emailGuardado;
  }

  function actualizarContadorMensaje() {
    const max = areaMensaje.maxLength > 0 ? areaMensaje.maxLength : 300;
    const min = areaMensaje.minLength > 0 ? areaMensaje.minLength : 15;
    const actual = areaMensaje.value.length;
    contadorCaracteres.textContent = actual + " / " + max + " caracteres (mínimo " + min + ")";
  }

  actualizarContadorMensaje();

  const camposValidables = [
    inputNombre,
    inputEmail,
    inputTelefono,
    selectMotivo,
    areaMensaje
  ];

  function validarUnCampo(campo) {
    let error = null;

    if (campo === inputNombre) {
      error = validarCampoObligatorio(campo.value, campo);
    } else if (campo === inputEmail) {
      error = validarEmail(campo.value, campo);
    } else if (campo === inputTelefono) {
      error = validarTelefono(campo.value, checkLlamar.checked);
    } else if (campo === selectMotivo) {
      error = validarMotivo(campo.value, campo);
    } else if (campo === areaMensaje) {
      error = validarMensaje(campo.value, campo);
    }

    mostrarEstadoCampo(campo, error);
    return error === null;
  }

  checkLlamar.addEventListener("change", () => {
    inputTelefono.required = checkLlamar.checked;
    etiquetaTelefono.textContent = checkLlamar.checked ? "(obligatorio)" : "(opcional)";

    if (inputTelefono.dataset.tocado === "true" || checkLlamar.checked) {
      inputTelefono.dataset.tocado = "true";
      validarUnCampo(inputTelefono);
    }
  });

  for (let i = 0; i < camposValidables.length; i = i + 1) {
    const campo = camposValidables[i];

    campo.addEventListener("blur", () => {
      campo.dataset.tocado = "true";
      validarUnCampo(campo);
    });

    const eventoTiempoReal = campo.tagName === "SELECT" ? "change" : "input";
    campo.addEventListener(eventoTiempoReal, () => {
      if (campo === areaMensaje) {
        actualizarContadorMensaje();
      }
      if (campo.dataset.tocado === "true") {
        validarUnCampo(campo);
      }
    });
  }

  form.addEventListener("submit", (evento) => {
    evento.preventDefault();
    let primerInvalido = null;

    for (let i = 0; i < camposValidables.length; i = i + 1) {
      const campo = camposValidables[i];
      campo.dataset.tocado = "true";
      const esValido = validarUnCampo(campo);

      if (!esValido && primerInvalido === null) {
        primerInvalido = campo;
      }
    }

    if (primerInvalido !== null) {
      primerInvalido.focus();
      return;
    }

    const datosMensaje = {
      nombre: inputNombre.value.trim(),
      email: inputEmail.value.trim(),
      prefieroLlamada: Boolean(checkLlamar.checked),
      telefono: inputTelefono.value.trim(),
      motivo: selectMotivo.value,
      mensaje: areaMensaje.value.trim()
    };

    crear("mensajes", datosMensaje);

    guardarCookie("td_contacto_nombre", datosMensaje.nombre, 7);
    guardarCookie("td_contacto_email", datosMensaje.email, 7);

    form.reset();
    inputTelefono.required = false;
    etiquetaTelefono.textContent = "(opcional)";
    actualizarContadorMensaje();
    limpiarEstadoFormulario(form);

    inputNombre.value = leerCookie("td_contacto_nombre");
    inputEmail.value = leerCookie("td_contacto_email");

    renderizarMensajes(listaMensajes, obtenerTodos("mensajes"), contadorMensajes);
  });

  listaMensajes.addEventListener("click", (evento) => {
    const boton = evento.target.closest("button[data-accion=\"borrar\"]");
    if (!boton) {
      return;
    }

    const id = boton.dataset.id;
    pedirConfirmacion("¿Seguro que quieres borrar este mensaje?", () => {
      borrar("mensajes", id);
      renderizarMensajes(listaMensajes, obtenerTodos("mensajes"), contadorMensajes);
    });
  });

  renderizarMensajes(listaMensajes, obtenerTodos("mensajes"), contadorMensajes);
}

document.addEventListener("DOMContentLoaded", () => {
  const listaStock = document.querySelector(".o-cuadricula");
  const contadorStock = document.querySelector(".inventario-stock__contador");
  const panelDetalle = document.querySelector("#detalle-alimento");

  if (listaStock && panelDetalle && typeof alimentos !== "undefined") {
    if (contadorStock) {
      contadorStock.textContent = alimentos.length + " alimentos";
    }
    renderizarListadoAlimentos(listaStock, alimentos, categorias, panelDetalle);
  }

  inicializarRegistro();
  inicializarContacto();
});