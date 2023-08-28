from Geometria import formas

oper = str(input("Digite sua operação (quadrado , círculo):  "))

if oper == 'quadrado':
    lado = int(input("Digite o valor do lado: "))
    areaq = formas.area_quadrado(lado)
    print(areaq)
elif oper == "círculo":
    raio = int(input("Digite o número do raio: "))
    areac = formas.area_circulo(raio)
    print(areac)
else:
    print("Não foi possível calcular")