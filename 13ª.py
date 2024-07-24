#calcula a raiz quadrada de dois pontos
x1=int(input("Digite o valor de x1: "))
x2=int(input("Digite o valor de x2: "))
y1=int(input("Digite o valor de y1: "))
y2=int(input("Digite o valor de y2: "))

distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
print("A distância entre os pontos é:", distancia)