#Import da data atual
from datetime import date

#Solicitando o ano e mês de nascimento
ano_nasc = int(input("Digite o ano do seu nascimento: "))
mes_nasc = int(input("Digite o mês do seu nascimento (1-12): "))

#Definindo do ano e o mêS atual pelo import
hoje = date.today()
ano_atual = hoje.year
mes_atual = hoje.month

#Calculo da idade do usuário
idade = ano_atual - ano_nasc

#Explicando que SE o mês atual for maior que o mês de nasc, subtrai com -1
if mes_atual < mes_nasc:
    idade -= 1

#Imprimindo...    
print(f"Você tem {idade} anos.")

