
#lista com lista dentro

fruta = [['maça', 52], ['banana', 39], ['abacaxi', 50], ['uva', 67]]
print(fruta[0])
print(fruta[0][0])
print(fruta [2][1])

#quando o usuario tem que perguntar se tem na lista
res =  str(input("Digite uma fruta"))
for C in fruta :
    if res in C :
        print("fruta escontrada")
    else:
        print('fruta não encontrada')
#adicionando a uma lista vazia
frutas = [[],[]]
frutas.append(['maca']) #adiciona em qualquer espaço vazio da lista

# os ':' cria uma cópia e não fica vinculado com a lista de cima.

#situação de baixo vai passar em toda a minha lista (mostrar todas as informações)
for C in fruta :
    print(f' a fruta {C[0]} tem {C[1]} calorias')