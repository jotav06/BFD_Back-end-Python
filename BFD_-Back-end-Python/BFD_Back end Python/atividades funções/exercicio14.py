nomes = ['João', 'Maria', 'Pedro']
sobrenomes = ['Silva', 'Santos', 'rocha']

nomes_completos = list(map(lambda x,y: x + ' ' + y, nomes, sobrenomes))
print(nomes_completos)
