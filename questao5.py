#Pedindo a quantidade de eleitores que votaram em branco
brancos = int(input("Quantos desses eleitores votaram em branco? "))

#Pedindo a quantidade de eleitores que votaram em nulo
nulos = int(input("Quantos desses eleitores votaram nulo? "))

#Pedindo a quantidade de eleitores que votaram válidos
validos = int(input("Quantos desses votos foram válidos? "))

#A soma de todos os votos acima, totalizando a quantidade de eleitores
total_eleitores = (brancos + nulos + validos)

#Calculo de votos em branco,que é, a quantidade de votos brancos, dividido pelo total e multiplicado por 100
calc_votos_brancos = (brancos / total_eleitores * 100)

#Calculo de votos nulos com a mesma base
calc_votos_nulos = (nulos / total_eleitores * 100)

#Calculo de votos válidos com a mesma base
calc_votos_validos = (validos / total_eleitores * 100)

#Imprimindo todos os porcentuais com calculo
print(f"O percentual de votos brancos é: {calc_votos_brancos: .2f}%")
print(f"O percentual de votos nulos é: {calc_votos_nulos: .2f}%")
print(f"O percentual de votos validos é: {calc_votos_validos: .2f}%")

