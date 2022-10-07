valor = float(input('Quantos doláres você quer converter em real: '))
cota = 5.65
real = valor * cota
if valor >= 100:
    desconto = valor * (cota + (cota*0.1))
    print(f'Como você converteu mais de 100 doláres, irá ganhar 10% de desconto, no caso ficou o valor total de {desconto:.2f} centavos. ')
else:
    print(f'Você vai receber {real:.2f} reais ')