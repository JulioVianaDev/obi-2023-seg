degraus = int(input())
k = 0
for i in range(1,degraus+1):
    for spaces in range(1,(degraus-i)+1):
        print(end='  ')
    while k!= (2*i-1):
        print(k,end='')
        k=0
    print()
print()