'''
11)	Elaborar um programa que apresente o valor de uma potência de
uma base qualquer (Variável b) elevada a um expoente qualquer (Variável e),
ou seja, de b elevado à e. (Sem usar Math.pow();)
'''

b = float(input("Informe a base da potência: "))
e = float(input("Informe o expoente da potência: "))

# usuário -> b = 3, e = 4
# no papel -> 3 * 3 * 3 * 3

cont = 1
acumulador = 1
while ( cont <= e ):
    acumulador = acumulador * b
    cont = cont + 1

print(f"{b:.0f} elevado à {e:.0f} = {acumulador:.0f}")