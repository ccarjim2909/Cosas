# Informe Práctica 3.1 — Instalación, arquitectura y despliegue de múltiples sitios en Nginx

## 1. Portada y datos generales
* **Autor:** Cristian Carrasco Jimenez
* **Fecha:** 2026-11-23
* **Sistema operativo:** Ubuntu 26.04.1 LTS (Kernel Linux 7.0.0-44-generic, x86_64) — ver [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt)* **Sistema operativo:** Debian GNU/Linux (ver [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt))
* **Versión de Nginx:** nginx version: nginx/1.28.3 (Ubuntu)
* **Opción elegida:** **Opción B — Diferenciación por nombres de dominio (`saludo.local` y `repetidor.local`)** mediante la cabecera HTTP `Host` en el puerto `80` (ver [0.-opcion_elegida.txt](evidencias-nginx-p1/0.-opcion_elegida.txt)). Se ha elegido esta opción porque refleja el funcionamiento real de alojamiento de múltiples dominios en un mismo servidor web sin obligar al cliente a especificar puertos no estándar.

---

## 2. Objetivo y alcance
El objetivo de esta práctica es instalar y configurar el servidor web **Nginx** en un entorno GNU/Linux Debian para publicar simultáneamente dos aplicaciones web frontend estáticas (`saludo-app` y `repetidor-app`) mediante Virtual Hosts basados en nombre, verificando su funcionamiento mediante pruebas HTTP (`curl`), pruebas funcionales en navegador y análisis de registros (`access.log` y `error.log`). El alcance corresponde a un entorno controlado de laboratorio/aula.

---

## 3. Diagrama de arquitectura y recorrido de una petición

```text
+-----------------------------------+
|  Cliente (Navegador web / curl)   |
|  Resolución local (/etc/hosts):   |
|  saludo.local / repetidor.local   |
+-----------------+-----------------+
                  | Petición HTTP GET / (Puerto 80)
                  | Cabecera Host: saludo.local | repetidor.local
                  v
+-----------------------------------+
|         Servidor Web Nginx        |
|  Evalúa puerto (80) + server_name |
+--------+-----------------+--------+
         |                 |
         | Host:           | Host:
         | saludo.local    | repetidor.local
         v                 v
+-----------------+ +-------------------+
| /var/www/       | | /var/www/         |
| saludo-app/     | | repetidor-app/    |
| index.html      | | index.html        |
+-----------------+ +-------------------+
```
**Recorrido de la petición:**
1. El cliente resuelve el dominio (`saludo.local` o `repetidor.local`) a `127.0.0.1` gracias a `/etc/hosts` y abre una conexión TCP al puerto `80`.
2. Envía una petición `GET / HTTP/1.1` incluyendo la cabecera `Host` con el dominio solicitado.
3. Nginx escucha en el puerto `80`, inspecciona la cabecera `Host` y selecciona el bloque `server` cuya directiva `server_name` coincide.
4. Dentro del bloque seleccionado, la directiva `location /` aplica `try_files $uri $uri/ =404;` y, al tratarse de `/`, resuelve `index index.html;` dentro de la ruta `root` correspondiente.
5. Nginx devuelve una respuesta `HTTP/1.1 200 OK` junto con el contenido estático de `index.html`.
6. El navegador recibe el documento y ejecuta localmente el CSS y el JavaScript en el equipo cliente (Nginx actúa únicamente como servidor de ficheros estáticos y no ejecuta JavaScript).

---

## 4. Ficha de requisitos y recursos

| Dato | Valor registrado |
| :--- | :--- |
| **Sistema operativo y versión** | Debian GNU/Linux (detalle en [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt)) |
| **Arquitectura de CPU** | x86_64 (detalle en [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt)) |
| **CPU y memoria asignadas** | Ver [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt) |
| **Disco disponible** | Ver [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt) |
| **Dirección IP del servidor** | `127.0.0.1` / IP privada local (ver [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt)) |
| **Puertos y protocolos** | `80/tcp` (HTTP) |
| **Nombres de dominio** | `saludo.local` y `repetidor.local` en `/etc/hosts` |
| **Permisos de raíz web** | Propietario usuario local, lectura global (`755` directorios / `644` `index.html`) para `www-data` |
| **Firewall** | Ver estado en [2.-instalacion-y-estado.txt](evidencias-nginx-p1/2.-instalacion-y-estado.txt) |
| **Cliente de prueba** | `curl` y navegador web local en Debian |
| **Resultado válido acordado** | Ambos sitios devuelven HTTP 200 y sus funciones interactivas producen el resultado esperado. |

