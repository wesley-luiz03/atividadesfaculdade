#Pedindo o valor do salário atual do funcionário
salario = float(input("Digite o salário atual do funcionário: "))

#Pedindo o valor que o empregado que dar de reajuste para o funcionário
percentual = float(input("Digite o percentual de reajuste (sem %): "))
 
#Calculo para saber o valor com o reajuste
novo_salario = salario * (1 + percentual / 100)

#Imprimindo o valor final com reajuste e em R$
print(f"O novo salário com reajuste será: R${novo_salario:.2f}")