mega = int(input())
meses = int(input())
sobrou = 0
gasto = 0
for mes in range(meses):
    gasto = int(input())
    sobrou += mega - gasto
print(sobrou + mega)