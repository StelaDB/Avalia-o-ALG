#Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% 
#ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 
#2% ao ano, escreva um programa, que imprima o tempo necessário para que a 
#população do país A ultrapasse a população do país B. 
pa = 5000000
pb = 7000000
c=0
while pa < pb:
    pa = pa + pa*0.03
    pb = pb + pb*0.02
    c+=1
print("A população A ultrapassará a população B em: ", c, "anos")