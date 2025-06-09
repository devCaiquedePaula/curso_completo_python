# Dicionários em Python
# Dicionários sao estruturas de dados que armazenam pares de chave-valor

# Criando um dicionário
dicionario = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores
print(dicionario["nome"])  # Saída: João
print(dicionario["idade"])  # Saída: 30
print(dicionario["cidade"])  # Saída: São Paulo

# Adicionando novos pares chave-valor
dicionario["profissão"] = "Engenheiro"
print(dicionario)
# Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'profissão': 'Engenheiro'}

# Atualizando valores
dicionario["idade"] = 31
print(dicionario["idade"])  # Saída: 31

# Removendo pares chave-valor
del dicionario["cidade"]
print(dicionario)  # Saída: {'nome': 'João', 'idade': 31, 'profissão': 'Engenheiro'}

# Verificando se uma chave existe
print("nome" in dicionario)  # Saída: True
print("cidade" in dicionario)  # Saída: False

# Iterando sobre chaves e valores
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
# Saída:
# nome: João
# idade: 31
# profissão: Engenheiro

# Obtendo todas as chaves
print(dicionario.keys())  # Saída: dict_keys(['nome', 'idade', 'profissão'])

# Obtendo todos os valores
print(dicionario.values())  # Saída: dict_values(['João', 31, 'Engenheiro'])

# Obtendo pares chave-valor como tuplas
print(dicionario.items())  # Saída: dict_items([('nome', 'João'), ('idade', 31), ('profissão', 'Engenheiro')])

# Limpando o dicionário
dicionario.clear()
print(dicionario)  # Saída: {}

# Dicionários aninhados
dicionario_aninhado = {
    "pessoa1": {
        "nome": "Ana",
        "idade": 25
    },
    "pessoa2": {
        "nome": "Carlos",
        "idade": 28
    }
}

# Acessando valores em dicionários aninhados
print(dicionario_aninhado["pessoa1"]["nome"])  # Saída: Ana
print(dicionario_aninhado["pessoa2"]["idade"])  # Saída: 28

# Adicionando um novo dicionário aninhado
dicionario_aninhado["pessoa3"] = {
    "nome": "Maria",
    "idade": 22
}
print(dicionario_aninhado)
# Saída: {'pessoa1': {'nome': 'Ana', 'idade': 25},
# 'pessoa2': {'nome': 'Carlos', 'idade': 28},
# 'pessoa3': {'nome': 'Maria', 'idade': 22}}

# Atualizando um valor em um dicionário aninhado
dicionario_aninhado["pessoa1"]["idade"] = 26
print(dicionario_aninhado["pessoa1"]["idade"])  # Saída: 26

# Removendo um dicionário aninhado
del dicionario_aninhado["pessoa2"]
print(dicionario_aninhado)
# Saída: {'pessoa1': {'nome': 'Ana', 'idade': 26},
# 'pessoa3': {'nome': 'Maria', 'idade': 22}}

# Tamanho do dicionário
print(len(dicionario_aninhado))  # Saída: 2

# Verificando se o dicionário está vazio
print(not dicionario_aninhado)  # Saída: False

# Verificando o tipo de um dicionário
print(type(dicionario_aninhado))  # Saída: <class 'dict'>



