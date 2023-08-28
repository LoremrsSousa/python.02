#4

def voto(a,b):
    var = a - b
    if var >= 18:
        print('Ovoto é obrigatorio')
    elif var == 16 or var ==17:
        print('O vota é opicional')
    else:
        print('Voto negado')
