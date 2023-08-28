from random import randint

dicionario = {}
i = 0

while i < 4:
    nomedachave = input('Insira o seu nome: ')
    dicionario[nomedachave] = randint(1,6)
    i += 1

print('Assim ficou o placar do sorteio:', dicionario)