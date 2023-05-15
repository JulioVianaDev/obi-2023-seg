caixa1 = int(input())
caixa2 = int(input())
caixa3 = int(input())
lista = [caixa1,caixa2,caixa3]
lista.sort()
menor = lista[0]
medio = lista[1]
maior = lista[2]
viagens = 3
if menor + medio < maior:
    viagens = 1
elif menor == maior and menor == medio:
    viagens = 3
else:
    viagens = 2
print(viagens)
