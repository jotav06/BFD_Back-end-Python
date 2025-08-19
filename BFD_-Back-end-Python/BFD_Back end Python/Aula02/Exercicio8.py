import datetime

hora_atual = datetime.datetime.now()
nome_usuario = input("Digite seu nome: ")

print(f'Olá , {nome_usuario}! Agora são {hora_atual.strftime("%H:%M")} horas')