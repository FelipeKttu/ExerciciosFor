for C in range (10):
    NI = int(input('Digite um Número Inteiro:'))
    R = NI % 3
    if R == 0:
        print('O Número {} é multiplo de 3'.format(NI))
    elif R != 0:
        print('O Número {} não é multiplo de 3'.format(NI))
    
    if NI > 0:
        print('O Número é Positivo')
    elif NI < 0: 
        print('O Número é Negativo')