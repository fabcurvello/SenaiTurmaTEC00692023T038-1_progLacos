'''
11)	Elaborar um programa que apresente o valor de uma potência de
uma base qualquer (Variável b) elevada a um expoente qualquer (Variável e),
ou seja, de b elevado à e. (Sem usar Math.pow();)
'''

b = float(input("Informe a base da potência: "))
e = float(input("Informe o expoente da potência: "))

pot = b ** e

print(f"{b:.0f} elevado à {e:.0f} = {pot:.0f}")