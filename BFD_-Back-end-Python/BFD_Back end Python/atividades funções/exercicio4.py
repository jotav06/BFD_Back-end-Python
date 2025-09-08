def juntar_strings(*args):
    resultado = ''
    for string in args:
        resultado += string
    return resultado


print(juntar_strings("O", " ", "céu"," ", "é", " ", "azul"))