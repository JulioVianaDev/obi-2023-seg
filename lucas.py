estados = int(input())
aprovados = []
for i in range(estados):
    linha = list(map(str, input().split()))
    estado = linha[0]
    alcool = float(linha[1])
    gasolina = float(linha[2])
    if alcool <= gasolina * 0.7:
        aprovados.append(estado)
if len(aprovados) == 0:
  print('*')
else:
   for estado in aprovados:
      print(estado)