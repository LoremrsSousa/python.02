class Surpresa:
    def __init__(self,tipo,nome,cor,idaderecom,material,caracte,preco,fabric,dimen,peso):
        self.tipo = tipo
        self.nome = nome
        self.cor = cor
        self.idaderecom = idaderecom
        self.material = material
        self.caracte = caracte
        self.preco = preco
        self.fabric = fabric
        self.dimen = dimen
        self.peso = peso
    def Parado (self):
            print("Imovéeel..")


Kinderr1 = Surpresa("avião","lula","vermelho",3,"plástico","helicóptero com adesivo",2.99,"China","1cm",0.5)
print(Kinderr1.preco)
Kinderr1.Parado()