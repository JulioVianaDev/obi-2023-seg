linhas,colunas = [int(i) for i in input().split()]
matriz = []
for i in range(linhas):
    valores = input()
    listaComValoresEmInteiro = [int(x) for x in valores.split()]
    matriz.append(listaComValoresEmInteiro)
somaDeTodasAsColunasDaMatriz = [sum(x) for x in zip(*matriz)]
somaDeTodasAsColunasDaMatriz.sort()
menor = somaDeTodasAsColunasDaMatriz[0]
print(menor)