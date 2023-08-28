import random


def dados(lados):
    if lados <= 0:
        return "O número de lados do dado deve ser maior que 0."

    resultado = random.randint(1, lados)
    return resultado