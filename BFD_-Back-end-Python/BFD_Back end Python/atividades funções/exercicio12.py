precos = [101, 120, 50, 250, 92, 30, 400, 5]

produtos_filtrados = list(filter(lambda x: x>100, precos))
print(produtos_filtrados)
