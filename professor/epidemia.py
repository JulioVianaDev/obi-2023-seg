N= int(input())
R= int(input())
P= int(input())
dias =0
infectadosAtual = N
while infectadosAtual<P:
    dias+=1
    NovosInfectados = N * R
    N = NovosInfectados
    infectadosAtual += N
print(dias)