tamanhoLista,tamanhoSubLista = [int(i) for i in input().split()]
valoresLista1 = list(map(int,input().split()))
valoresSub = list(map(int,input().split()))
i = 0
j = 0
while i< tamanhoLista and j < tamanhoSubLista:
    if valoresLista1[i] == valoresSub[j]:
        j+=1
    i+=1
if j == tamanhoSubLista:
    print("S")
else:
    print("N")