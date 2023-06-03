infectados = int(input())
contagio = int(input())
alvo = int(input())
dias = 0
infectadosAtuais = infectados
while infectadosAtuais < alvo:
    dias+=1 
    novosInfectados = infectados * contagio
    infectados = novosInfectados
    infectadosAtuais += infectados
print(dias)
