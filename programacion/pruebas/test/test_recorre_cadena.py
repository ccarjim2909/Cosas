import pytest
from recorre_cadena import saca_vocales2

@pytest.mark.parametrize(
    "palabra, resultado",
    [
        # Casos del enunciado:
        ("hola", "oa"),
        ("pepe", "ee"),
        ("septiembre", "eiee"),
        ("agosto", "aoo"),
    ]
)

# Debes darle contenido a la siguiente función
def test_saca_vocales(palabra, resultado):
   assert saca_vocales2(palabra) == resultado