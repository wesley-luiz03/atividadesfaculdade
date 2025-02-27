#Quantidade de KM inicial da viagem
km_inicial = int(input("Qual a quantidade de KM inicial? "))

#Quantidade de KM final da viagem
km_final = int(input("Qual a quantidade de KM final? "))

#Quantidade de litros que foram consumidos durante a viagem
litro_consumidos = float(input("Quantos litros foram consumidos? "))

#Quantidade, em REAL, do preço do litro do combustível
preco_litro = float(input("Qual o preço do litro do combustível? R$"))

#Calculos da distância total percorrida
distancia = km_final - km_inicial

#Calculo para saber o gasto total 
valor_gasto = litro_consumidos * preco_litro

#Calculo para saber o consumo total do carro em KM
consumo_carro = distancia / litro_consumidos

#Imprimindo
print(f"\nRelatório da Viagem:")
print(f"- Distância percorrida: {distancia:.2f} km")
print(f"- Valor total de gastos: R$ {valor_gasto:.2f}")
print(f"- Consumo do carro: {consumo_carro:.2f} km/l")

