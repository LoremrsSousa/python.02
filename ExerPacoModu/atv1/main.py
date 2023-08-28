from Math import calculadora
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = str(input("Digite sua operação (+, -, *, /):  "))

if operacao == "+":
    somade = calculadora.soma(num1,num2)
    print(somade)
elif operacao == "-":
    subde = calculadora.subtracao(num1,num2)
    print(subde)
elif operacao == "*":
    multide = calculadora.multiplicacao(num1,num2)
    print(multide)
elif operacao == "/":
    divde = calculadora.divisao(num1,num2)
    print(divde)
else:
    print("Não é possivel realizar essa operação")


