#Quantidade de KM inicial da viagem
km_inicial = int(input("Qual a quantidade de KM inicial? "))

#Quantidade de KM final da viagem
km_final = int(input("Qual a quantidade de KM final?"))

#Quantidade de litros que foram consumidos durante a viagem
l_consumidos = int(input("Quantos litros foram consumidos? "))

#Quantidade, em REAL, do preço do litro do combustível
preço_l = float(input("Qual o preço do litro do combustível? "))


#CALCULOS
#Calculos para resultar a distância total
distancia = (km_inicial - km_final * (-1))

#Calculo para saber o gasto total 
valor_gasto = (l_consumidos + preço_l)

#Calculo para saber o consumo total do carro em KM
consumo_carro = (distancia + 1)

#Imprimindo
print(f"A distância percorrida foi de: {distancia: .2f}")
print(f"O valor total de gastos foi de: {valor_gasto} R$")
print(f"O consumo total do carro foi de: {consumo_carro: .2f}")

