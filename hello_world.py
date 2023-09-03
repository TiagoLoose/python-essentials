#!/usr/bin/python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável APP_LANG devidamente configurada ex:

    export APP_LANG=pt_BR

Execução:

    python3 hello_world.py
    ou
    ./hello_world.py
"""
__version__ = "0.0.1"
__author__ = "Tiago Loose"
__license__ = "Unlicense"

import os

current_lang = os.getenv("APP_LANG", "en_US")[:5]

menssages = {
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
    "en_US": "Hello world!"
}
msg = menssages[current_lang]

print(msg)
