# Operador de Membro
# O operador de membro é usado para verificar se um valor é um membro de uma coleção, como uma lista ou um dicionário.
lista = [1, 2, 3, 'Supra', 'GTR R34']
print(1 in lista)
print('Supra' not in lista)

# operador de identidade
# O operador de identidade é usado para verificar se duas variáveis apontam para o mesmo objeto na memória.
x = 3
y = x
z = 3
print(x is y)  # True, pois y é uma referência ao mesmo objeto que x
print(y is z)  # True, pois z tem o mesmo valor que x, mas é um objeto diferente
print(x is not z)  # False, pois x e z têm o mesmo valor, mas são objetos diferentes