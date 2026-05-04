# dado um conjunto de nome de 4 pessoas, escreva um algoritmo que imprima todas as possiveis duplas que podem ser formadas.
# primeiro, crie um vetor e coloque quatro nomes nele.
# a seguir exiba as possiveis duplas.

duplas = ["Ana", "Maria", "Enzo", "Leo"]
i = 0
for i in range(len(duplas)):
    for j in (range(i + 1, len(duplas))):
        print(f"Duplas: {duplas[i], duplas[j]}")
