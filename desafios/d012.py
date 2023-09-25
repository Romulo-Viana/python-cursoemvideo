preco = float(input('Qual o preço do produto? R$ '))
porcent5 = preco*5/100
desconto5 = preco - porcent5
print(f'Desconto de 5%, corresponde a R${porcent5:.2f}. Total à pagar de R${desconto5:.2f} reais')

#Lembra que para encontrar qualquer porcentagem valor*%/100

#Segunda opção
preco = float(input('Qaul o preço do produto? R$ '))
novo = preco - (preco*5/100)
print(f"O produto de R${preco:.2f} com desconto de 5% custa {novo:.2f}")