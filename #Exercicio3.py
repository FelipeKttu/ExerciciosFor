for c in range (20):
    N = int(input('Digite o número:'))
    Resto = N % 2
    
    if Resto == 0:
        print('{} é Par'.format(N))
    elif Resto != 0:
        print('{} é Impar'.format(N))
