
#1
def LarguraeComprimento(a,b):
    area = a * b
    print('o valor da area é: ', area)

#2
def  escreva(txt):
    print('- ' * len(txt))
    print(txt)
    print('- ' * len(txt))
#3
def maior(valores):
    b = max(valores)
    print(f'O maior número é: {b}')

#4

def voto(a,b):
    var = a - b
    if var >= 18:
        print('Ovoto é obrigatorio')
    elif var == 16 or var ==17:
        print('O vota é opicional')
    else:
        print('Voto negado')
#5
def ficha(nome =  '', gols = 0 ):
    print(f'o jogador{nome} marcou {gols}. ')