linhas = int(input())
textoFinal = ""
for i in range(linhas):
    textinho = str(input())
    textoFinal += textinho
chavesEmAberto = 0
FechouAntesDeAbrir  = False
for caracter in textoFinal:
    if caracter == "{":
        chavesEmAberto+=1
    if caracter == "}":
        chavesEmAberto-=1
    if chavesEmAberto < 0:
        FechouAntesDeAbrir = True
if chavesEmAberto == 0 and FechouAntesDeAbrir == False:
    print("S")
else: 
    print("N")
