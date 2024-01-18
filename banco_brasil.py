print('=== Todo dia essa luta ===')
money = int(input("Informe o valor que você deseja tirar: "))

#centena = money // 100
#dezena = (money // 100) % 10
#unidade = money % 10
total = money
ced = 50
tot_ced = 0
while True:
 if total >= ced:
  total -= ced
  tot_ced += 1
 else:
  if tot_ced > 0:
   print('O valor total de cedulas foi de: ', tot_ced,'cédulas de ', ced)
  if ced == 50:
     ced = 20
     tot_ced = 0
  elif ced == 20:
   ced = 10
   tot_ced = 0
  elif ced == 10:
   ced = 1
   tot_ced = 0
  if total == 0:
     break

#print('O valor que você sacou foi contado em:  ', centena," centena(s)\n",dezena," dezena(s)\n",unidade," unidades")
