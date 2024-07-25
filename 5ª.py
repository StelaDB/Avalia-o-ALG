#Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% 
#ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 
#2% ao ano, escreva um programa, que imprima o tempo necessário para que a 
#população do país A ultrapasse a população do país B. 
a= 5000000
b = 7000000
c=0
while a < b:
    a = a + a*0.03
    b = b + b*0.02
    c+=1
print("A população A ultrapassará a população B em: ", c, "anos")