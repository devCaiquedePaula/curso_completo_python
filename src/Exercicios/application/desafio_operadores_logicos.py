"""
Confirmando os 2: TV 50' + Sorvete
Confirmando apenas 1: TV 32' + Sorvete
Nenhum confirmado: Ficar em casa
"""

terca = input("Você trabalhou na terça? (s/n): ")

if terca == "s":
    trabalho_terca = True
else:
    trabalho_terca = False

quinta = input("Você trabalhou na quinta? (s/n): ")

if quinta == "s":
    trabalho_quinta = True
else:
    trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("Tv50={}, Tv32={}, Sorvete={}, Mais Saudavel={}"
        .format(tv_50, tv_32, sorvete, mais_saudavel))
