dia = float(input('Quantos dias foi alugado: '))
km = float(input('Quantos km foram rodados: '))
preço_km = (km*0.15) + (dia*60)
print(f'Você rodou {km}km por {dia} dias, o preço total do aluguel é de R${preço_km:.2f}')