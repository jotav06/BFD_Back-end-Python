vendedores = ['João', 'Maria', 'Pedro', 'Ana']

print("Ranking de Vendedores:")
for posicao, nome in enumerate(vendedores, start=1):
    print(f"{posicao}. {nome}")