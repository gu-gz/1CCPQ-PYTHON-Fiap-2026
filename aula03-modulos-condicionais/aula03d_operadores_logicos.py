# Lógica E (and)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa!")

#logica OU (or)

logica_ou = False or True or False
print(logica_ou)

#operador de negação (not)
negacao = not False
print(negacao)

if not verifica_login:
    print("loga certo aeee")