# Listas
# Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável.
# Elas são mutáveis, ou seja, podem ser alteradas após a criação.
# Listas são arrays dinâmicos que podem conter elementos de diferentes tipos, incluindo outros arrays.

lista = []
print(lista)
# Adicionando elementos à lista
lista.append(1)
lista.append(2)
lista.append(3)
# Exibindo a lista
print("Lista após adição:", lista)

# Removendo um elemento da lista
lista.remove(2)
# Exibindo a lista após remoção
print("Lista após remoção:", lista)

# Acessando elementos da lista
print("Primeiro elemento:", lista[0])

# Verificando o tamanho da lista
print("Tamanho da lista:", len(lista))

# Verificando se um elemento está na lista
print("O número 1 está na lista?", 1 in lista)

# Ordenando a lista
lista.sort()
print("Lista ordenada:", lista)

# Invertendo a lista
lista.reverse()
print("Lista invertida:", lista)

# Limpando a lista
lista.clear()
print("Lista após limpeza:", lista)

# Criando uma lista com elementos iniciais
lista_inicial = [4, 5, 6]

# Concatenando listas
lista_concatenada = lista_inicial + [7, 8, 9]
print("Lista concatenada:", lista_concatenada)

# pop - Remove e retorna o último elemento da lista
ultimo_elemento = lista_concatenada.pop()
print("Último elemento removido:", ultimo_elemento)

# Fatiamento de listas
fatiamento = lista_concatenada[1:4]  # Pega do índice 1 ao 3
print("Fatiamento da lista:", fatiamento)

# Listas aninhadas (listas dentro de listas)
lista_aninhada = [[1, 2], [3, 4], [5, 6]]
print("Lista aninhada:", lista_aninhada)

# Acessando elementos de listas aninhadas
print("Primeiro elemento da primeira lista aninhada:", lista_aninhada[0][0])

# Iterando sobre uma lista
for elemento in lista_concatenada:
    print("Elemento:", elemento)

# Listas com compreensão de listas
lista_compreensao = [x**2 for x in range(10)]  # Quadrados dos números de 0 a 9
print("Lista com compreensão de listas:", lista_compreensao)

# Verificando se uma lista é vazia
def is_lista_vazia(lista):
    return len(lista) == 0
print("A lista está vazia?", is_lista_vazia(lista))

# Função para contar elementos em uma lista
def contar_elementos(lista):
    return len(lista)
print("Número de elementos na lista:", contar_elementos(lista_concatenada))

print("---------------------------------------------")

carros = ["Supra mk4", "Civic g6", "Porsche 911", "Nissan 350z", "Ferrari f40"]
print(carros[1:3])
print(carros[1:-1])
print(carros[1:])
print(carros[:-1])
print(carros)
print(carros[::2])
print(carros[::-1])
del carros[1:]
print("Lista de carros após deleção:", carros)
