from conversor_unidades import conversao
oper = int(input("Digite oque você vai converter (1- celsius ,  2- fahrenheit): "))
num = int(input("Digite o número em celsius ou fahrenheit: "))

if oper == 1:
    fahr = conversao.fahrenheit(num)
    print(fahr)
elif oper == 2:
    cels = conversao.celsius(num)
    print(cels)