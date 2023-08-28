bib = {}
while True:
    chave = str(input("Digite a nome da chave: "))
    bib[chave]= str(input(f' digite o valor de  {chave}: '))
    res = str(input('deseja continuar (s/n): '))
    if res in 'Nn':
        break
print(bib)