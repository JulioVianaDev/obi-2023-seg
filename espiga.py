dias = int(input())
lista=[]
for i in range(dias):
    lista.append(int(input()))
valor = 0
for dia in lista:
    valor+=dia
    if valor>=1000000:
        print(lista.index(dia) +1)
        break