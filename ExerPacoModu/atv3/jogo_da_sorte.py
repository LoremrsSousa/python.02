from Jogo import adivinha

print("JOGO DE ADIVINHAÇÃO")
sortear =adivinha.jogo_adivinhar()

while True:
        palpite = int(input("Digite o seu número: "))
        tentativa =+1

        if palpite < sortear:
            print("É maior.")
        elif palpite > sortear:
            print("É menor.")
        else:
            print(f"Parabéns! Você acertou o número {sortear} em {tentativa} tentativas.")
            break
