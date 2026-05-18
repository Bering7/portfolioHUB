# Texto base para todos os exemplos
texto = "  Olá, Mundo! Bem-vindo ao Python. Python é incrível!  "

# 1. FATIAMENTO DE STRING
# Acessa partes específicas da string usando índices
print("Fatiamento:")
print(texto[3:8])   # Mostra os caracteres do índice 3 até o 7 (exclui o 8)
print(texto[:5])    # Do início até o índice 4
print(texto[10:])   # Do índice 10 até o final
print(texto[::2])   # Pula de 2 em 2 caracteres
print()

# 2. ANÁLISE COM len(), count(), find()
print("Análise:")
print("Tamanho da string:", len(texto))                    # Conta o número total de caracteres (inclui espaços)
print("Quantidade de 'Python':", texto.count("Python"))    # Conta quantas vezes 'Python' aparece
print("Posição da palavra 'Mundo':", texto.find("Mundo"))  # Retorna o índice da primeira ocorrência
print("Palavra 'Java' existe?", texto.find("Java") != -1)  # find() retorna -1 se não encontrar
print()

# 3. TRANSFORMAÇÕES
print("Transformações:")
print("replace():", texto.replace("Python", "Java"))      # Substitui 'Python' por 'Java'
print("upper():", texto.upper())                          # Converte toda a string para maiúsculas
print("lower():", texto.lower())                          # Converte toda a string para minúsculas
print("capitalize():", texto.capitalize())                # Primeira letra maiúscula, resto minúsculo
print("title():", texto.title())                          # Primeira letra de cada palavra maiúscula
print("strip():", texto.strip())                          # Remove espaços extras no início e fim
print()

# 4. JUNÇÃO COM join()
print("Junção com join():")
palavras = texto.strip().split()                          # Quebra a string em uma lista de palavras
texto_junto = "-".join(palavras)                          # Junta usando hífens
print("Texto com hífens:", texto_junto)