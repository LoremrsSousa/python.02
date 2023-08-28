from modulo import maior

lista = []
while True:
    valor = input('Digite um número: ')
    lista.append(int(valor))  # Converte para inteiro antes de adicionar à lista

    res = input('Deseja continuar? (s/n): ')
    if res == 'n':
        break

print('O maior valor inserido foi:')
maior(lista)
