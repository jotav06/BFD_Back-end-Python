def soma(a, b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao(a,b):
    return a/b
try:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    operacao = input("digite a operação desejada (+, -, *, /): ")
    if operacao == "+":
        resultado = soma(num1, num2)
        print(f"O resultado é: {resultado}")
    elif operacao == "-":
        resultado = subtracao(num1, num2)
        print(f"O resultado é: {resultado}")
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
        print(f"O resultado é: {resultado}")
    elif operacao == "/":
        if num2 == 0:
            raise ZeroDivisionError
        resultado = divisao(num1, num2)
        print(f"O resultado é: {resultado}")
    else:
        print("Erro: operação invalida")
except ValueError:
    print("Erro: valor invalido")
except ZeroDivisionError:
    print("Erro: divisão por zero")
finally:
    print("Saindo...")
    
            
    