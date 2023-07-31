quantidade = int(input())
lista = []
#<--- um item por linha-->

# for entrada in range(quantidade):
#     numero= int(input())
#     lista.append(numero)
# print(lista)

#<--- dois itens por linha-->

# for pedido in range(quantidade):
#     tamanho,numero = map(int,input().split())
#     print(f"tenho do tamanho {tamanho} {numero} quantidades")

#<--- dois itens por linha(string , float)-->

# for pedido in range(quantidade):
#     cidade,numero = map(str,input().split())
#     numero = float(numero)
#     resultado = numero * 0.8 
#     print(f"Na cidade {cidade} vai ter {resultado} de pessoas")
for i in range(quantidade):
    entrada = list(map(int,input().split()))
    print(sum(entrada))
