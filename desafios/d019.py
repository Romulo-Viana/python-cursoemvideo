import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo Aluno: ')
a3 = input('Nome do terceiro aluno: ')
lista = [a1, a2, a3]
escolhido = random.choice(lista)
print(f'O escolhi para apagar o quadro é: {escolhido}')
