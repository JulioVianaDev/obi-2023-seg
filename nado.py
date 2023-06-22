N1 = int(input())
N2 = int(input())
N3 = int(input())
lista = [[N1,"1",[12,33]],[N2,"2"],[N3,"3"]]
print(lista)
lista.sort()
print(lista)
# ver quem ganhou a olimpiada
print(lista[0][2][0])
print(lista[0][0])
print(lista[2][1])
print(lista[1][1])
print(lista[0][1])