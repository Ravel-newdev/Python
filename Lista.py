lista = []
while True:
 lista.append(float(input('informe um numero: ')))
 resposta = str(input('Você vai querer continuar?: ')).strip().lower()[0]
 if resposta in 'n':
  break
 elif resposta not in 'sn':
  print('a reposta é sim ou não.')
print(lista)
print(f'A lista possui {len(lista)} caracteres')
lista.sort(reverse=True)
print('A lista em ordem crescente fica assim: ', lista)