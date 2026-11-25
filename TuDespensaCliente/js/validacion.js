function validarCampoObligatorio(valor, elemento) {
  if (elemento && elemento.required && valor.trim() === "") {
    return "Este campo es obligatorio.";
  }
  return null;
}

function validarUsuario(valor, elemento) {
  const errorObligatorio = validarCampoObligatorio(valor, elemento);
  if (errorObligatorio !== null) {
    return errorObligatorio;
  }

  const limpio = valor.trim();
  const min = elemento && elemento.minLength > 0 ? elemento.minLength : 3;
  const max = elemento && elemento.maxLength > 0 ? elemento.maxLength : 20;

  if (limpio.length < min) {
    return "El nombre de usuario debe tener al menos " + min + " caracteres.";
  }
  if (limpio.length > max) {
    return "El nombre de usuario no puede superar " + max + " caracteres.";
  }

  const regexUsuario = /^[a-zA-Z0-9_áéíóúÁÉÍÓÚñÑ]+$/;
  if (!regexUsuario.test(limpio)) {
    return "Solo se permiten letras, números y guion bajo.";
  }

  return null;
}

function validarEmail(valor, elemento) {
  const errorObligatorio = validarCampoObligatorio(valor, elemento);
  if (errorObligatorio !== null) {
    return errorObligatorio;
  }

  const limpio = valor.trim();
  const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  if (!regexEmail.test(limpio)) {
    return "Introduce un correo electrónico válido (ejemplo@dominio.com).";
  }

  return null;
}

function validarContrasena(valor, elemento) {
  const errorObligatorio = validarCampoObligatorio(valor, elemento);
  if (errorObligatorio !== null) {
    return errorObligatorio;
  }

  const min = elemento && elemento.minLength > 0 ? elemento.minLength : 8;
  if (valor.length < min) {
    return "La contraseña debe tener al menos " + min + " caracteres.";
  }

  const tieneMayuscula = /[A-ZÁÉÍÓÚÑ]/.test(valor);
  const tieneNumero = /[0-9]/.test(valor);

  if (!tieneMayuscula || !tieneNumero) {
    return "Debe incluir al menos una letra mayúscula y un número.";
  }

  return null;
}

function validarRepetirContrasena(valor, contrasenaOriginal, elemento) {
  const errorObligatorio = validarCampoObligatorio(valor, elemento);
  if (errorObligatorio !== null) {
    return errorObligatorio;
  }

  if (valor !== contrasenaOriginal) {
    return "Las contraseñas no coinciden.";
  }

  return null;
}

function validarFechaNacimiento(valor, elemento) {
  const errorObligatorio = validarCampoObligatorio(valor, elemento);
  if (errorObligatorio !== null) {
    return errorObligatorio;
  }

  const fechaNac = new Date(valor + "T00:00:00");
  if (Number.isNaN(fechaNac.getTime())) {
    return "Introduce una fecha válida.";
  }

  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);

  if (fechaNac > hoy) {
    return "La fecha de nacimiento no puede ser futura.";
  }

  if (elemento && elemento.max && valor > elemento.max) {
    return "Debes tener al menos 16 años para gestionar tu despensa.";
  }

  if (elemento && elemento.min && valor < elemento.min) {
    return "La fecha introducida es demasiado antigua.";
  }

  return null;
}

function validarAceptacion(checked, elemento) {
  if (elemento && elemento.required && !checked) {
    return "Debes aceptar las condiciones de uso para continuar.";
  }
  return null;
}

function validarTelefono(valor, esObligatorioPorContacto) {
  const limpio = valor.trim();

  if (limpio === "") {
    if (esObligatorioPorContacto) {
      return "El teléfono es obligatorio si prefieres que te llamemos.";
    }
    return null;
  }

  const regexTelefono = /^(?:\+34\s?)?[6789]\d{8}$/;
  if (!regexTelefono.test(limpio.replace(/\s+/g, ""))) {
    return "Introduce un teléfono español válido de 9 dígitos.";
  }

  return null;
}

function validarMotivo(valor, elemento) {
  const errorObligatorio = validarCampoObligatorio(valor, elemento);
  if (errorObligatorio !== null) {
    return errorObligatorio;
  }
  return null;
}

function validarMensaje(valor, elemento) {
  const errorObligatorio = validarCampoObligatorio(valor, elemento);
  if (errorObligatorio !== null) {
    return errorObligatorio;
  }

  const limpio = valor.trim();
  const min = elemento && elemento.minLength > 0 ? elemento.minLength : 15;
  const max = elemento && elemento.maxLength > 0 ? elemento.maxLength : 300;

  if (limpio.length < min) {
    return "El mensaje debe tener al menos " + min + " caracteres.";
  }

  if (limpio.length > max) {
    return "El mensaje no puede superar los " + max + " caracteres.";
  }

  return null;
}