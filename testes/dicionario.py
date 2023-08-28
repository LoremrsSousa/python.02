pessoa = {'nome': 'Davi' , 'idade' : 16 , 'altura' : 1.80}
print(pessoa.values())
print(pessoa.keys())
print(pessoa.items())
for k in pessoa:
    print(k)
for k,v in pessoa.items():
    print({k},{v})