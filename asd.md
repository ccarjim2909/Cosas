# Calculadora binaria de 8 bits (Python) — README

> CLI que **suma** y **resta** números binarios de **8 bits**.  
> **Salida exclusivamente en binario de 8 bits** (listas con bits).  
> Si no se indica signo, el programa ejecuta **ambas operaciones** (suma y resta).

---

## 1) Descripción del módulo

Este proyecto implementa una **calculadora binaria de 8 bits** que opera con **enteros sin signo**.  
El programa permite realizar **sumas y restas** entre dos números binarios, verificando que los operandos sean válidos.

- Los **operandos** se introducen como **cadenas binarias** de exactamente **8 bits** (`0`/`1`).
- La **operación** se define con el **signo** `+` (suma) o `-` (resta).
- Si no se especifica signo, el programa ejecuta **ambas operaciones** automáticamente.
- El resultado se muestra como **lista de bits** binarios en formato de 8 bits.

---

## 2) Requisitos

- **Python 3.10 o superior**
- **Sin dependencias externas**

Si en un futuro se añaden librerías adicionales, estas se incluirán en el archivo **`dependecias.txt`** (ver sección 5).

---

## 3) Instalación de Python

### 3.1 Linux

#### Debian/Ubuntu
```bash
sudo apt update
sudo apt install -y python3 python3-pip
python3 --version
python3 -m pip --version
