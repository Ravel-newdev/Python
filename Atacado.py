while True:
 print("-="*10, "Atacado","-="*10)
 nome = str(input("Informe o nome do produto que você quer comprar: "))
 total = 0
 mais_1000 = 0
 if nome == "":
  print('informe o nome do produto.')
  break
 else:
  preco = float(input("Informe o preço do produto desejado: "))
  total += preco
  if preco > 1000:
   mais_1000 += 1
  if preco <= 0:
     print('informe um preço valido')
     break
  else:
   choice = str(input('Finalizar Compra? [s/n]: ')).lower().strip()[0]
   if choice not in 'sn':
      print('informe o valor corretamente')
      break
   elif choice == 's':
    print('Obrigado por compra nosso atacado!')
    print('Seu valor total foi de: ', total,'\n O numero de produtos com valor maior que 1000 é: ', mais_1000)
    break