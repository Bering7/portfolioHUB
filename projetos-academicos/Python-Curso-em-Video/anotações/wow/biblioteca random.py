# Importando a biblioteca random
import random

print("BIBLIOTECA RANDOM - Exemplos e Explicações\n")

# 1. random.random()
# Gera um número decimal aleatório entre 0 e 1
print("1. random():")
print("Número aleatório entre 0 e 1:", random.random())
print()

# 2. random.randint(início, fim)
# Gera um número inteiro aleatório dentro de um intervalo, incluindo os extremos
print("2. randint():")
print("Número inteiro entre 1 e 10:", random.randint(1, 10))
print()

# 3. random.uniform(início, fim)
# Gera um número decimal aleatório entre dois valores
print("3. uniform():")
print("Número decimal entre 1.5 e 9.9:", random.uniform(1.5, 9.9))
print()

# 4. random.choice(lista)
# Escolhe aleatoriamente um item de uma lista ou sequência
print("4. choice():")
cores = ["vermelho", "azul", "verde", "amarelo"]
print("Cor escolhida:", random.choice(cores))
print()

# 5. random.choices(lista, k=n)
# Retorna uma lista com 'k' escolhas, com repetição
print("5. choices():")
print("2 cores aleatórias (com repetição):", random.choices(cores, k=2))
print()

# 6. random.sample(lista, k=n)
# Retorna uma lista com 'k' itens aleatórios, sem repetição
print("6. sample():")
print("2 cores aleatórias (sem repetição):", random.sample(cores, k=2))
print()

# 7. random.shuffle(lista)
# Embaralha a ordem dos itens da lista original (modifica a lista)
print("7. shuffle():")
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print("Lista embaralhada:", numeros)
print()