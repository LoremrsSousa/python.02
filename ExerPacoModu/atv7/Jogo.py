from Simula import Dados


def main():
    try:
        num_lados = int(input("Insira o número de lados do dado: "))
        resultado = Dados.dados(lados=)

        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"O resultado do lançamento do dado de {lados} lados é: {resultado}")

    except ValueError:
        print("Por favor, insira um número válido.")


if __name__ == "__main__":
    main()
