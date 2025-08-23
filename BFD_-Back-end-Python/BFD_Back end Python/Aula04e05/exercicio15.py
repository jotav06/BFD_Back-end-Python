senha = "Python123"
senha_valida = (senha !="" and len(senha)>8 and senha == "Python123" and senha != "12345")
#O len(senha)>8 eu tive que dar uma pesquisada para saber como definir um numero minimo de caracteres

print (f"A senha é válida? {senha_valida}")