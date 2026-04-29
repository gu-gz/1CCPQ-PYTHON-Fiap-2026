while True:
    print('hello world')
    while True:
        resposta = input('Deseja exibir a mensagem novamente? Sim ou Nao?').lower().strip()
        if resposta == 'sim'or resposta == 'nao':
            break
        else:
            print('Resposta invalida! digite apenas Sim ou Nao')
    if resposta == 'nao':
        break
print('Fim')