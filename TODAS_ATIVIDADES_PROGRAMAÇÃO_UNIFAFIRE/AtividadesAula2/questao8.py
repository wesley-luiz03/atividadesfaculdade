km_inicial = float(input("Digite a marcação do hodômetro no início do dia (KM): "))

km_final = float(input("Digite a marcação do hodômetro no final do dia (KM): "))

litros_gastos = float(input("Digite a quantidade de litros de combustível gastos: "))

total_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))

preco_combustivel = 2.59

distancia = km_final - km_inicial

consumo = distancia / litros_gastos

gasto_combustivel = litros_gastos * preco_combustivel

lucro_liquido = total_recebido - gasto_combustivel

print("\n--- RELATÓRIO DO DIA ---")
print(f"Distância percorrida: {distancia:.2f} Km")
print(f"Consumo médio do carro: {consumo:.2f} Km/L")
print(f"Gasto total com combustível: R$ {gasto_combustivel:.2f}")
print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")