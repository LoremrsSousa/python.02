class Retangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        print((self.base * self.altura) / 2)


triangulo = Retangulo(10,20)
triangulo.calcular_area()
