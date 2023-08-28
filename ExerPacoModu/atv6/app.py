from Senha import aleatorio_senha
comprimento = int(input("Digite o comprimento da senha desejada: "))
gerada = aleatorio_senha.gerar_senha(comprimento)

print(f"A senha gerada é: {gerada}")