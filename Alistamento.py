from time import sleep
from datetime import date

ano = int(input("informe o seu ano de nascença: "))
sexo = input("Informe o seu sexo (M ou F): ")
atual = date.today().year
idade = atual - ano
alista = ano
sexo = sexo.lower()
if sexo == "m":
 if idade == "" or idade < 0:
    print("Informe um valor válido, plmds")
 elif idade > 18:
  dife = idade - 18
  print("Você tem: ", idade,", você não precisa se alistar, mas precisou a", dife, "anos atrás")
 elif idade == 18:
    print("Você tem: ", idade ,"e necessita se alistar")
 else:
  dife = 18 - idade
  print("Você tem: ", idade,"\n você ainda não tem 18 anos, mas terá de se alista daqui a", dife,"anos")
else:
    print("Você não é obrigada a se alistar")