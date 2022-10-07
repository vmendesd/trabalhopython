import math
numero = int(input('Digite um numero para saber o fatorial: '))
factor = math.factorial(numero)
for i in range(numero,0,-1):
    print(f'{i}', end=' ')
    print('X' if i > 1 else'=', end=' ')
print(factor, end=' ')
