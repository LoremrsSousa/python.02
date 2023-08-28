valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))

    res = ' '
    while res not in 'SN':
        res = str(input('Continuar? [S / N] ')).upper()[0]
    if res in 'N':
        break

print(f'Lista completa: {valores}')

for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')