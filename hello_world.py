#!/usr/bin/python3


# A esa primera linea se le llama shebang, indica como ejecutar codigo sin necesidad de indicar el programa que lo interpreta

import random

def calcular_porcentaje_aleatorio(minimo, maximo):
    return round(random.uniform(minimo, maximo))

def main():
    minimo = 1
    maximo = 100
    porcentaje_aleatorio = calcular_porcentaje_aleatorio(minimo, maximo)

    if porcentaje_aleatorio < 50:
        return "eres poco gay"
    elif porcentaje_aleatorio > 50:
        return "eres muy gay"
    else:
        return "eres medio gay"

if __name__ == "__main__":
    print(main())