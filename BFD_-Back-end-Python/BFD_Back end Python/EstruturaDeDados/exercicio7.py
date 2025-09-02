catalogo = {'Mouse Gamer': [150.00, 50]}

catalogo['Teclado Mecânico'] = [450.00, 30]

print("Catálogo de Produtos:")
for produto in catalogo:
    print("Nome:", produto)
    print("Preço:", catalogo[produto][0])
    print("Estoque:", catalogo[produto][1])
    print()  
