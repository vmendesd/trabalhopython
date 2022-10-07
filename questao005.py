numero = int(input('Digite um número para multiplicar: '))
count = 0
print(f'{numero} X 0 = 0 ')
for i in range(1,11):
    multi = numero * i
    count = count + 1
    print(f'{numero} X {count} = {multi}')

