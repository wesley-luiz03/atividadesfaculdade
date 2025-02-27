#O valor total da quantidade de prestações
qnt_prestacoes = int(input("Qual a quantidade total de prestações? "))

#O valor de quantas prestações foram pagas
prestacoes_pagas = int(input("Quantas prestações foram pagas? "))

#O valor em REAL da atual prestação
prestacao_atual = float(input("Qual o valor atual da prestação? R$"))

if prestacoes_pagas > qnt_prestacoes:
    print("Erro: O número de prestações pagas não pode ser maior que o número de prestações.")
else:
    prestacoes_apagar = qnt_prestacoes - prestacoes_pagas
    
    devedor = prestacoes_pagas * prestacao_atual

print (f"O valor devedor faltante é: {devedor:.2f}")
print (f"O valor de prestações faltante é: {prestacoes_apagar}")