#Exercicio8
lista = []
contador = 0
for c in range (1,7):
  N = float(input('Digite um número:'))
  lista.append(N)
  print(lista)
  contador += 1
  print('Número {} Posição {} '.format(N,c-1))
print('a lista é {}'.format(lista))
