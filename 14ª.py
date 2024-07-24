#Escreva um programa que encontre os números primos é uma tarefa 
#difícil. Faça um programa que gera uma lista dos números primos 
#existentes entre 1 e um número inteiro informado pelo usuário. 
n = int(input("Digite um número: "))
lista = []
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lista.append(i)
print(lista)