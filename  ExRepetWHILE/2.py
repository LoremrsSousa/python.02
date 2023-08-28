pares  = 0
soma = 0
while True:
    numeros = int(input("Digite um Número: "))
    if numeros %2 == 0:
     soma += numeros
    elif numeros == -1:
     break
print(" A soma dos números pares é: ", soma)
