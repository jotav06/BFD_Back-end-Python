saldo_bancario = 1000
deposito = float(input("Insira o valor de depósito: R$"))
saque = float (input("Isnsira o valor de saque: R$"))
juros = float (input("Qual a taxa de juros do banco (exemplo 1.05 para 5%)? "))

saldo_bancario+=deposito
saldo_bancario-=saque
saldo_bancario*=juros

print(f"saldo final: R${saldo_bancario:.2f}")
