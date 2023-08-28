mulher = 0
homem = 0
grupo = 0
somam= 0
somah= 0
for n in range(1,11):
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo: '))
    if sexo == 'mulher':
        mulher = mulher+idade
        somam=somam+1
        grupo=idade+grupo
    elif sexo == 'homem':
        homem = homem+idade
        somah = somah+1
        grupo = idade+grupo

mediam = mulher/somam
mediah = homem/somah
media = grupo/10

print('Média da mulheres:',mediam)
print('Média dos Homens: ', mediah)
print('Média do Grupo' , media)