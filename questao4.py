#Pedindo o valor do salário atual do funcionário
salario = int(input("Me diga o valor do salário atual do funcionário: "))

#Pedindo o valor que o empregado que dar de reajuste para o funcionário
reajuste = int(input("Me diga o valor do reajuste que vai ser adicionada ao salário: ")) / 100 + 1
 
#Calculo para saber o valor com o reajuste
calc_salarioatual = (reajuste * salario)

#Imprimindo o valor final com reajuste e em R$
print(f"O valor do final, com reajuste, ficou: R${calc_salarioatual:.2f}")