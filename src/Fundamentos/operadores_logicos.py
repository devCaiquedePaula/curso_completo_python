# Operadores Logicos
# Operadores lógicos son utilizados para combinar expresiones booleanas.

# Operador AND
def and_operator(a, b):
    return a and b # Retorna True se ambos são verdadeiros, caso contrário retorna False

# Operador OR
def or_operator(a, b):
    return a or b # Retorna True se pelo menos um é verdadeiro, caso contrário retorna False

# Operador NOT
def not_operator(a):
    return not a # Retorna a negação do valor booleano, ou seja, True se a for False e vice-versa

# Operador XOR (Exclusivo)
def xor_operator(a, b):
    return (a and not b) or (not a and b) # Retorna True se apenas um dos valores for verdadeiro, caso contrário retorna False

#Cuidado
# Operadores Bitwise
def bitwise_and(a, b):
    return a & b # Retorna o resultado da operação AND bit a bit '&'

def bitwise_or(a, b):
    return a | b # Retorna o resultado da operação OR bit a bit '|'

def bitwise_xor(a, b):
    return a ^ b # Retorna o resultado da operação XOR bit a bit '^'

def bitwise_not(a):
    return ~a # Retorna o resultado da operação NOT bit a bit  '~'