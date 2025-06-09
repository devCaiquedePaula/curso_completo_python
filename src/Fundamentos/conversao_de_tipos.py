# Conversão de tipos em Python
# Conversão de tipos é o processo de transformar um valor de um tipo de dado para outro.
# Python possui funções embutidas para conversão de tipos, como int(), float(), str(), etc.
# Exemplo de conversão de tipos

numero_inteiro = 10
numero_float = float(numero_inteiro)  # Converte inteiro para float
print(numero_float)  # Saída: 10,0

numero_float = 3.14
numero_inteiro = int(numero_float)  # Converte float para inteiro
print(numero_inteiro)  # Saída: 3

texto = "123"
numero_inteiro = int(texto)  # Converte ‘string’ para inteiro
print(numero_inteiro)  # Saída: 123

numero_float = float(texto)  # Converte string para float
print(numero_float)  # Saída: 123,0

numero_texto = str(numero_inteiro)  # Converte inteiro para ‘string’
print(numero_texto)  # Saída: '123'

numero_texto_float = str(numero_float)  # Converte float para ‘string’
print(numero_texto_float)  # Saída: '123,0'



