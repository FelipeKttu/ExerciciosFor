for c in range(30):
    prova_1 = float(input('Digite a primeira nota:'))
    prova_2 = float(input('Digite a segunda nota:'))
    media = (prova_1 + prova_2 ) / 2

    if media >= 5:
        print('APROVADO !!')
    elif media < 5 and media >= 3:

        print('EXAME !!')

        nota_exame = float(input('Digite a nota do exame:'))

        if nota_exame > 5:
            print('APROVADO !!')
        elif nota_exame < 5:
            print('REPROVADO !!')

    elif media < 3:
        print('REPROVADO !!')
    
    
