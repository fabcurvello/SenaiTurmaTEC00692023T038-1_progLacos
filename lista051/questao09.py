'''
9)	Elaborar um programa que apresente no final a
soma dos valores pares existentes na faixa de 0 até 500.
Utilize um laço que efetue a variação de 2 em 2.
'''

cont = 0
soma = 0  # soma é acumulador

while ( cont <= 500 ):
    soma = soma + cont
    cont = cont + 2

print(f"a soma dos valores pares de 0 a 500 é {soma}")