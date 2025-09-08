def atualizacao_perfil(perfil, **kwargs):
    for chave, valor in kwargs.items():
        perfil[chave] = valor
    return perfil
    
perfil = {'nome': 'João', 'idade': 30}
print(atualizacao_perfil(perfil , idade=26 , cidade='Recife'))

