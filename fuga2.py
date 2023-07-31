helicoptero,policial,fugitivo,direcao = map(int,input().split())
# valores = list(map(int,input().split()))
# h       =valores[0]
# policial=valores[1]
# fug     =valores[2]
# dire    =valores[3]
while fugitivo != helicoptero:
    fugitivo += direcao
    if fugitivo < 0:
        fugitivo = 15
    if fugitivo > 15:
        fugitivo = 0
    if policial == fugitivo:
        break
if fugitivo == policial:
    print("N")
else:
    print("S")