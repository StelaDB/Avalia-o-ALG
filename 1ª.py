#Faça um programa que calcule o fatorial de todos os numeros impares dentre 
#os 10 primeiros da sequência de Fibonacci. 
a, b = 0, 1
c = 0
while c < 10: 
    f=1
    proxn = a+b
    a = b
    b = proxn
    if a % 2 != 0:
        for i in range(1, a+1):
            f*=i
        print(f, end=" ")            
    c += 1   