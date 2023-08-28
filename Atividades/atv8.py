pessoa = { 'Lorena' : 16 , 'Mariana' : 17}
inf = str(input("Digite um dos nomes, Lorena ou Mariana: "))
for K,V in pessoa.items():
    if K == inf:
        print(V)