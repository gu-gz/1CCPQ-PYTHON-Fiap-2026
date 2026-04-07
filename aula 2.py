
'''
import pandas

dados 1 = pandas .read_csv(filepath_on_buffer: 'dadosaula(2).txt', sep=' ', header = 0)
print(dados1)
'''

# csv:
import pandas

dados2 = pandas.read_csv('dadosaula(2).txt', sep=' ', header = 0)
print(dados2)

#xlsx
import pandas

dados3 = pandas.read_excel("DadosAula(2).xlsx", engine= "openpyxl")
print(dados3)