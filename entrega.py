caixa1= int(input())
caixa2= int(input())
caixa3= int(input())
lista =[caixa1,caixa2,caixa3]
lista.sort()
menor = lista[0]
medio = lista[1]
maior = lista[2]
viagens = 3
if medio+menor < maior:
    viagens = 1
elif medio < maior or menor < medio:
    viagens = 2
print(viagens)