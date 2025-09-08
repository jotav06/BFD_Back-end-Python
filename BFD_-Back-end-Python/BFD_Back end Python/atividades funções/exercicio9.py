def buscador_livros(titulo, **kwargs):
    print(f"titulo: {titulo}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

buscador_livros("Harry Potter", autor="J.K. Rowling", ano=1997, genero="Fantasia")

           