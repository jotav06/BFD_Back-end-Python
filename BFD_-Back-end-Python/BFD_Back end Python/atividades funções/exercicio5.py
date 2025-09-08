def calcular_media(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(calcular_media(8.5, 7.0, 6.0, 9.5, 10.0))