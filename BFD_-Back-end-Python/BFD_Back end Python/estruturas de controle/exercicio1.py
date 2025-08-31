#Passo 1

IDADE_MINIMA = 18
idade_usuario = int(input("Qual sua idade? "))
if idade_usuario >= IDADE_MINIMA:
    print("O usuário é maior de idade.")
#Passo 2
elif idade_usuario<IDADE_MINIMA and idade_usuario>=16:
    print("O usuario é menor de idade e tem 16 ou 17 anos.")
#Passo 3
else:
    print("O usuário é menor de idade.")
        
    
    