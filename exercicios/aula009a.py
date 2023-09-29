frase = 'Curso em Vídeo Python'
# Regra básica: Mostra na frase[inicio: final: pula].
print(frase[9])
print(frase[9:13])
print(frase[9:13:2])
# Não declarar valor antes dos : é o mesmo que índice [inicial]
print(frase[:5])
# Não declarar valor depois dos : é o mesmo que índice [final]
print(frase[15:])
print(frase[9::3])

#Diz o comprimento de uma variável
print(len(frase))

# Analisa a quantidade de um determinado valor na variável
print(frase.count('o'))

# Conta quantos 'o' existem do índice [0] até [13]. Lembrando que o índice [13] não é considerado
print(frase.count('o',0,13))

# Indica qual índice começa no trecho de frase 'deo'
print(frase.find('deo'))

# Busca algo que não existe na variável retorna o valor de -1. Mesma coisa que "não foi encontrado"
print(frase.find('Android'))

# Utilizar o operador 'in' retorna valor booleano 
print('Curso' in frase)


# Torna a primeira letra de toda palavra maiúscula
print(frase.title())

# A função replace substitui um valor por outro desejado
print(frase.replace('Python', 'Android'))

# Torna todos caracteres maiúsculos
print(frase.upper())

# Torna todos caracteres minúsculos
print(frase.lower())


# Torna todo que está maiúsculo em minúsculo com acessão do caractere de índice [0]
print(frase.capitalize())

# Torna todos caracteres minúsculos com ecessão da primeira letra de cada palavra
print(frase.title())

# Remove todos espaços inúteis no início e final, que possam existir.  
print(frase.strip())


# Remove todos espaços inúteis no início ou na direita, que possam existir.  
print(frase.rstrip())

# Remove todos espaços inúteis no final ou esquerda, que possam existir.  
print(frase.lstrip())

# Divide as palavra dentro de uma variável baseado nos espaços entre elas, tornando-as uma lista com palavras separadas e índices individuais para cada palavra.
print(frase.split())

# Uni palavras de uma lista, removendo a característica de uma lista e indexando de forma continua.
print(''.join(frase))