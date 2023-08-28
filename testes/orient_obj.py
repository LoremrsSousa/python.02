#classe é representação abstrata do objeto
#metódos = função
#propriedades = caracteristicas -> atribui objeto

#método de construção
class Carro:
    def __init__(self, nome,cor,ano):
        self.nome = nome
        self.cor = cor
        self.ano = ano


Fusca = Carro('Fusca', 'Azul', 1965)
print("O nome do carro é: ", Fusca.nome)