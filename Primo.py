num = int(input('Informe um numero: '))
if num == '':
 print('Informa o numero, agora')
else:
 for c in range(1, num + 1):
  print(c)
  if num % c == 0:
   print('não é primo')
  else:
   print('é primo')