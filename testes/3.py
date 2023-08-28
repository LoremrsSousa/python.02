fruta = ['abacaxi' , 'uva', 'banana', 'maçã']
fruta.append('Laranja')
fruta.insert(1, 'morango')
print(fruta)


num0 = list(range(1,7))
num = [7,5,3,0,9,6]
num.sort()
num.sort(reverse=True)


num1  = [7,5,3,0,9,6]
soma = sum(num1)
maior = max(num1)
menor = min(num1)

fruta = ['banana', ' maçã', 'laranja', 'abacaxi']
maior = max(fruta, key = len)
menor = min(fruta, key= len )



num1  = [7,5,3,0,9,6]
num2 = num1 [:]
num2[1] = 2

num3 = []
while True:
    num3.append( int(input(' Digite um numero : ')))
    res = str(input('Deseja continuar?:  [S/N]'))
    if res in 'Nn':
        break



