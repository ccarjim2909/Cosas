# test_radares.py
# -*- coding: utf-8 -*-

import pytest
from src.nochevieja import procesar_linea

@pytest.mark.parametrize(
    "linea, esperado",
    [
        # Casos del enunciado:
        ("23:45", "15"),
        ("21:30", "150"),
        ("00:01", "1439"),
        ("00:00", "0"),

    ]
)

# Debes darle contenido a la siguiente función
def test_procesar_linea(linea, esperado):
   print(procesar_linea)