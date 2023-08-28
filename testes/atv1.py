while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input('Digite o preço do produto: '))
    res = str(input('Deseja continuar? S/N: '))
    if res in 'nN':
        break