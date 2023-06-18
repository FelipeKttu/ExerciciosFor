#Exercicio8

lista = []
contador = 0

for c in range (1,7):
  
  numero = float(input('Digite um número:'))
  lista.append(numero)

  print(lista)

  contador += 1

  print('Número {} Posição {} '.format(numero,c-1))

print('a lista é {}'.format(lista))
