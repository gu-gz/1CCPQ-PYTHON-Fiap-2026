# Função COM PARAMETRO SEM RETORNO
def boas_vindas (nome):
    print(f"olá, {nome}!! Seja bem-vindo!")

nome_digitado = input("digite seu nome: ")
boas_vindas(nome_digitado)

#FUNCAO COM PARAM. COM RETORNO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(1, 2)
print(resultado_soma)
