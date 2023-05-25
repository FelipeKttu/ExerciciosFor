#Exercicio6
#Elaborar um programa que o usuário tenha que digitar 10 números inteiros. 
#No final, o programa deve exibir quantos números são múltiplos de 3, 
#quantos números são menores que 45 e maiores que 55, qual é o menor número entre eles e qual a média.
NMultiplos = 0
NMenores = 0
NMaiores = 0
M = 0
Menor = 0
for c in range (1,11):
      N = float(input('Digite um número:'))
      MN = N
      M = M + N 
      if N % 3 == 0:
          NMultiplos += 1
      if N < 45:
          NMenores += 1
      if N > 55:
          NMaiores += 1
      if N < Menor or Menor ==0:
           Menor = N
MF = M / 10
print('{} são multiplos de 3'.format(NMultiplos))
print('{} são menores que 45'.format(NMenores))
print('{} números são maiores que 55'.format(NMaiores))
print('{} é o menor número !!'.format(Menor))
print('{} é a media dos números'.format(MF))
      

