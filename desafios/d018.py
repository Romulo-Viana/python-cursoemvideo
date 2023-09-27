from math import sin,cos,tan,radians
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
print(f'O seno de {ângulo} é....: {seno:20.2f}')
cosseno = cos(radians(ângulo))
print(f'O cosseno de {ângulo} é.: {cosseno:20.2f}')
tangente = tan(radians(ângulo))
print(f'A tangente de {ângulo} é: {tangente:20.2f}')
