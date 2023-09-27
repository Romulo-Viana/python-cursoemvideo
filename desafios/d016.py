#USando módulo para encontrar um porção inteira de um número real
#Código com variavel reserva (inteiro) 
from math import trunc
n = float(input('Digite um valor: '))
inteiro = trunc(n)
print(f'O valor digitado foi {n} e a sua porção inteira é: {inteiro}')

#Código sem variável reserva
from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é: {trunc(n)}')


#Usnado função já existente no Python
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {n} e a sua porção inteira é: {int(n)}')



