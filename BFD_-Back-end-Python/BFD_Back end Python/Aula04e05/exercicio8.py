saldo_bancario = 1000
print(f"Saldo Inicial: R${saldo_bancario}")
deposito = float(input("Digite um valor para depósito: R$"))
saldo_bancario+=deposito
print (f"Novo saldo após deposito: R${saldo_bancario}")
saque = float(input("Digite um valor para saque: R$"))
saldo_bancario-=saque
print (f"Novo saldo após saque: R${saldo_bancario}")
juros = float(input("Digite a taxa de juros do banco (ex. 1.05 para 5%):"))
saldo_bancario*=juros
print(f"Valor após aplicação de juros: R${saldo_bancario}")