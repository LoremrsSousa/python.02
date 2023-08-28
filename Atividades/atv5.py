from random import randint
num1 = randint(1,10)
while True:
    num = int(input('Digite um número entre 1 e 10: '))
    if num == num1:
        print("Parabéns, os números sãos iguais ao sorteado!")
        break
    else:
        print("Não foi dessa vez, tente novamente!")
