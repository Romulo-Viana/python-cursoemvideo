largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual altura da parede? '))
area = largura*altura
tinta = area/2

print(f'A dimensão total é {area:.2f}m², e são necessarios {tinta:.1f}l de tinta para pintar toda a parede.')