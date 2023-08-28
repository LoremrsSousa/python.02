total = 0
caro = 0
ncaro = ''
while True:
    produto = str(input("Qual é o nome do produto? "))
    preco = float(input('Qual é o preço?: '))
    total += preco
    if preco > caro:
        caro = preco
        ncaro = produto
    res = str(input('Deseja continuar? S/N: '))
    if res == 'N':
        break

print('O produto mais caro é: ' , ncaro)
print("O total da compra é: " ,  total)

