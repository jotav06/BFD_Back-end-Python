vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]
total_vendas = sum(vendas_semana)
menor_venda = min(vendas_semana)
dia_menor = vendas_semana.index(menor_venda) + 1

print(f"O total de vendas na semana foi de r${total_vendas}.")
print(f"O dia que vendeu menos foi no dia {dia_menor}, com total de vendas de r${menor_venda}.")