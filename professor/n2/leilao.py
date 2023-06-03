numLances = int(input())
valorDosLances = []
for i in range(numLances):
    nome = str(input())
    valor = int(input())
    valorDosLances.append([nome,valor])
maiorValor = 0
for i in range(len(valorDosLances)):
    if valorDosLances[i][1]> maiorValor:
        maiorValor = valorDosLances[i][1]
for i in range(len(valorDosLances)):
    if valorDosLances[i][1] == maiorValor:
        print(valorDosLances[i][0])
        print(valorDosLances[i][1])
        break