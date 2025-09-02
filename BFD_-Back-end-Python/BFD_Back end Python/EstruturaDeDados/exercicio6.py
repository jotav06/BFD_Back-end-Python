arquivos = ("documentos.pdf", "foto.jpg", "relatorio.pdf", "planilha.xlsx")
qtd_pdf = sum(1 for arq in arquivos if arq.endswith(".pdf"))
print(arquivos)
print(f"Quantidade de arquivos .pdf: {qtd_pdf}")
