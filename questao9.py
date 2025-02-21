#Preço da mercadoria de Abril
preco_abril = float(input("Digite o preço de uma mercadoria de Abril: "))

#Preço da mercadoria de Maio
preco_maio = float(input("Digite o preço de uma mercadoria de Maio: "))

#Calculo da inflação entre os produtos de Abril e Maio X 100
calc_inflacao = (preco_abril / preco_maio * 100)

#Imprimindo...
print(f"O valor total inflacionado é de: {calc_inflacao: .2f} %")
