compra = float(input("Qual foi o valor da conta?: "))
prestacao = int(input("Quantas vezes você dividiu?: "))

valor = (compra / prestacao)
if valor > 500:
    print("Você não consegue pagar!")
    print(valor)
elif valor <= 500:
    print("Você consegue pagar! ")
    print(valor)