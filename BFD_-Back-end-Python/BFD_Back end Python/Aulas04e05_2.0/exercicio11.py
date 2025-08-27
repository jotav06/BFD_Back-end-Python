km_percorrido = float(input("Quantos km foram percorridos? "))
dias_alugado = float(input("Quantos dias o carro ficou alugado? "))
total = (km_percorrido * 0.15) + (dias_alugado * 60.00)

print (f"O valor a ser pago é de R${total:.2f}")