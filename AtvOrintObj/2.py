class Cachorro:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def Latir (self):
        print( "Woof!")


Pitbull = Cachorro("Nicole", 5)
Pitbull.Latir()