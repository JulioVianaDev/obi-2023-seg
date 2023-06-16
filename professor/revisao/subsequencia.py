TL1 , TL2 = map(int, input().split())
lista1 = list(map(int, input().split()))
lista2 = list(map(int, input().split()))
contadorL1 = 0
contadorL2 = 0
while contadorL1 < TL1 and contadorL2 < TL2:
    if lista1[contadorL1] == lista2[contadorL2]:    
        contadorL2+=1 
    contadorL1+=1
if contadorL2 == TL2:
    print("S")
else:
    print("N")
