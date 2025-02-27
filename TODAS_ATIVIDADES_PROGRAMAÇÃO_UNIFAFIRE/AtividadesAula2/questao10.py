#Solicitando o tempo de duração do evento
tempo_segundos = int(input("Digite o tempo de duração do evento em segundos: "))

#Calculando horas, minutos e segundos
horas = tempo_segundos // 3600 #Divide o total de segundos por 3600 para obter horas
minutos = (tempo_segundos % 3600) // 60 #Pega o restante dos segundos e divide por 60 para dar os minutos
segundos = tempo_segundos % 60 #Pega o restante de segundos após retirar horas e minutos

#Exibe o resultado formatado
print(f"O evento teve duração de {horas} horas, {minutos} minutos e {segundos} seguhndos.")
