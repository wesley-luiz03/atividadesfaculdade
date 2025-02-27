#Solicitando a quantidade de votos
brancos = int(input("Quantos desses eleitores votaram em branco? "))
nulos = int(input("Quantos desses eleitores votaram nulo? "))
validos = int(input("Quantos desses votos foram válidos? "))

#Calculando o total de eleitores
total_eleitores = brancos + nulos + validos

#Verificando se há eleitores e calculando, evitando a divisão por 0
if total_eleitores == 0:
    print("Nenhum voto foi registrado.")
else:
    calc_votos_brancos = (brancos / total_eleitores) * 100
    calc_votos_nulos = (nulos / total_eleitores) * 100
    calc_votos_validos = (validos / total_eleitores) * 100

#Imprimindo todos os percentuais de cada voto
print(f"O percentual de votos brancos é: {calc_votos_brancos:.2f}%")
print(f"O percentual de votos nulos é: {calc_votos_nulos:.2f}%")
print(f"O percentual de votos validos é: {calc_votos_validos:.2f}%")

