tupla = list()
while True:
 num = int(input('Adicione um numero a lista: '))
 if num not in tupla:
  tupla.append(num)
  resp = str(input('Quer continuar?[S/N]: ')).strip().lower()[0]
  if resp == 's':
    continue
  elif resp == 'n':
     break
  else:
     print('Responda direito')
 else:
    print('esse numero já foi informado')
    tupla.sort()
    print(tupla)
