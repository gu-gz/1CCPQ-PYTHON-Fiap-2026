#---Consultando os alunos aprovados:
import pandas as pd

#---Lendo a base de dados gerada em Python no formato xlxs
base_dados = pd.read_excel("Registro_Alunos.xlsx", engine="openpyxl")

#Filtrando os alunos com status de Aprovado
aprovados = base_dados[base_dados['Status'] == 'Aprovado']
print(aprovados)