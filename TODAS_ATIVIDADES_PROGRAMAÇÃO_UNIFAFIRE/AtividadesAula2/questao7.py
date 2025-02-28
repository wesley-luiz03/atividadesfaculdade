#Pedindo KM Inicial, final, litros consumidos e preço
km_inicial = int(input("Qual a quantidade de KM inicial? "))
km_final = int(input("Qual a quantidade de KM final? "))
litro_consumidos = float(input("Quantos litros foram consumidos? "))
preco_litro = float(input("Qual o preço do litro do combustível? R$"))

#Calculos
distancia = km_final - km_inicial #Calculando a distância em KM
valor_gasto = litro_consumidos * preco_litro #Calculando os gatos de litros
consumo_carro = distancia / litro_consumidos #Calculando o consumo do carro

#Imprimindo relatório da viagem
print(f"\nRelatório da Viagem:")
print(f"- Distância percorrida: {distancia:.2f} km")
print(f"- Valor total de gastos: R$ {valor_gasto:.2f}")
print(f"- Consumo do carro: {consumo_carro:.2f} km/l")

