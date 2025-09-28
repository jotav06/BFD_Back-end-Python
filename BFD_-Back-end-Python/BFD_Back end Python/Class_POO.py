class Jogo:
    def __init__(self, nome, genero, ano_lancamento):
        self.nome = nome
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        
        
    def jogar(self):
        print(f"Eu irei jogar {self.nome}, que é um jogo de {self.genero} lançado no ano de {self.ano_lancamento}!")
        
jogo1 = Jogo("Age of Mythology", "Estratégia", 2002)
jogo2 = Jogo("Top gear", "Corrida", 1992)
jogo3 = Jogo("Call of Duty", "Tiro", 2003)
jogo4 = Jogo("FIFA", "Esporte", 1993)

jogo1.jogar()
jogo2.jogar()
jogo3.jogar()
jogo4.jogar()
