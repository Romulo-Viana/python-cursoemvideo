#Modo easy
import math
cO = float(input('Digite o comprimento do cateto oposto do seu triângulo: '))
cA = float(input('Digite o comprimento do cateto adjacente do seu triângulo: '))
hipo = math.hypot(cO, cA)
print(f'O valor da hipotenusa é: {hipo}')


#Modo hard
# h é a √h = c1² + c2² 
cateto1 = float(input('Digite o comprimento do cateto oposto do seu triângulo: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente do seu triângulo: '))
hipot = (cateto1**2 + cateto2**2) **(1/2)
print(f'O valor da hipotenusa do seu triângulo é: {hipot}')