pao=int(input())
doce=int(input())
bolo=int(input())
soma = pao + doce*2 + bolo*3
if soma >=150:
    print("B")
elif soma>=120:
    print("D")
elif soma>=100:
    print("P")
else:
    print("N")