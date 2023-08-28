lista = []

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: ' ))
telefone = input('Digite seu telefone: ')

pessoa = [nome, idade, telefone]
lista.append(pessoa)

pessoa.clear()

nome = input('Digite um novo nome: ')
idade = int(input('Digite uma nova idade: ' ))
telefone = input('Digite um novo telefone: ')

pessoa = [nome, idade, telefone]
lista.append(pessoa)

print("A nova lista é: ", lista)