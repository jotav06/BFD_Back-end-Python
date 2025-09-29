#Passo 1 - criar a classe
class Personagem:
    def __init__(self, nome):
        self._nome = nome
        self._hp = 100  

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_hp(self):
        return self._hp

    def dano(self, valor):
        self._hp -= valor
        if self._hp < 0:
            self._hp = 0

    def cura(self, valor):
        self._hp += valor
        if self._hp > 100:
            self._hp = 100

# Passo 2 - programa principal
personagem = Personagem("Herói")
print("Nome:", personagem.get_nome())
print("HP inicial:", personagem.get_hp())

personagem.dano(30)
print("HP após dano:", personagem.get_hp())

personagem.cura(50)
print("HP após cura:", personagem.get_hp())

personagem.set_nome("João")
print("Novo nome:", personagem.get_nome())
