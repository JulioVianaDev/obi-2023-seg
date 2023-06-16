tamanhos = int(input())
qtdTamanhos = []
for _ in range(tamanhos):
    qtdTamanhos.append(int(input()))
pedidos = int(input())
vendido = 0
for i in range(pedidos):
    posicaoPedidoAtual= int(input()) -1
    if qtdTamanhos[posicaoPedidoAtual] >0:
        qtdTamanhos[posicaoPedidoAtual] -=1
        vendido+=1
print(vendido)