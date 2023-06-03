degraus = int(input("num de degraus: "))
k = 1
for i in range(degraus,0,-1):
    for j in range(0,i):
        print(k,end="")
    print("\n")
    k=k+1
print()