salario = float(input('Qual seu salário atual? R$ '))
salario2 = salario*15/100
novosalario = salario2 + salario
print(f'Seu salário teve um aumento de R$ {salario2:.2f} reais, e foi atualizado para R$ {novosalario:.2f} reais. Parábens!')

#Lembra que para encontrar qualquer porcentagem valor*%/100

#Segunda opção
salario = float(input('Qual seu salário atual: R$ '))
nsalario = salario + (salario*15/100)
print(f'Seu salário antigo de R${salario:.2f} foi atualizado para R${nsalario:.2f} aumento de 15%. Parabéns!')