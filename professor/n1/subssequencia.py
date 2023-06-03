tamanho_seq1, tamanho_seq2 = map(int, input().split())
sequencia1 = list(map(int, input().split()))
sequencia2 = list(map(int, input().split()))
i = 0  # índice para percorrer a sequência 1
j = 0  # índice para percorrer a sequência 2
while i < tamanho_seq1 and j < tamanho_seq2:
    if sequencia1[i] == sequencia2[j]:
        j += 1 
    i += 1
if j == tamanho_seq2:
    print("S")
else:
    print("N")
