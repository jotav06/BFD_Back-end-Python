status_pedido = input("Digite o status atual do seu pedido (recebido, em preparação, em entrega, entregue): ")
match status_pedido:
    case "recebido":
        print("Seu pedido foi recebido e está em processamento.")
    case "em preparação":
        print("Seu pedido está sendo preparado.")
    case "em entrega":
        print("Seu pedido está a caminho.")
    case "entregue":
        print("Seu pedido foi entregue.")
    case _:
        print("Status inválido. Tente novamente.")
        