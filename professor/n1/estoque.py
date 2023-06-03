linhas,colunas = map(int, input().split())
estoque =[]
for i in range(linhas):
    linha = list(map(int,input().split()))
    estoque.append(linha)
qtdPedidos = int(input())
vendidos = 0
for j in range(qtdPedidos):
    I,J = map(int,input().split())
    if estoque[I-1][J-1]>0 :
        estoque[I-1][J-1] -= 1
        vendidos+=1
print(vendidos)