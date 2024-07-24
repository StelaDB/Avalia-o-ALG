#Um banco concederá um crédito especial aos seus clientes, variável 
#com o saldo médio no último ano. Faça um algoritmo que leia o saldo 
#médio de um cliente e calcule o valor do crédito de acordo com a tabela 
#abaixo. Mostre uma mensagem informando o saldo médio e o valor do 
#crédito. 
sm = int(input("Informe seu saldo médio: "))
if sm < 201:
    print("Saldo médio de", sm, "reais. Nenhum crédito.")
elif 200 < sm < 401:
    print(f"Saldo médio de {sm} reais. Crédito de R${sm*0.20}")
elif 400 < sm < 601:
    print(f"Saldo médio de {sm} reais. Crédito de R${sm*0.30}")
else:
    print(f"Saldo médio de {sm} reais. Crédito de R${sm*0.40}")