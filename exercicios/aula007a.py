n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
ex = n1 ** n2
intdiv = n1 % n2
rdiv = n1 // n2

print(f'A soma é: {soma}\nA subtração é: {sub}\nA multiplicação é: {mul}\nA divisão é: {div}\nA exeponenciação é: {ex}\nA divisão inteira é: {intdiv}\nO resto da divisão é: {rdiv}')
print('')
print(f'A soma entre {n1} e {n2} é = {soma}',end='')
print(f'A subtração entre {n1} e {n2} é = {sub}')