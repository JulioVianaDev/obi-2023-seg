lista1 = [1,2,6]
lista2 = [6,4,15]
print(lista1+ lista2)
print([x + y for x, y in zip(lista1, lista2)])

a = [3,5]
b = [2,2]
x = zip(a, b)
print(*x)