---

## 5. Instalación y puesta en marcha de Nginx
Se actualizó el índice de paquetes con `apt update` y se instaló el paquete `nginx`. Posteriormente se habilitó e inició el demonio mediante `systemctl enable --now nginx`, comprobando que el estado es `active (running)` y que el proceso escucha en el puerto `80`.
* **Evidencia:** [2.-instalacion-y-estado.txt](evidencias-nginx-p1/2.-instalacion-y-estado.txt)

---

## 6. Arquitectura de ficheros de Nginx

| Ruta | Tipo | Función principal |
| :--- | :--- | :--- |
| `/etc/nginx/` | Directorio | Raíz de configuración del servidor Nginx. |
| `/etc/nginx/nginx.conf` | Archivo | Configuración global (procesos `worker`, MIME types, logs e instrucciones `include`). |
| `/etc/nginx/sites-available/` | Directorio | Almacén de definiciones de Virtual Hosts disponibles (activos o inactivos). |
| `/etc/nginx/sites-enabled/` | Directorio | Enlaces simbólicos hacia `sites-available/` que `nginx.conf` incluye efectivamente. |
| `/var/www/` | Directorio | Raíz habitual donde se alojan los recursos públicos de cada sitio web. |
| `/var/log/nginx/` | Directorio | Contiene `access.log` (tráfico recibido) y `error.log` (errores de servicio o rutas). |

* **Evidencia:** [3.-arquitectura-ficheros.txt](evidencias-nginx-p1/3.-arquitectura-ficheros.txt)

---

## 7. Aplicaciones web desplegadas
* **Sitio 1 (`saludo-app`):** alojado en `/var/www/saludo-app/index.html`. Metadatos en [4.-saludo-app.txt](evidencias-nginx-p1/4.-saludo-app.txt) y copia en [4.-saludo-app.index.html](evidencias-nginx-p1/4.-saludo-app.index.html).
* **Sitio 2 (`repetidor-app`):** alojado en `/var/www/repetidor-app/index.html`. Metadatos en [5.-repetidor-app.txt](evidencias-nginx-p1/5.-repetidor-app.txt) y copia en [5.-repetidor-app.index.html](evidencias-nginx-p1/5.-repetidor-app.index.html).

---

## 8. Configuración de sitios virtuales (Opción B)
Ambos bloques `server` escuchan en el puerto `80` y se diferencian mediante la directiva `server_name`:
* **Configuración `saludo-app` (`saludo.local`):** [6.-saludo-app.conf](evidencias-nginx-p1/6.-saludo-app.conf)
* **Configuración `repetidor-app` (`repetidor.local`):** [7.-repetidor-app.conf](evidencias-nginx-p1/7.-repetidor-app.conf)

---

## 9. Activación, validación y pruebas HTTP
Se crearon los enlaces simbólicos en `/etc/nginx/sites-enabled/`, se desactivó `default` mediante `unlink`, se validó la sintaxis con `nginx -t` (`syntax is ok` / `test is successful`) y se aplicaron los cambios sin corte de servicio con `systemctl reload nginx`.
* **Activación y validación:** [8.-activacion-y-validacion.txt](evidencias-nginx-p1/8.-activacion-y-validacion.txt)
* **Recarga y estado:** [9.-recarga-y-estado.txt](evidencias-nginx-p1/9.-recarga-y-estado.txt)
* **Configuración efectiva (`nginx -T`):** [10.-nginx-configuracion-efectiva.txt](evidencias-nginx-p1/10.-nginx-configuracion-efectiva.txt)
* **Pruebas HTTP con `curl`:** [11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt)

---

## 10. Pruebas funcionales y registros
* **Resultados en navegador:** [12.-pruebas-funcionales.txt](evidencias-nginx-p1/12.-pruebas-funcionales.txt)
* **Registros (`access.log`, `error.log` y `journal`):** [13.-registros.txt](evidencias-nginx-p1/13.-registros.txt)
* **Índice e inventario completo:** [README.md](evidencias-nginx-p1/README.md) y [14.-inventario-y-validacion.txt](evidencias-nginx-p1/14.-inventario-y-validacion.txt)

---

## 11. Matriz de pruebas

