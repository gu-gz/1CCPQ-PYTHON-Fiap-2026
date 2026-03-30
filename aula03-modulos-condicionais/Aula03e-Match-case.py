from re import Match

escolha_usuario = 4
# 0 -> sair do programa
# 1 -> entrar no programa
# >>>>> erro!

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!!")