from imposto import impostos_renda

renda = input("Digite 'salario' para calcular o imposto de renda ou 'produto' para calcular o ICMS: ")

if renda == 'salario':
    salario = float(input("Digite o valor do salário: "))
    imposto_renda = impostos_renda.calcular_imposto_renda(salario)
    print(f"O imposto de renda é: R${imposto_renda:.2f}")
elif renda == 'produto':
    valor_produto = float(input("Digite o valor do produto: "))
    icms = impostos_renda.calcular_icms(valor_produto)
    print(f"O ICMS é: R${icms:.2f}")
else:
    print("Escolha inválida. Digite 'salario' ou 'produto'.")