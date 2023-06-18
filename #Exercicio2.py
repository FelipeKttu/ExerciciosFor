for c in range(20):
    print(c)
    VA = float(input('Digite o primeiro valor:'))
    VB = float(input('Digite o segundo valor:'))
    VC = float(input('Digite o terceiro valor:'))
    
    if VA > VB and VA > VC:
        print('O primeiro valor {} é o maior !!'.format(VA))
    elif VB > VA and VB > VC:
        print('O segundo valor {} é o maior !!'.format(VB))
    elif VC > VA and VC > VB:
        print('O terceiro valor {} é o maior !!'.format(VC))
