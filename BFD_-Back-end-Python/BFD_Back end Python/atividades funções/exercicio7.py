def cadastro_usuario(nome, email, **kwargs):
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
        
cadastro_usuario(nome="Victor", email="victor0602silva@gmail.com", idade=26, cidade="Recife")
print(cadastro_usuario)
