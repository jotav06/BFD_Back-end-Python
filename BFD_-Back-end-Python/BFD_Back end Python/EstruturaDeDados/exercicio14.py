clientes = ['João', 'Maria', 'José']
saldos = [1500, 2500, 800]

print("Clientes e seus saldos:")
for i, (cliente, saldo) in enumerate(zip(clientes, saldos), start=1):
    print(f"{i}. {cliente}: R$ {saldo}")