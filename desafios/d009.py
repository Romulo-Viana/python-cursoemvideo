n = int(input('Digite um valor: '))

i = 1
print(f'TABUADA DE {n}:')
while i < 11:
    tabuada = n*i
    print(f'{n} X {i:2} = {tabuada:5}')
    i=i+1
    