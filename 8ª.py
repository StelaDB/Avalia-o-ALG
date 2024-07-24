#Escreva um programa que cria uma lista de duas dimensões utlizando List 
#Compreshion e imprima a diagonal principal desta lista.
import random
a = [[random.randint(1,10)for j in range(3)]for i in range(3)]
b=[]
for i in range(3):
    for j in range(3):
        if i==j:
          dp = a[i][j]
          b.append(dp)
for linha in a:
    print(linha)
print("Essa é a diagonal principal",b)