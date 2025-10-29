# Calculadora binaria de 8 bits (Python) — README

> Programa que **suma** y **resta** números binarios de **1 a 8 bits**.
> 
> **Salida exclusivamente en binario de 8 bits** (relleno con ceros a la izquierda).
> 
> Si no se indica signo, el programa ejecuta **ambas operaciones** (suma y resta).

---

## 1) Descripción del módulo

Este proyecto implementa una **calculadora binaria de 8 bits** que opera con **enteros sin signo**.
- Los **operandos** se introducen como **cadenas binarias** de **1 a 8 bits** (`0`/`1`).
- La **operación** se define por **signo**: `+` (suma) o `-` (resta).
- Si **no** se especifica el signo, el programa **realiza ambas operaciones** con los mismos operandos y muestra **dos bloques** de salida.
- Antes de calcular, cada operando se **rellena a 8 bits** para el cálculo/visualización.



---

## 2) Requisitos

- **Python 3.10 o superior**.
- **Sin dependencias externas obligatorias.**
- Si en algún momento se añaden librerías, se listarán en el archivo **`dependecias.txt`** (ver sección 5).

---

## 3) Instalación de Python

### 3.1 Linux

#### Debian/Ubuntu (y derivados)
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
```

### 3.2 Windows

#### Opción A — Microsoft Store
1. Abrir **Microsoft Store**, buscar **Python 3.x** (Python Software Foundation).
2. Instalar y verificar:
```powershell
py --version
py -m pip --version
```

#### Opción B — Instalador oficial
1. Descargar desde **https://www.python.org/downloads/** el instalador de Python 3.x.
2. **Marcar** “**Add Python to PATH**” durante la instalación.
3. Verificar:
```powershell
py --version
py -m pip --version
```

---

## 4) Ejecución del módulo

### Sintaxis general
```bash
python nombre_modulo.py OPERANDO1 [SIGNO] OPERANDO2
```
- `OPERANDO1` y `OPERANDO2`: binarios de 8 bits**.
- `SIGNO` (opcional): `+` para **suma**, `-` para **resta**.
- Si **omites el signo**, el programa realiza **suma y resta** y muestra **dos bloques** de salida.


### Ejemplos

**Suma explícita**
```bash
# Linux/macOS
python nombre_modulo.py 10110010 + 11011010

# Windows
py nombre_modulo.py 10100001 + 11011001
```
Salida esperada:
```
El resultado la suma de estos dos numeros es: 00001101
```

**Resta explícita**
```bash
# Linux/macOS
python nombre_modulo.py 10110010 - 11011010

# Windows
py nombre_modulo.py 10100001 - 11011001
```
Salida esperada:
```
El resultado la resta de estos dos numeros es:  01111111
```

**Sin signo (ejecuta ambas)**
```bash
# Linux/macOS
python nombre_modulo.py 10110010 11011010

# Windows
py nombre_modulo.py 10100001 11011001
```
Salida esperada:
```
El resultado la suma de estos dos numeros es: 100000000

El resultado la resta de estos dos numeros es: 11111110
```
---


## 5) Mensajes de error y códigos de salida

- **Operando inválido** (no binario o > 8 bits)
- Mensaje: `El primer/segundo numero que has escrito no es un numero binario o no tiene 8 bits, vuelve a intentarlo.` →
- **Signo/operación inválida** (distinta de `+` o `-`)
- Mensaje: `Operando no válido. Usa únicamente '+' o '-'.` →


---

## 6) Problemas frecuentes (FAQ)

- **“python: command not found” / “py no se reconoce”** → Instala Python (ver sección 3)
- **Formato de operando incorrecto** → Revisa que sean solo `0`/`1` y longitud ≤ 8.
- **Signo en posición incorrecta** → Asegúrate de usar `OPERANDO1 [SIGNO] OPERANDO2`.

---

