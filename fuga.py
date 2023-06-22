valores = list(map(int, input().split()))
helicoptero = valores[0]
policial = valores[1]
fugitivo = valores[2]
direcao = valores[3]

while fugitivo != helicoptero:
    fugitivo += direcao
    if fugitivo <0:
        fugitivo = 15
    if fugitivo > 15:
        fugitivo = 0
    if fugitivo == policial:
        break
if fugitivo == policial:
    print("N")
else: 
    print("S")