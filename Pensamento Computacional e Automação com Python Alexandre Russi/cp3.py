# Matriz de temperaturas
temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

# Variáveis para controle da sala com maior risco
maior_risco = 0
sala_maior_risco = 0


for i in range(len(temperaturas)):
    sala = temperaturas[i]

    # Calcula a média das temperaturas
    media = sum(sala) / len(sala)

    # Conta registros críticos (temperatura >= 33)
    registros_criticos = 0

    for temperatura in sala:
        if temperatura >= 33:
            registros_criticos += 1

    # Exibe os dados da sala
    print(f"Sala {i + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registros_criticos}")
    print()

    # Verifica qual sala possui mais registros críticos
    if registros_criticos > maior_risco:
        maior_risco = registros_criticos
        sala_maior_risco = i + 1

# Resultado final
print(f"Sala com maior risco: Sala {sala_maior_risco}")