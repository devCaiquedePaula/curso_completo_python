# Interpolação de ‘Strings’
# Seria a substituição de valores numa ‘string’
from string import Template

nome, idade = 'João', 26

# Interpolação com o operador de formatação - Antigo
print('Nome: %s, Idade: %d' % (nome, idade))

# Interpolação com o methods format - Novo
print('Nome: {}, Idade: {}'.format(nome, idade))

# Interpolação com f-strings - Mais Novo
print(f'Nome: {nome}, Idade: {idade}')

# Interpolação com Template - Novo
s = Template('Nome: $nome, Idade: $idade')
print(s.substitute(nome=nome, idade=idade))