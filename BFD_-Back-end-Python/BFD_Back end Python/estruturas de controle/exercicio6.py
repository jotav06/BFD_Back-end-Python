nota = int(input("Digite uma nota entre 1 e 5: "))

match nota:
    case 1:
        print("Nota muito abaixo do esperado")
    case 2:
        print("Nota baixa, mas pode melhorar")
    case 3:
        print("Continue se esforçando")
    case 4:
        print("Muito bom, quase lá")
    case 5:
        print("Excelente, parabéns!")
    case _:
        print("Nota inválida. digite uma nota entre 1 e 5.")
        