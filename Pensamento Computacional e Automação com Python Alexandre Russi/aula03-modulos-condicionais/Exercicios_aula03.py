#exercicio 2
#number = int(input("Digite um número: "))

#if number % 2 != 0:
#    print('impar')
#else:
#    print('par')

#exercicio 3
#num_a = float(input("Digite o primeiro numero: "))
#num_b = float(input('Digite o segundo numero: '))
#if num_a > num_b:
#    print(num_a)
#elif num_a == num_b:
#    print("iguais")
#else:
#    print(num_b)
#exercicio 4
#num_1 = float(input("digite a primeira nota: "))
#num_2 = float(input("digite a segunda nota: "))
#num_3 = float(input("digite a terceira nota: "))
#num_4 = float(input("digite a quarta nota: "))
#media = (num_1 + num_2 + num_3 + num_4) / 4
#print("Média:", media)
#if media < 5:
#    print("reprovado")
#elif media >= 5 and media < 7:
#        print("Recuperação")
#else:
#        print("aprovado")
#exercicio 5
num_y = int(input("digite o numero A: "))
num_x = int(input("digite o numero B: "))

if num_x == 0 or num_y == 0:
    print("Número zero não é válido")
elif num_y % num_x == 0 or num_x % num_y == 0:
    print("são multiplos")
else:
    print("não são multiplos")