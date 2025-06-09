# Strings em Python
# Strings são sequências de caracteres
# Strings podem ser definidas com aspas simples ou duplas


nome = "Caique de Paula Nascimento"
print(nome)

print(nome[0])
print("Marca d'água")
print('Marca d\'água')

# Strings com múltiplas linhas
doc = """Lorem ipsum dolor sit amet, 
\tconsectetur adipiscing elit.
\tSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
\tUt enim ad minim veniam, quis nostrud exercitation ullamco laboris 
\tnisi ut aliquip ex ea commodo consequat."""
print(doc)

print("-----------------------------------")

nome2 = 'Caique de Paula Nascimento'
print(nome2[0])
print(nome2[4])
print(nome2[6:])
print(nome2[-5:])
print(nome2[:3])
print(nome2[3:6])

print("-----------------------------------")

numeros = "0123456789"
print(numeros)
print(numeros[::2]) # Pega os elementos de 2 em 2
print(numeros[1::2]) # Pega os elementos de 2 em 2, a partir do segundo
print(numeros[::-1]) # Inverte a string
print(numeros[::-2]) # Inverte a ‘string’ e pega os elementos de 2 em 2

print("-----------------------------------")

frase = "Python é uma linguagem de programação"
print('py' in frase) # Verifica se a substring está na string
print(len(frase)) # Tamanho da string
print(frase.upper()) # Converte a string para maiúsculas
print(frase.lower()) # Converte a string para minúsculas
print(frase.capitalize()) # Converte a primeira letra da ‘string’ para maiúscula
print(frase.title()) # Converte a primeira letra de cada palavra para maiúscula
print(frase.strip()) # Remove espaços no início e no final da ‘string’
print(frase.replace('Python', 'Java')) # Substitui uma substring por outra
print(frase.split()) # Divide a ‘string’ numa lista de palavras
print(frase.split('a')) # Divide a ‘string’ numa lista de palavras, usando 'a' como separador
print(frase.split(' ')) # Divide a ‘string’ numa lista de palavras, usando espaço como separador

