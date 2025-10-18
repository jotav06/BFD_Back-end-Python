from datetime import datetime, timedelta

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False
        self.data_emprestimo = None
        self.data_devolucao = None

    def __str__(self):
        return self.titulo

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def autenticar(self):
        print(f"[Autenticação] Usuário {self.nome} autenticado com sucesso.")
        return True

    def emprestar_livro(self, livro):
        if self.autenticar():
            if self.tem_livros_atrasados():
                self.notificar_atraso()
            if not livro.emprestado:
                livro.emprestado = True
                livro.data_emprestimo = datetime.now()
                self.livros_emprestados.append(livro)
                print(f"[Empréstimo] Livro '{livro}' emprestado para {self.nome}.")
            else:
                print(f"[Erro] Livro '{livro}' já está emprestado.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            multa = self.calcular_multa(livro)
            livro.emprestado = False
            livro.data_devolucao = datetime.now()
            self.livros_emprestados.remove(livro)
            print(f"[Devolução] Livro '{livro}' devolvido.")
            if multa > 0:
                self.processar_pagamento(multa)
        else:
            print(f"[Erro] Livro '{livro}' não foi emprestado por {self.nome}.")

    def calcular_multa(self, livro):
        dias_emprestimo = (datetime.now() - livro.data_emprestimo).days
        dias_permitidos = 7
        if dias_emprestimo > dias_permitidos:
            multa = (dias_emprestimo - dias_permitidos) * 2  # R$2 por dia de atraso
            print(f"[Multa] Multa de R${multa} calculada por atraso.")
            return multa
        return 0

    def tem_livros_atrasados(self):
        for livro in self.livros_emprestados:
            if (datetime.now() - livro.data_emprestimo).days > 7:
                return True
        return False

    def notificar_atraso(self):
        print(f"[Aviso] {self.nome}, você possui livros com devolução em atraso!")

    def processar_pagamento(self, valor):
        pagamento = SistemaPagamento()
        pagamento.realizar_pagamento(self.nome, valor)

class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome

    def adicionar_livro(self, biblioteca, livro):
        biblioteca.acervo.append(livro)
        print(f"[Bibliotecário] Livro '{livro}' adicionado ao acervo.")

    def remover_livro(self, biblioteca, livro):
        if livro in biblioteca.acervo:
            biblioteca.acervo.remove(livro)
            print(f"[Bibliotecário] Livro '{livro}' removido do acervo.")
        else:
            print(f"[Erro] Livro '{livro}' não encontrado no acervo.")

class SistemaPagamento:
    def realizar_pagamento(self, usuario, valor):
        print(f"[Pagamento] Pagamento de R${valor} processado para {usuario}.")

class Biblioteca:
    def __init__(self):
        self.acervo = []

# ================= EXEMPLO DE USO ====================
if __name__ == "__main__":
    biblioteca = Biblioteca()
    bibliotecario = Bibliotecario("Ana")
    usuario = Usuario("Victor")

    livro1 = Livro("Percy Jackson e o Ladrão de Raios")
    livro2 = Livro("Harry Potter e a Pedra Filosofal")

    bibliotecario.adicionar_livro(biblioteca, livro1)
    bibliotecario.adicionar_livro(biblioteca, livro2)

    usuario.emprestar_livro(livro1)

    # Simula atraso de 10 dias
    livro1.data_emprestimo -= timedelta(days=10)

    usuario.devolver_livro(livro1)
