linhas,colunas = map(int,input().split())
estoque = []
for _ in range(linhas):
    linha = list(map(int,input().split()))
    estoque.append(linha)
pedidos = int(input())
comprados = 0
for _ in range(pedidos):
    I,J = map(int,input().split())
    if estoque[I-1][J-1]>0:
        estoque[I-1][J-1] -=1
        comprados+=1
print(comprados)