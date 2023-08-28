num1= float(input("Adicione um num1: "))
num2= float(input("Adicione um num1: "))

resultado1 = (num1 + num2)
resultado2 = (num1/num2)
resultado3 = (num1 * num2)
resultado4 = (num1 - num2)



operacao = int(input('Escolha sua operação: somar = 1\n dividir = 2\n multiplicar = 3\n subtrair = 4\n '
))

if operacao == 1:
    print('O resultado foi: ' , resultado1)
elif  operacao == 2:
    print('O resultado foi: ' , resultado2)
elif  operacao == 3:
    print('O resultado foi: ' , resultado3)
else:
    print('O resultado foi: ', resultado4)





