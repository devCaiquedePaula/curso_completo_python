# Tuplas
# As tuplas são estruturas de dados imutáveis em Python, ou seja, uma vez criadas, não podem ser alteradas.
# Elas são definidas usando parênteses.

# Criando uma tupla
tupla = (1, 2, 3, 4, 5)

# Acessando elementos de uma tupla
print(tupla[0])  # Saída: 1

# Tuplas podem conter diferentes tipos de dados
tupla_mista = (1, "dois", 3.0, True)

# Acessando elementos de uma tupla mista
print(tupla_mista[1])  # Saída: dois

# Tuplas podem ser aninhadas
tupla_aninhada = (1, (2, 3), 4)

# Acessando elementos de uma tupla aninhada
print(tupla_aninhada[1][0])  # Saída: 2

# Tuplas podem ser concatenadas
tupla_concatenada = tupla + tupla_mista
print(tupla_concatenada)  # Saída: (1, 2, 3, 4, 5, 1, 'dois', 3.0, True)

# Tuplas podem ser repetidas
tupla_repetida = tupla * 2
print(tupla_repetida)  # Saída: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Verificando o comprimento de uma tupla
print(len(tupla))  # Saída: 5

# Verificando se um elemento está em uma tupla
print(3 in tupla)  # Saída: True

# Verificando o índice de um elemento em uma tupla
print(tupla.index(3))  # Saída: 2

# Contando o número de ocorrências de um elemento em uma tupla
print(tupla.count(2))  # Saída: 1

# Desempacotamento de tuplas
a, b, c = tupla[:3]
print(a, b, c)  # Saída: 1 2 3

# Tuplas são úteis para retornar múltiplos valores de uma função
def coordenadas():
    return (10, 20)
x, y = coordenadas()
print(x, y)  # Saída: 10 20

# Tuplas são frequentemente usadas para armazenar dados que não devem ser alterados
# Exemplo de uso de tuplas em um dicionário
dados = {
    "pessoa1": ("João", 30),
    "pessoa2": ("Maria", 25)
}
# Acessando dados em um dicionário com tuplas
print(dados["pessoa1"])  # Saída: ('João', 30)

# Tuplas são mais eficientes em termos de memória do que listas
# e podem ser usadas como chaves em dicionários, enquanto listas não podem.
# Tuplas são imutáveis, então não podemos adicionar ou remover elementos
# de uma tupla após sua criação.
# No entanto, podemos converter uma tupla em uma lista, modificar a lista e depois convertê-la de volta para uma tupla.
tupla_para_lista = list(tupla)
tupla_para_lista.append(6)
tupla_modificada = tuple(tupla_para_lista)
print(tupla_modificada)  # Saída: (1, 2, 3, 4, 5, 6)

# Tuplas são úteis para agrupar dados relacionados
# e podem ser usadas para representar registros, coordenadas, etc.
# Exemplo de uso de tuplas para representar coordenadas
def ponto_2d(x, y):
    return (x, y)
ponto = ponto_2d(5, 10)
print(ponto)  # Saída: (5, 10)

# Tuplas também podem ser usadas para armazenar dados de forma segura,
# pois não podem ser alteradas acidentalmente.
# Isso é especialmente útil quando queremos garantir que os dados permaneçam constantes.
# Exemplo de uso de tuplas para armazenar dados constantes
dados_constantes = (3.14, "Pi", True)
print(dados_constantes)  # Saída: (3.14, 'Pi', True)

# Tuplas são uma parte fundamental da linguagem Python e são amplamente utilizadas em muitos contextos.
# Elas oferecem uma maneira eficiente e segura de agrupar dados relacionados.
# Conclusão
# As tuplas são uma estrutura de dados poderosa e versátil em Python.
# Elas são imutáveis, eficientes em termos de memória e podem ser usadas para agrupar dados relacionados.
# Tuplas são frequentemente usadas para retornar múltiplos valores de funções,
# armazenar dados constantes e representar registros ou coordenadas.

