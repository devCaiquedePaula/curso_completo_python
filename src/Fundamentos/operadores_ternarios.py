# Operadores ternarios
chuva = input("Está chovendo? (s/n): ").strip().lower()
esta_chovendo = chuva == 's'
# Usando operador ternário para decidir a mensagem
print("Hoje estou com as roupas " + ("secas", "molhadas")[esta_chovendo] + " -> Aqui usamos índice booleano (forma menos recomendada)")
print("Hoje estou com as roupas " + ("molhadas" if esta_chovendo else "secas") + " -> Aqui usamos IF ELSE ternário (forma recomendada e mais clara)")