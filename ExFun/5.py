from modulo import  ficha
nomej = input('o nome do jogador e a camisa que usa: ')
gol =  input('digite quais gols ele marcou: ')


if gol.isnumeric():
    ficha(nomej, int(gol))
else:
    ficha(nomej)