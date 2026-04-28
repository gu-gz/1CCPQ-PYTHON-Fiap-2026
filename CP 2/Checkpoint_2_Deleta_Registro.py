#Apagando um reistro de um aluno que cancelou a matrícula
import pandas as pd

#---Lendo a base de dados gerada em Python no formato xlxs
base_dados = pd.read_excel("Registro_Alunos.xlsx", engine="openpyxl")
print(base_dados.head(4))

nome_aluno = input("Digite o nome do aluno: ")
registro_aluno = base_dados.loc[base_dados["Nome"] == nome_aluno]#localiza os valores de acordo uma label estabelecida, no caso o nome da coluna
indice_exlusao = registro_aluno.index

base_dados = base_dados.drop(indice_exlusao) #drop para remover o índice específico da base de dados
base_dados["ID_aluno"] = range(1, len(base_dados) + 1) #atualizando a coluna de ID dos alunos

#convertendo a nova base para excel
base_dados.to_excel("Registro_Alunos_3.xlsx", sheet_name="Base-Dados", index=False, engine="openpyxl")
#"index = False" para não salvar a coluna de índices do DataFrame no arquivo excel.

#---Lendo a base de dados gerada em Python no formato xlxs
base_dados = pd.read_excel("Registro_Alunos_3.xlsx", engine="openpyxl")
print(base_dados.head(4))
