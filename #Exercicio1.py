for c in range(5):
    valor1 = float(input('Digite o primeiro valor:'))
    valor2 = float(input('Digite o segundo valor:'))
    soma = valor1 + valor2
    print('A soma é {}'.format(soma))
    print(c)
    
    if valor1 > valor2:
        print("O primeiro valor é maior !!")
    elif valor2 > valor1:
        print('O segundo valor é maior !!')
