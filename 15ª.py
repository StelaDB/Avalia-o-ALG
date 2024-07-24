#A locadora de carros precisa da sua ajuda para cobrar seus serviços. 
#Escreva um programa que pergunte a quantidade de Km percorridos por 
#um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e 
#R$0,20 por Km rodado.
km = int(input("Digite a quantidade de quilômetros percorridos: "))
d = int(input("Digite a quantidade de dias que o carro foi alugado: "))
pt = (d*90)+(km*0.20)
print(f"O preço total a ser pago é de R${pt}")