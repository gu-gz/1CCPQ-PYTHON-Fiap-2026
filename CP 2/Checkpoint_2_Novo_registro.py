import pandas as pd

#Lendo a base de dados gerada em Python no formato xlxs
base_dados = pd.read_excel("Registro_Alunos.xlsx", engine="openpyxl")

novo_registro = {
'ID_aluno': len(base_dados) + 1,
'Nome': "Larissa",
'Idade': 25,
'Forma de ingresso': "ENEM",
'Curso': "Ciência da Computação",
'Campus': "Aclimação",
'Turno': "Noturno",
'Modalidade': "Presencial",
'Semestre': 5,
'Duração do curso': 4,
'Nota 1': 8,
'Nota 2': 4,
'Média': 6,
'Presença (%)': 60,
'Status': "Aprovado",
'Bolsa de estudos': "Não"
}

#concatenando a base original com a novo registro
base_dados = pd.concat([base_dados, pd.DataFrame([novo_registro])], ignore_index=True)
#"ignore_index = True" para evitar duplicação de índices e continuar a partir do último índice da base

#convertendo a nova base para excel
base_dados.to_excel("Registro_Alunos_1.xlsx", sheet_name="Base-Dados", index=False, engine="openpyxl")
#"index = False" para não salvar a coluna de índices do DataFrame no arquivo excel.
print(base_dados)
