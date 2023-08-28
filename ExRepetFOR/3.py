quantidade = int(input('Qual é a quantidade de pessoas?: '))
soma =0

for n in range(quantidade):
    grau = float(input('Digite a sua temperatura: '))
    soma += grau
if grau <= 37.2:
    print(' a temperatura esta normal ')
elif grau >= 37.3 and grau <= 38 :
    print('está em estado febril: ')
elif grau > 38 and grau < 39 :
    print('com febre')
else:
    ('febre alta')
media = soma/quantidade
print('Quantidade de pessoas:', quantidade)
print('Média de temperatura dos clientes: ', media)
