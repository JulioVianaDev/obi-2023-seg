#Exibir uma informação
print("Mostrar algo na tela")

#pedir uma informação
input()

#salvar a informação em uma variavel
variavel = input()

#transformar o texto em numero
numero = int(input())

#organizar uma lista
lista = [12,77,0]
lista.sort() # lista=[0,12,77]

#pegar o primeiro item da lista
primeiro = lista[0]

#adicionar um item na lista
lista.append(12)

# pedir uma quantidade de informações
quantidade = int(input())
for rep in range(quantidade):
    input()

#printar o item da lista
lista =["ronaldo","kaká","neymar"]
for itemDaLista in lista:
    print(itemDaLista)

#controlar repetições
for rep in range(13,29):
    print(rep)

# perguntar se um valor é igual ao outro 
valor1 = 12
valor2 = 17
valor3 = 12

if valor1 == valor2:
    print("são iguais")
elif valor3 == valor1 or valor2 == valor3:
    print("segundo loop") 
else:
    print("tudo errado")
