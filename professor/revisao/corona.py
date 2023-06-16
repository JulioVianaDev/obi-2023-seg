N  = int(input())
R  = int(input())
P  = int(input())
infectadosAtuais = N
dias = 0

while infectadosAtuais < P:
    N = N * R
    infectadosAtuais += N
    dias+=1
print(dias)