lista0 = [1,2,3,4,5,6,7,8]
lista1 = [1,2,3,4,5,6,7,8]
lista2 = ['1','2','3','4','5','6','7','8']
lista3 = ['a','a','a','a','a','a','a','a',]
# print(*zip(lista1,lista2,lista3))
# for x in zip(lista1,lista2,lista3):
#     print(x)
# for x ,y in zip (lista1,lista3):
#     print("y: ",y)
matriz = lista0,lista1
a =[sum(x) for x in zip(*matriz)]

print(*zip(matriz))