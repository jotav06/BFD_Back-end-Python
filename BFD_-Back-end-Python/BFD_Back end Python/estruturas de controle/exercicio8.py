cor = input("Digite a cor do semáforo (verde, amarelo ou vermelho): ")

match cor:
    case "verde":
        print("Você pode seguir. Siga com atenção.")
    case "amarelo":
        print("Atenção! Prepare-se para parar.")
    case "vermelho":
        print("Pare! Aguardando o sinal abrir.")
    case _:
        print("Sinal inválido! Por favor, digite uma cor válida (verde, amarelo ou vermelho).")