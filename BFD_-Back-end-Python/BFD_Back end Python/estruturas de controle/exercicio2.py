#Passo 1
NOTA_MINIMA = 7.0
nota_usuario = float(input("Qual sua nota? "))

if nota_usuario >= NOTA_MINIMA:
    print("Aprovado")
#Passo 2
elif nota_usuario >= 5.0:
    print("Você tirou nota baixa, mas dá para recuperar. ")
#Passo 3
else:
    print("Reprovado")