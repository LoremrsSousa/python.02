print('----------------')
print('senai é uma merda')
print('----------------')
print('=' * 20)
#rotinas
#criar função sem parametros
def  linha():
  print('-' * 20)


linha()
print('senai é uma merda')
linha()
#função com parametro

def linha(txt):
    print('- '* 20)
    print(txt)
    print('- ' * 20)

linha('senai é uma merda')

#fazendo equação - funçao
def soma(a,b):
    s = a + b
    print('a soma é : ', s)

soma(1,300)
#funçao com parametros indefinidos (*)
def sume( *valores):
    soma2 = 0
    for c in valores:
        soma2+= c
    print(' a soma é: ', soma2)
sume(22,22,66,66)

#quando o b for opcional
def soma3 (a, b =0):
    S = a + b
    print('a soma é: ', S)
soma3(1,300)
soma3(300)

#com retorno da função

def somar( a, b):
    S1 = a + b
    return  S1
A =  somar(1,200)
print(A)

#exemplo de exercicío
def parouimpar(a):
    if a %2 == 0 :
        print('é par')
    else:
        print('impar')


num = int(input(" Digite um numero: "))
parouimpar(num)

# isnumeric() se é numero ou nõo