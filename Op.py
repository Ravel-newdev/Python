v1 = float(input("Informe um valor: "))
v2 = float(input("Informe um segundo valor: "))
v3 = float(input("Informe um terceiro valor: "))
for i in range(6):
 print("=== Veremos suas \033[0;30;41m opções ===")
 print("[1] Somar \n [2]Multipicar \n [3] Maior numero \n [4] Adicionar numero \n [5] Sair do programa")
 value = int(input("Informe um numero: "))
 list = [v1, v2, v3]
 if value > 6 or value < 1:
      print('informe um valor valido')
 else:
  if value == 4:
   v = float(input("Informe o novo valor que você quer apresentar: "))
   list.append(v)
  elif value == 1:
       soma = sum(list)
       print("O valor total da soma é de: ", soma)
  elif value == 2:
       mult = v1 * v2 * v3
       print("O valor da multiplicação é de: ", mult)
  elif value == 3:
       max = max(list)
       print("O maior valor é: ", max)
  elif value == 5:
     break
     