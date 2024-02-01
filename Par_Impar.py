from random import randint
from time import sleep
while True:
 print("=-"*10 ,"Pao ou Impar?", "=-"*10)
 sleep(2)
 print("Vamos jogar esse jogo maravilhoso.")
 sleep(2)
 num = int(input("informe o numero que você deseja jogar(até 10, você não tem mais que 10 dedos): "))
 IA = randint(0, 11)
 if num > 10:
    print("Você tem mais de 10 dedos???")
    sleep(2)
    print('vamos tentar novamente.')
 else:
  val = str(input('Par ou Impar? [p/i]')).lower().strip()[0]
  sum = num + IA
  if val not in 'pi':
      print('informe um valor válido')
  else:
   print("Você informou o numero: ", num, ". \n A IA informou o numero: ", IA, ". \n A soma do seus valores é", sum)
   if val == 'p':
    if sum % 2 == 0:
     print("O jogador venceu!!")
    else:
     print("Quem venceu foi eu!! ;)")
   elif val == 'i':
    if sum % 2 != 0:
       print("O jogador venceu!!")
    else:
       print("Quem venceu foi eu!! ;)")
sleep(2)
"""