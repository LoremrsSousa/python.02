import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    Senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return Senha
