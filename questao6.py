#O valor total da quantidade de prestações
qnt_prestacoes = int(input("Qual a quantidade total de prestações? "))

#O valor de quantas prestações foram pagas
prestacoes_pagas = int(input("Quantas prestações foram pagas? "))

#O valor em REAL da atual prestação
prestacao_atual = float(input("Qual o valor atual da prestação? R$"))

#Calculando a quantidade de prestações a pagar
prestacoes_apagar = (qnt_prestacoes - prestacoes_pagas)

#Calculando qual o valor em REAL que ainda deve
devedor = (prestacoes_apagar * prestacao_atual)

#Imprimindo o valor que ele ainda deve
print (f"O valor devedor faltante é: {devedor: .2f}")

#Imprimindo o valor restante de prestações
print (f"O valor de prestações faltante é: {prestacoes_apagar}")