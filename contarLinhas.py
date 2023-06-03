qtdLinhas = int(input())
textoFinal = ''
for i in range(qtdLinhas):
    textinho = str(input())
    textoFinal+= textinho
print(textoFinal[0])
if textoFinal[0] == 'a' or textoFinal[0] == 'e'or textoFinal[0] == 'i' or textoFinal[0] == 'o' or textoFinal[0] == 'u':
    print("S")
else:
    print("N")