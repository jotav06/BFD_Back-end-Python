nomes = ['Teclado', 'Mouse']
precos = [250, 120]
estoques = [10, 25]

produtos = list(zip(nomes, precos, estoques))

print("Produtos cadastrados:")
for nome, preco, estoque in produtos:
    print(f"Nome: {nome}, Preço: R$ {preco}, Estoque: {estoque} unidades")