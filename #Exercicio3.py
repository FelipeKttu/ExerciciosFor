for C in range (20):
    N = int(input('Digite o número:'))
    R = N % 2
    if R == 0:
        print('{} é Par'.format(N))
    elif R != 0:
        print('{} é Impar'.format(N))