# Tipos Numéricos

from decimal import Decimal

a = 5
b = 2.5

print(type(a),type(b))
print(a / b)
print(a + b)
print(a - b)
print(a * b)

print(b.is_integer())
print(5.0.is_integer())

print(dir(int))
print(int.__add__(2, 3))
print((-2).__abs__())

print(Decimal(1.1) + Decimal(2.2))
print(Decimal.max(Decimal(1), Decimal(7)))



