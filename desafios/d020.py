import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
lista = [a1, a2, a3]
random.shuffle(lista)
print(f'A ordem dos alunos é: {lista}')