| ID | Precondiciones | Acción | Resultado esperado | Resultado obtenido | Estado | Evidencia |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P-01** | Nginx activo y sintaxis válida | `curl -i http://saludo.local/` | `HTTP/1.1 200 OK` y HTML de `Saludo en Nginx` | `HTTP/1.1 200 OK` con HTML correcto | **PASS** | [11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt) |
| **P-02** | Nginx activo y sintaxis válida | `curl -i http://repetidor.local/` | `HTTP/1.1 200 OK` y HTML de `Repetidor Hola Mundo` | `HTTP/1.1 200 OK` con HTML correcto | **PASS** | [11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt) |
| **P-03** | Sitios habilitados en puerto 80 | Petición a `127.0.0.1` alterando cabecera `Host` | Selección dinámica del Virtual Host según `Host` | Cada cabecera devuelve su propio `index.html` | **PASS** | [11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt) |
| **P-04** | `saludo.local` cargado en navegador | Introducir `Pedro` y pulsar **Aceptar** | Muestra `Hola Pedro!!` | Muestra `Hola Pedro!!` | **PASS** | [12.-pruebas-funcionales.txt](evidencias-nginx-p1/12.-pruebas-funcionales.txt) |
| **P-05** | `saludo.local` cargado en navegador | Dejar campo vacío y pulsar **Aceptar** | Muestra `Por favor, escribe un nombre.` | Muestra el aviso de validación | **PASS** | [12.-pruebas-funcionales.txt](evidencias-nginx-p1/12.-pruebas-funcionales.txt) |
| **P-06** | `repetidor.local` cargado en navegador | Introducir `4` y pulsar **Generar** | Genera 4 líneas numeradas `¡Hola mundo!` | Genera de `1. ¡Hola mundo!` a `4. ¡Hola mundo!` | **PASS** | [12.-pruebas-funcionales.txt](evidencias-nginx-p1/12.-pruebas-funcionales.txt) |
| **P-07** | `repetidor.local` cargado en navegador | Introducir `0` o campo vacío y pulsar **Generar** | Muestra aviso de número válido sin generar líneas | Muestra el aviso sin crear elementos DOM | **PASS** | [12.-pruebas-funcionales.txt](evidencias-nginx-p1/12.-pruebas-funcionales.txt) |
| **P-08** | Directiva `try_files $uri $uri/ =404;` activa | `curl -i http://saludo.local/ruta-que-no-existe` | Respuesta `HTTP/1.1 404 Not Found` | `HTTP/1.1 404 Not Found` y registro en logs | **PASS** | [11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt) |

---

## 12. Ejercicios de análisis y relación con RA1

### Ejercicios de análisis
1. **Arquitectura:** Nginx actúa como servidor HTTP receptor en el puerto `80`; localiza el fichero `index.html` en disco y genera la respuesta HTTP (línea de estado y cabeceras). El navegador del cliente recibe el texto plano del HTML y es quien interpreta el DOM, aplica los estilos CSS embebidos y ejecuta el código JavaScript al hacer clic en los botones.
2. **Comparación de selección (Opción A vs Opción B):**
   * En la **Opción A**, la directiva `listen` diferencia los sitios (`80` vs `8080`) mientras `server_name` puede ser idéntico (`localhost`). Es rápida para pruebas sin tocar DNS/`hosts`, pero obliga a indicar el puerto en la URL y puede chocar con cortafuegos.
   * En la **Opción B**, ambos comparten `listen 80;` y se distinguen mediante `server_name` (`saludo.local` vs `repetidor.local`). El cliente envía el dominio deseado en la cabecera HTTP `Host`. Es el estándar en producción para alojar múltiples webs bajo una misma IP y puerto `80/443`, aunque requiere resolución de nombres previa (`/etc/hosts` o DNS).
3. **Análisis HTTP:** En la salida de `curl --include`, la **línea de estado** es `HTTP/1.1 200 OK`; entre las **cabeceras** destacan `Server: nginx/...`, `Content-Type: text/html` y `Content-Length`; tras una línea en blanco viaja el **cuerpo HTML**. Un `HTTP 200` solo confirma que Nginx encontró y entregó el archivo `index.html` sin errores de servidor, pero no valida que el JavaScript funcione en el navegador (un error de sintaxis JS seguiría devolviendo `200 OK`).
4. **Estructura web:** Cada aplicación consta de un fichero `index.html` con CSS embebido (`<style>`) y JavaScript embebido (`<script>`) ubicados en su raíz pública (`/var/www/saludo-app` y `/var/www/repetidor-app`), un fichero de configuración de sitio en `/etc/nginx/sites-available/` y los logs compartidos en `/var/log/nginx/`. Todos los recursos de la aplicación son **estáticos** y la lógica JS se ejecuta íntegramente en el **cliente (navegador)**.
5. **Diagnóstico de códigos HTTP:**
   * **HTTP 404:** Ruta o recurso inexistente en el `root` configurado (comprobado en `11.-pruebas-http.txt` y `13.-registros.txt`).
   * **HTTP 403:** Revisaría permisos de lectura (`644`) en los ficheros y de ejecución/travesía (`755`) en `/var/www/...` para el usuario `www-data`, la existencia de `index.html` o reglas `deny` en Nginx.
   * **HTTP 502 (Bad Gateway):** Revisaría si el servicio backend o PHP-FPM al que apunta `proxy_pass` / `fastcgi_pass` está caído o escuchando en un socket/puerto incorrecto.
   * **HTTP 503 (Service Unavailable):** Revisaría saturación de conexiones/workers, límites de tasa (`limit_req`) o estado de mantenimiento del servicio.
