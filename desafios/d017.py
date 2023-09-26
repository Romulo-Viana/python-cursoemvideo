#Modo easy
import math
cO = float(input('Digite o valor do cateto oposto do seu triângulo: '))
cA = float(input('Digite o valor do cateto adjacente do seu triângulo: '))
hipo = math.hypot(cO, cA)
print(f'O valor da hipotenusa é: {hipo}')


#Modo hard
cateto1 = float(input('Digite o valor do cateto oposto do seu triângulo: '))
cateto2 = float(input('Digite o valor do cateto adjacente do seu triângulo: '))
hipot = (cateto1**2 + cateto2**2) **(1/2)
print(f'O valor da hipotenusa é: {hipot}')