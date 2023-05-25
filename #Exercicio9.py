#Exercicio9
#Elaborar um programa para ler uma lista A de 15 elementos e um valor X. O 
#programa deve copiar para a lista B somente os elementos de A que são maiores que X. Exibir no final a lista 
listaA = []
listaB = []
print('A segunda lista vai ser formada por números menores que X')
V = float(input('Digite O valor de X:'))
for c in range(1,16):
  N = float(input('Digite um valor para adicionar na lista:')) 
  listaA.append(N)
  print(listaA)
  if N > V:
    listaB.append(N)
print('A primeira lista é {}'.format(listaA))
print('A segunda lista é {}'.format(listaB))