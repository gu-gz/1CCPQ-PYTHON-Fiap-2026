from collections import Counter

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

#criando a base de dados:
dados = [14]*6 + [15] *12 + [16]*9 + [17]*3
print(dados)
# print(type(dados))

#Frequencia absoluta (fi):
fi = pd.Series(Counter(dados)).sort_index()
print(fi)

#Frequencia absoluta acumulada (fia):
fia = fi.cumsum()
print(fia)

# Frequência Relativa (fr):
fr = 100 * fi / fi.sum()
print(fr)

# Frequência Relativa Acumulada (fra):
fra = fr.cumsum()
print(fra)

#montando a tabela:
tabela = pd.DataFrame({
    'Frequencia_Absoluta': fi,
    'Frequencia_Absoluta_Acumulada':fia,
    'Frequencia_Relativa': fr,
    'Frequencia_Relativa_Acumulada': fra
})
print(tabela)

#nome "total: na ultima linha:
tabela.loc['Total'] = [
    fi.sum(),
    '-',
    fr.sum(),
    '-'
]

#Tabela de Distrubuicao de Frequencias:
print(tabela)

# Gráficos para Variáveis Qualitativas
# Setores
from collections import Counter
import matplotlib.pyplot as plt

dados1 = ["Sim"] * 20 + ["Não"] * 45
print(dados1)

respostas1 = Counter(dados1)
print(respostas1)

plt.pie(list(respostas1.values()),
        labels=list(respostas1.keys()),
        autopct='%1.2f%%',
        colors=["red", "blue"])

plt.title("Respostas Entrevista")
plt.legend(list(respostas1.keys()), loc="upper right")
plt.show()