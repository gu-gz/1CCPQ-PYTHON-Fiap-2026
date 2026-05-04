lista_frutas = ["banana", "maça", "melancia"]

print(lista_frutas[1])

lista_frutas.append("Laranja")
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

    print()

    for fruta in lista_frutas:
        print(fruta)