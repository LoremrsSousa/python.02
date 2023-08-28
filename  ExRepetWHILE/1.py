nota = 1
smedia = 0
quantidade = 0
while nota > 0:
    nota = float(input("Digite a Nota: "))
    quantidade +=1
    smedia += nota
media= smedia/quantidade
print('A média das notas é: ', media)
