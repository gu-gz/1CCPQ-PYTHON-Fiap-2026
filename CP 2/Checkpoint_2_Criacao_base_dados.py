#Checkpoint 2 - Modelagem Linear para Aprendizado de Máquina
#Elaboração de uma base de dados relacionada ao cadastro dos alunos de uma faculdade

#Alunos: Artur Souza Pereira - RM 570880
#Gustavo Gamba Zancopé - RM 569287
#Isabela Camargo Souza - RM569196
#Miguel Silvério de Avila - RM 568873
#Victor Vieira Galvão - RM 571483


from faker import Faker #blibioteca que gera dados fictícios
faker = Faker('pt_BR') #inicializando a função Faker e definindo o idioma
import random
import pandas as pd

#---Função para gerar os dados fictícios da base
def gerar_dados(quantidade_registros):
    registro_alunos = [] #lista de dados
    formas_ingresso = ["Vestibular interno", "ENEM", "Transferência"]
    cursos = ["Administração", "Análise e Desenvolvimento de Sistemas", "Biomedicina", "Ciências Contábeis", "Ciência da Computação",
    "Economia", "Jornalismo", "Marketing", "Publicidade e Propaganda", "Segurança da Informação", "Sistemas de Informação"]
    duracao_curso = {"Administração": 4, "Análise e Desenvolvimento de Sistemas": 2, "Biomedicina": 4, "Ciências Contábeis": 4,
    "Ciência da Computação": 4, "Economia": 4, "Jornalismo": 4,"Marketing": 4,"Publicidade e Propaganda": 4,"Segurança da Informação": 2,
    "Sistemas de Informação": 4}
    campus = ["Aclimação", "Paulista", "São Judas", "Campinas", "São José dos Campos", "Brotas"]

    for i in range(quantidade_registros):
        nota_1 = round(random.uniform(0, 10),2)  #gerar um número decimal aleatório entre 0 e 10 com 2 casas após a vírgula
        nota_2 = round(random.uniform(0, 10), 2)
        media = round((nota_1 + nota_2) / 2, 2)
        frequencia = faker.random_int(min=0, max=100)
        status = ''
        if media >= 6 and frequencia >=50:
            status = 'Aprovado'
        else:
            status = 'Reprovado'
        curso = random.choice(cursos)
        duracao = duracao_curso[curso] #pegando a duração específica do curso escolhido aleatoriamente
        semestre = duracao * 2 #quantidade de semestres do curso

        #---Adicionando as informações à lista de dados
        registro_alunos.append({
        'ID_aluno': i + 1,
        'Nome': faker.first_name() + " " + faker.last_name(), #para que o nome não venha com formas de tratamento (Dr, Sra)
        'Idade': faker.random_int(min=17, max=40),
        'Forma de ingresso': random.choice(formas_ingresso),
        'Curso': curso,
        'Campus': random.choice(campus),
        'Turno': random.choice(["Matutino", "Noturno"]),
        'Modalidade': random.choice(["Presencial", "Online"]),
        'Semestre': random.randint(1, semestre), #selecionar um número aleatório para o semestre que vá de 1 até o nº de semestres da duração do curso
        'Duração do curso': duracao,
        'Nota 1': nota_1,
        'Nota 2': nota_2,
        'Média': media,
        'Presença (%)': frequencia,
        'Status': status,
        'Bolsa de estudos': random.choice(["Sim", "Não"]),
        })
    return pd.DataFrame(registro_alunos) #transformando a lista em uma estrutura de dados organizada em linhas e colunas

#---Gerando os 150 registros fictícios:
base_dados = gerar_dados(200)

#---Exportando a base criada para o excel
base_dados.to_excel("Registro_Alunos.xlsx", sheet_name="Base-Dados", index=False, engine="openpyxl")
#---"index = False" para não salvar a coluna de índices do DataFrame no arquivo excel.


