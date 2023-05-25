for C in range(30):
    P1 = float(input('Digite a primeira nota:'))
    P2 = float(input('Digite a segunda nota:'))
    M = (P1 + P2 )/ 2
    if M >= 5:
        print('APROVADO !!')
    elif M < 5 and M >= 3:
        print('EXAME !!')
        NE = float(input('Digite a nota do exame:'))
        MF = (M + NE) / 2
        if MF > 5:
            print('APROVADO !!')
        elif MF < 5:
            print('REPROVADO !!')
    elif M < 3:
        print('REPROVADO !!')
    
