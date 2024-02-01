print('Aqui se conta de verdade')
num = (float(input('informe um valor: ')), float(input('informe um valor: ')), float(input('informe um valor: ')), float(input('informe um valor: ')), float(input('informe um valor: ')))
tupla_num = (num)
print('você digitou os valores:', tupla_num)
print(f'O valor 9 apareceu', tupla_num.count(9),' vezes')
if 3 in tupla_num:
  print('O valor 3 apareceu na ', tupla_num.index(3)+1,' posição')
else:
 print('não possui valor 3 na lista')
for n in tupla_num:
 if n % 2 == 0:
  print('numeros pares: ', n)