6. **Seguridad y mantenimiento:** Nunca se deben guardar secretos (`.env`, claves privadas, credenciales) dentro de `/var/www/` porque cualquier archivo accesible bajo la raíz pública puede ser descargado directamente vía HTTP si no se bloquea explícitamente. Validar siempre con `nginx -t` antes de `systemctl reload nginx` evita que un error de sintaxis deje el servidor inoperativo o impida recargar la configuración. Antes de modificar un sitio en producción, se debe conservar una copia de respaldo del archivo de `/etc/nginx/sites-available/` (por ejemplo `sitio.conf.bak` fuera de rutas incluidas por Nginx).

### Relación de evidencias con RA1
* **RA1.a:** Diagrama y comparativa Puertos vs Nombres en apartados 3, 12.1 y 12.2 ([0.-opcion_elegida.txt](evidencias-nginx-p1/0.-opcion_elegida.txt)).
* **RA1.b:** Análisis de peticiones HTTP, cabecera `Host` y códigos de estado en [11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt).
* **RA1.c:** Instalación, activación de Virtual Hosts, validación y recarga sin corte en [2.-instalacion-y-estado.txt](evidencias-nginx-p1/2.-instalacion-y-estado.txt), [6.-saludo-app.conf](evidencias-nginx-p1/6.-saludo-app.conf), [7.-repetidor-app.conf](evidencias-nginx-p1/7.-repetidor-app.conf), [8.-activacion-y-validacion.txt](evidencias-nginx-p1/8.-activacion-y-validacion.txt) y [9.-recarga-y-estado.txt](evidencias-nginx-p1/9.-recarga-y-estado.txt).
* **RA1.f:** Matriz de pruebas funcionales, prueba negativa 404 y revisión de logs en [11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt), [12.-pruebas-funcionales.txt](evidencias-nginx-p1/12.-pruebas-funcionales.txt) y [13.-registros.txt](evidencias-nginx-p1/13.-registros.txt).
* **RA1.g:** Inventario de recursos estáticos, directorios de configuración y logs en [3.-arquitectura-ficheros.txt](evidencias-nginx-p1/3.-arquitectura-ficheros.txt), [4.-saludo-app.txt](evidencias-nginx-p1/4.-saludo-app.txt) y [5.-repetidor-app.txt](evidencias-nginx-p1/5.-repetidor-app.txt).
* **RA1.h:** Ficha de requisitos y entorno inicial en [1.-entorno.txt](evidencias-nginx-p1/1.-entorno.txt) y apartado 4 del informe.
* **RA1.i:** Documentación reproducible completa, índice de evidencias e inventario verificado en [README.md](evidencias-nginx-p1/README.md) y [14.-inventario-y-validacion.txt](evidencias-nginx-p1/14.-inventario-y-validacion.txt).

---

## 13. Incidencias encontradas y recuperación
* **Incidencia 1 (Herramienta `curl` no preinstalada):** Al ejecutar las pruebas HTTP desde terminal, Debian no incluía `curl` en la instalación base. *Solución:* Instalación mediante `apt install curl -y` y repetición exitosa de las pruebas ([11.-pruebas-http.txt](evidencias-nginx-p1/11.-pruebas-http.txt)).
* **Incidencia 2 (Sitio `default` en `sites-enabled`):** El enlace simbólico predeterminado podía interceptar peticiones en el puerto `80`. *Solución:* Eliminación mediante `unlink /etc/nginx/sites-enabled/default` y verificación de enlaces activos ([8.-activacion-y-validacion.txt](evidencias-nginx-p1/8.-activacion-y-validacion.txt)).
* **Procedimiento de recuperación:** Ante un fallo tras modificar un sitio, restaurar la copia de `/etc/nginx/sites-available/`, comprobar la sintaxis con `nginx -t` y ejecutar `systemctl reload nginx` (o `systemctl restart nginx` si el servicio estuviera detenido).
