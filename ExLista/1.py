numeros = []
multi = 1
mult2 = 1
while True:
    mult = (int(input('Digite um número: ')))
    numeros.append(multi)
    mult2 = multi*mult2
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'Nn':
        break
    print(f'Os números são {numeros}')

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

print(f'A soma é:  {soma}')
print(f'O maior é:  {maior}')
print(f'O menor é:  {menor}')
print(f"Todos os itens multiplicados dá:  {mult2}")