#Exercicio igual ao 3.

def vogais(palavra):
    
    count = 0
    for letra in palavra:
        if letra.lower() in 'aeiou':
            count += 1
    return count
palavra = input("Digite uma palavra: ")

print(vogais(palavra))