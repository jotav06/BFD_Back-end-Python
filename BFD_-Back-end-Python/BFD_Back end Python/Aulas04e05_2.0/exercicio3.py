salario_hora = float(input("Quanto você recebe por hora trabalhada? R$"))
hora_trabalhada = float(input("Quantas horas você trabalha por mês? "))
salario_mes = salario_hora * hora_trabalhada

print(F"Seu salário mensal é de R${salario_mes:.2f}")
