nota = {}
while True:
    chave = str(input("Digite a nome da chave: "))
    nota[chave] = int(input(f"Digite a nota:  "))
    res = str(input('deseja continuar (s/n): '))
    if res in 'Nn':
        media= (sum(nota.values()))/len(nota)
        break
print(nota)
print(media)