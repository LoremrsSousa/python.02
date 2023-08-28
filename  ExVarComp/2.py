biblioteca = {
    "Ação": ["Velozes e Furiosos", "Vingadores: Ultimato", "Missão: Impossível"],
    "Comédia": ["Se Beber, Não Case!", "Minha mãe é uma peça", "Debi & Loide"],
    "Drama": ["Um ninho para dois", "Clube da Luta", "O informante"],
    "Romance": ["Barraca do beijo", "Titanic", "A dama e o vagabundo"],
    "Documentário": ["Professor polvo", "Dahmer", "O golpista do tinder"],
    "Suspense": ["Resgate", "Corra!", "Truque de mestre"],
    "Terror": ["O Exorcista", "O Iluminado", "Invocação do Mal"],
    "Ficção científica": ["Blade Runner 2049", "Interestelar", "Matrix"]
}

genero = input("Digite o gênero para ver as indicações de filmes: ")

if genero in biblioteca:
    filmes = biblioteca[genero]
    print("Indicações de filmes do gênero", genero + ":")
    for filme in filmes:
        print(filme)