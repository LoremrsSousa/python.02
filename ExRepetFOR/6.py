homemvelho= ' '
mulheres = 0
idadeh = 0
for ps in range (1,9):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo: '))
    if sexo == "homem" and idade > idadeh:
        homemvelho = nome
    if sexo == "mulher" and idade < 20:
        mulheres +=1

print("O homem mais velho é: ", homemvelho)
print('A mulheres menores de 20 anos : ', mulheres)