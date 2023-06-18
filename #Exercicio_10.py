#Exercicio10
'''Elaborar um programa que contem uma lista com 5 elementos. 
O usuário deve preencher essa lista. Exibir no final os valores inseridos pelo usuário, 
porém os valores negativos (caso existirem) devem ser substituídos por zero (0).'''

lista = []

for c in range(1,6):

    N = float(input('Digite o valor que quer adicionar a lista:'))

    if N < 0:
        N = 0

    lista.append(N)
    
print('A lista é {}'.format(lista))
