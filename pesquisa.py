quantidade = int(input())
aprovados = []
for i in range(quantidade):
    estado,alcool,gasosa = map(str,input().split())
    alcool = float(alcool)
    gasosa = float(gasosa)
    if alcool <= gasosa * 0.7:
        aprovados.append(estado)
if len(aprovados) == 0:
    print("*")
else:
    for estado in aprovados:
        print(estado)