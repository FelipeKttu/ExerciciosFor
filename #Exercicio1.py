for C in range(5):
    print(C)
    V1 = float(input('Digite o primeiro valor:'))
    V2 = float(input('Digite o segundo valor:'))
    S = V1 + V2
    print('A soma é {}'.format(S))
    
    if V1 > V2:
        print("O primeiro valor é maior !!")
    elif V2 > V1:
        print('O segundo valor é maior !!')
