taxa = int(input('digite a taxa: '))
valor = int(input('digite o valor: '))
tempo = int(input('digite o tempo: '))
prestação = valor + (valor * (taxa/100) * tempo)

print( "o  valor de uma prestação em atraso: ", prestação)
