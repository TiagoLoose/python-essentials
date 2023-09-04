#!/usr/bin/env python3
"""Exemplos de comprehension
"""
__version__ = "0.0.1"

lista_completa = range(0,11)

lista_numeros_pares = [numero for numero in lista_completa if numero % 2 == 0]
lista_numeros_ao_quadrado = [numero**2 for numero in lista_completa]

print(f"Números: {list(lista_completa)}")
print(f"Números pares: {lista_numeros_pares}")
print(f"Números ao quadrado: {lista_numeros_ao_quadrado}")

dict_numeros = {numero: f"Numero: {numero}" for numero in lista_completa}
print(f"Dicionário com os números: {dict_numeros}")