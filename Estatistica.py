
while True:
 print("="*15 ,"Cadastro de seres humanos(apenas)", "="*15)
 idade = int(input("Informe a sua idade: "))
 sexo = str(input("Informe seu sexo[m/f]: ")).lower().strip()[0]
 total_idade = 0
 total_H = 0
 total_F = 0
 if sexo not in 'mf':
  print('informe um sexo válido')
  break
 else:
  choice = str(input("Quer continuar?[s/n]: ")).lower().strip()[0]
  if idade >= 18:
   total_idade += 1
  if sexo == 'm':
   total_H += 1
  else:
   total_F += 1
  if choice not in 'sn':
      print('informe uma resposta válida')
      break
  else:
    if choice == 'n':
       print("a quantidade de pessoas com, ou mais de 18 é: ", total_idade,'\n A quantidade de homens é: ', total_H, '\n O total de mulheres é: ', total_F)
       break

