# print(1 + '1')
# Isso vai gerar um erro do tipo TypeError porque você não pode somar um número inteiro com uma string

# print('1' + '1')
# Isso vai concatenar (juntar) duas strings, resultando em '11'

# print(1 + 1)
# Isso vai somar dois números inteiros, resultando em 2

# print(1 + 1.0)
# Isso vai somar um inteiro com um número decimal (float), resultando em 2.0

# print(1 + True)
# Isso vai somar um inteiro com um booleano, resultando em 2 (True é tratado como 1)

# print(1 + False)
# Isso vai somar um inteiro com um booleano, resultando em 1 (False é tratado como 0)

# print(7 * '1')
# Isso vai repetir a string '1' sete vezes, resultando em '1111111'


# Data Structures

# Lista (List) - Estrutura bem simples em Python
lista = [1, 2, 3, 4, 5]
print("Lista:", lista)


# Árvore (Tree) - Só um nó simples
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


# Fila (Queue) - Primeiro que entra é o primeiro que sai
fila = []

# Adicionar na fila
fila.append('A')
fila.append('B')
fila.append('C')

# Remover da fila
item = fila.pop(0)  # Remove o primeiro
print("Item removido da fila:", item)
print("Fila atual:", fila)


# Pilha (Stack) - Último que entra é o primeiro que sai
pilha = []

# Adicionar na pilha
pilha.append('X')
pilha.append('Y')
pilha.append('Z')

# Remover da pilha
item = pilha.pop()  # Remove o último
print("Item removido da pilha:", item)
print("Pilha atual:", pilha)


# Dicionário (Dictionary)
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessar um valor pelo nome da chave
print(pessoa["nome"])  # Maria

# Adicionar um novo par chave:valor
pessoa["profissão"] = "Engenheira"

# Alterar valor
pessoa["idade"] = 31

# Mostrar o dicionário completo
print(pessoa)


# Criando uma tupla
ponto = (10, 20)

print(ponto)        # (10, 20)
print(ponto[0])     # 10 (acessa o primeiro elemento)

# Tuplas não permitem mudar valores
# ponto[0] = 5
# Isso vai dar erro!


