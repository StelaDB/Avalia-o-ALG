#Escreva um programa que leia o índice pluviométrico de cada dia do mês de 
#junho e informe o dia que mais choveu, o dia que menos choveu e as médias 
#pluviométricas de cada uma das duas quinzenas.
soma1=0
soma2=0
list_pl = []
for i in range (1,31):
    pl = int (input("Digite o {}° numero: ".format(i)))
    if i <= 15:
        soma1+=pl
    else:
        soma2+=pl
    list_pl.append(pl)
    maior = list_pl[0]
    menor = list_pl[0]
    for n in list_pl:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

for j in range(len(list_pl)):
    if list_pl[j] == maior:
        print(f"O dia que mais choveu foi o {j+1}° dia")
        break 
for k in range(len(list_pl)):
    if list_pl[k] == menor:
        print(f"O dia que menos choveu foi o {k+1}° dia")
        break  
        
print(f"A média pluviométrica da primeira quinzena é {soma1/15} %")
print(f"A média pluviométrica da segunda quinzena é {soma2/15} %")