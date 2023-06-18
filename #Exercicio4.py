for c in range (10):
    NumInt = int(input('Digite um Número Inteiro:'))
    resto = NumInt % 3
    if resto == 0:
        print('O Número {} é multiplo de 3'.format(NumInt))
    elif resto != 0:
        print('O Número {} não é multiplo de 3'.format(NumInt))
    
    if NumInt > 0:
        print('O Número é Positivo')
    elif NumInt < 0: 
        print('O Número é Negativo')
