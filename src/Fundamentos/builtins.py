# Builtins são funções e objetos que já estão disponíveis no Python sem a necessidade de importação.
# Eles são parte do escopo global e podem ser usados diretamente.

print(type(1))
print(__builtins__,type("Fala galera!"),type(1.5),type(True),type(None))

# Exemplo de uso de alguns builtins

print(len("Fala galera!"))  # Retorna o comprimento da string
print(max([1, 2, 3, 4, 5]))  # Retorna o maior valor da lista
print(min([1, 2, 3, 4, 5]))  # Retorna o menor valor da lista
print(sum([1, 2, 3, 4, 5]))  # Retorna a soma dos valores da lista
print(sorted([5, 3, 1, 4, 2]))  # Retorna a lista ordenada

# Exemplo de uso de algumas funções built-in

print(abs(-10))  # Retorna o valor absoluto
print(round(3.14159, 2))  # Arredonda o número para duas casas decimais

# Exemplo de uso de algumas funções built-in

print(all([True, True, False]))  # Retorna False se algum elemento for False
print(any([True, False, False]))  # Retorna True se algum elemento for True
print(bin(10))  # Converte o número para binário
print(hex(255))  # Converte o número para hexadecimal
print(oct(8))  # Converte o número para octal
print(isinstance(10, int))  # Verifica se 10 é um inteiro
print(isinstance("Fala galera!", str))  # Verifica se "Fala galera!" é uma string
