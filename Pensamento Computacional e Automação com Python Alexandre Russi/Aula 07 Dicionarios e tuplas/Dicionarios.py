from multiprocessing import context

eng2sp = dict()
print(eng2sp)

eng2sp["one"] = "uno"
print(eng2sp)

eng2sp = {
    "one": "uno",
    "two": "dois",
    "three": "tres"
}
print(eng2sp["two"])

#Operador IN
print('one' in eng2sp)

#selecionar valores
valores= eng2sp.values()
print('uno' in valores)

#contando letras
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("paralelepipedo")
print(dict_contagem)