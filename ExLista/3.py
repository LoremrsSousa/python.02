num1 = []
while True:
    num1.append(int(input('Digite um número: ')))
    res = str(input('Deseja continuar [S/N]: '))
    if res in 'Nn':
        break

soma = sum(num1)
menor = min(num1)

print(f'A soma de todos os números são {soma}')
print(f'O menor número é {menor}')