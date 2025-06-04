#Dado o salario de um funcionario e suas despesas mensais, calcule quantos % do salario esta comprometido para as despesas.
salario = float(input("Digite o salário do funcionário: "))
despesas = float(input("Digite o total das despesas mensais: "))
percentual_comprometido = (despesas / salario) * 100
print(f"O percentual do salário comprometido com as despesas é: {percentual_comprometido:.2f}%")