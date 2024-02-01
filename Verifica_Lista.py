lista = []
par = []
impar = []
while True:
 lista.append(int(input('informe um numero: ')))
 resposta = str(input('Você vai querer continuar?: ')).strip().lower()[0]
 if resposta in 'n':
  break
 elif resposta not in 'sn':
  print('a reposta é sim ou não.')
 else:
  for i, v in enumerate(lista):
   if v % 2 == 0:
    par.append(v)
   elif v % 2 != 0:
    impar.append(v)
print(f'A lista é assim: {lista}')
print(f'Pares: {par}')
print(f'Impares: {impar}')