#---Atualizando a nota de determinado aluno
import pandas as pd

#---Lendo a base de dados gerada em Python no formato xlxs
base_dados = pd.read_excel("Registro_Alunos.xlsx", engine="openpyxl")
print(base_dados.head(2))

nome_aluno = input("Digite o nome do aluno: ")
busca_aluno = base_dados.loc[base_dados['Nome'] == nome_aluno] #localiza valores de acordo uma label estabelecida, no caso o nome da coluna
indice = busca_aluno.index #procurando o índice do aluno que a nota será atualizada

#----Atualização da nota
base_dados.loc[indice, "Nota 1"] = 8
base_dados.loc[indice, "Nota 2"] = 9
#----Calculando a nova média
base_dados.loc[indice, "Média"] = (base_dados.loc[indice, "Nota 1"] + base_dados.loc[indice, "Nota 2"]) / 2

#---Mudando o Status do aluno caso ele esteja Aprovado
if (base_dados.loc[indice, "Média"][1] >= 6) and (base_dados.loc[indice, "Presença (%)"][1] >=50):
    base_dados.loc[indice, "Status"] = "Aprovado" #mudando o valor do status do aluno para Aprovado
    #----Concatenando a base original com a novo registro
    base_dados = pd.concat([base_dados, pd.DataFrame([base_dados.loc[indice, "Média"]],[base_dados.loc[indice, "Status"]])], ignore_index=True)
    #----"ignore_index = True" para evitar duplicação de índices e continuar a partir do último índice da base
else:
    base_dados.loc[indice, "Status"] = "Reprovado"
    base_dados = pd.concat([base_dados, pd.DataFrame([base_dados.loc[indice, "Média"]], [base_dados.loc[indice, "Status"]])], ignore_index=True)
    # "ignore_index = True" para evitar duplicação de índices e continuar a partir do último índice da base

#Convertendo a nova base para excel
base_dados.to_excel("Registro_Alunos_2.xlsx", sheet_name="Base-Dados", index=False, engine="openpyxl")
#"index = False" para não salvar a coluna de índices do DataFrame no arquivo excel.
print(base_dados.head(2))
