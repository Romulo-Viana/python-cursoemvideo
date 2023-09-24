algo = input("Digite um valor: ")
print(f'Seu tipo é: {type(algo)}')
print(f'Pode ser um número? {algo.isnumeric()}')
print(f'Pode ser uma alfabético? {algo.isalpha()}')
print(f"Pode ser alfanumérico? {algo.isalnum()}")
print(f'Está todo em maiúsculo? {algo.isupper()}')
print(f'Está todo em minúsculo? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')#Quando está escrito em formato de nome próprio, com letra maiúscula iniciando e todo restanto minúscula 

