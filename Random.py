from random import randint
num = (randint(0,14000), randint(0,14000), randint(0,14000), randint(0,14000), randint(0,14000),)
print(f'Os numeros sorteados foram os numeros:', end='')
for n in num:
 print(f' {n},', end='')
maior = max(num)
menor = min(num)
print('\n O maior valor é: ', maior, '\n O menor numero é: ', menor)