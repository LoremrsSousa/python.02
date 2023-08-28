class Aluno:
    def __init__(self,nome, nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        print(f"A nota de {self.nome} é: ", (self.nota1 + self.nota2)/2 )


Notas = Aluno("Lorena" , 10, 9 )
Notas.calcular_media()
