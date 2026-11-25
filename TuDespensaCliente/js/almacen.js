const PREFIJO_ALMACEN = "tudespensa_";
const CLAVE_SESION = PREFIJO_ALMACEN + "sesion";

function obtenerTodos(coleccion) {
  const clave = PREFIJO_ALMACEN + coleccion;
  const datosCrudos = localStorage.getItem(clave);

  if (!datosCrudos) {
    return [];
  }

  return JSON.parse(datosCrudos);
}

function guardarColeccion(coleccion, lista) {
  const clave = PREFIJO_ALMACEN + coleccion;
  localStorage.setItem(clave, JSON.stringify(lista));
}

function obtenerPorId(coleccion, id) {
  const lista = obtenerTodos(coleccion);
  let encontrado = null;
  let i = 0;

  while (i < lista.length && encontrado === null) {
    if (String(lista[i].id) === String(id)) {
      encontrado = lista[i];
    }
    i = i + 1;
  }

  return encontrado;
}

function crear(coleccion, dato) {
  const lista = obtenerTodos(coleccion);
  const nuevoRegistro = {
    ...dato,
    id: Date.now()
  };

  lista.push(nuevoRegistro);
  guardarColeccion(coleccion, lista);
  return nuevoRegistro;
}

function actualizar(coleccion, id, dato) {
  const lista = obtenerTodos(coleccion);
  let actualizado = null;
  let i = 0;

  while (i < lista.length && actualizado === null) {
    if (String(lista[i].id) === String(id)) {
      lista[i] = {
        ...lista[i],
        ...dato,
        id: lista[i].id
      };
      actualizado = lista[i];
    }
    i = i + 1;
  }

  if (actualizado !== null) {
    guardarColeccion(coleccion, lista);
  }

  return actualizado;
}

function borrar(coleccion, id) {
  const lista = obtenerTodos(coleccion);
  const nuevaLista = [];
  let eliminado = false;

  for (let i = 0; i < lista.length; i = i + 1) {
    if (String(lista[i].id) === String(id)) {
      eliminado = true;
    } else {
      nuevaLista.push(lista[i]);
    }
  }

  if (eliminado) {
    guardarColeccion(coleccion, nuevaLista);
  }

  return eliminado;
}

function iniciarSesionUsuario(idUsuario) {
  localStorage.setItem(CLAVE_SESION, String(idUsuario));
}

function obtenerUsuarioActivo() {
  const idSesion = localStorage.getItem(CLAVE_SESION);
  if (!idSesion) {
    return null;
  }
  return obtenerPorId("usuarios", idSesion);
}

function cerrarSesionUsuario() {
  localStorage.removeItem(CLAVE_SESION);
}