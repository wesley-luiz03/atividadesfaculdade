# Esse é um código para calcular todas as minhas notas na UniFafire

# Aqui vou colocar todas as notas do 1ª Semestre de todas as matérias

# Aqui estou verificando se a nota que vou colocar está entre 0 e 10, caso não, o valor será retornado.
def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Por favor, digite um valor entre 0 e 10.")
        except ValueError:
            print("Valor Inválido. Digite um número.")

# Aqui estou calculando a média da matéria de Fundamento da Programação
fund_n1 = obter_nota ("Digite a nota da 1ª prova de Fundamentos: ")
fund_n2 = obter_nota ("Digite a nota da 2ª prova de Fundamentos: ")
media_de_fundamentos = (fund_n1 + fund_n2) / 2

print(f"Média de fundamentos: {media_de_fundamentos: .2f}")


# Aqui estou calculando a média da matéria de Enganharia de Software
eng_n1 = obter_nota ("Digite a nota da 1ª prova de Engenharia de software: ")
eng_n2 = obter_nota ("Digite a nota da 2ª prova de Enganharia de software: ")
media_de_enganharia = (eng_n1 + eng_n2) / 2

print(f"Média de Engenharia de Software: {media_de_enganharia: .2f}")


# Aqui estou calculando a média da matéria de Gestão de Projetos
gestao_n1 = obter_nota ("Digite a nota da 1ª prova de Gestão de Projetos: ")
gestao_n2 = obter_nota ("Digite a nota da 2ª prova de Gestão de Projetos: ")
media_de_gestao = (gestao_n1 + gestao_n2) / 2

print(f"A média de Gestão de projetos é: {media_de_gestao: .2f}")


# Aqui estou calculando a média da matéria de Matemática
mat_n1 = obter_nota ("Digite a nota da 1ª prova de Matemática: ")
mat_n2 = obter_nota ("Digite a nota da 2ª prova de Matemática: ")
media_de_mat = (mat_n1 + mat_n2) / 2

print(f"A média de Matemática é: {media_de_mat: .2f}")


# Aqui estou calculando a média de Computação
comp_n1 = obter_nota ("Digite a nota da 1ª prova de Introdução a Computação: ")
comp_n2 = obter_nota ("Digite a nota da 2ª prova de Introdução a Computação: ")
media_de_comp = (comp_n1 + comp_n2) / 2

print(f"A média de Introdução a Computação é: {media_de_comp: .2f}")


# Aqui estou calculando a média de Projeto Social
projeto_n1 = obter_nota ("Digite a nota da 1ª prova de Projeto de Integração Social: ")
projeto_n2 = obter_nota ("Digite a nota da 1ª prova de Projeto de Integração Social: ")
media_de_projeto = (projeto_n1 + projeto_n2) / 2

print(f"A média de Projeto de Integração Social: {media_de_projeto: .2f}")

