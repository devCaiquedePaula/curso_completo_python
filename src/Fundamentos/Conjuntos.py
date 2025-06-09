# Conjuntos
# Um conjunto é uma coleção de elementos únicos.
# Conjuntos são mutáveis, mas os elementos devem ser imutáveis.
# Conjuntos são úteis para operações matemáticas como união, interseção e diferença.

# Criando um conjunto
conjunto = {1, 2, 3, 4, 5}
a = set("Python")  # Conjunto de caracteres únicos
print(a)

b = {1,2,3}
c = {3,2,1,3}
d = b == c
print(d)

c1 = {1, 2, 3}
c2 = {3, 4, 5}
# Operações com conjuntos
uniao = c1.union(c2)  # União
intersecao = c1.intersection(c2)  # Interseção
diferenca = c1.difference(c2)  # Diferença
subconjunto = c1.issubset(c2)
superconjunto = c1.issuperset(c2)
print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença:", diferenca)
print("É subconjunto:", subconjunto)
print("É superconjunto:", superconjunto)

