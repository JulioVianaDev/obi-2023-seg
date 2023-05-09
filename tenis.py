p1 = input()
p2 = input()
p3 = input()
p4 = input()
p5 = input()
p6 = input()
jogos = [p1,p2,p3,p4,p5,p6]
vitorias = 0
for partida in jogos:
    if partida == "V":
        vitorias += 1
if vitorias == 1 or vitorias == 2:
    print(3)
if vitorias == 4 or vitorias == 3:
    print(2)
if vitorias == 5 or vitorias == 6:
    print(1)
if vitorias== 0:
    print(-1)
