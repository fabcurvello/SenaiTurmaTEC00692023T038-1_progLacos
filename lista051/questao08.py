'''
8)	Desenvolver um programa que apresente todos os valores numéricos
inteiros ímpares situados na faixa de 0 a 20. Para saber se o número é ímpar,
será necessário verificar essa condição com o comando if.
Sendo ímpar, mostre-o; não sendo, passe para o próximo passo.
'''
# regra 1 da estrutura de repetição:
# declarar var contador no valor inicial da repetição
cont = 0

# regra 2: testar a esturura (while com var contador) no valor fim da repetição
while ( cont <= 20 ):
    # bloco que será repetido várias vezes
    resto = cont % 2
    if ( resto == 1 ):
        print( cont )

    # regra 3: incrementar a var contador na última linha dentro do bloco
    cont = cont + 1
