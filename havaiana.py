tamanhos = int(input())
quantidadePorTamanho = []
for i in range(tamanhos):
    quantidadePorTamanho.append(int(input()))
quantidadeDePedidos = int(input())
pedidosAprovados = 0
for j in range(quantidadeDePedidos):
    pedidoAtual = int(input())
    checarTamanho = quantidadePorTamanho[pedidoAtual-1]
    if checarTamanho > 0:
        quantidadePorTamanho[pedidoAtual-1]-=1
        #reposta aqui atualizar os pedidosAprovados

print(pedidosAprovados)