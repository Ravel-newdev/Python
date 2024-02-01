from time import sleep

num1 = input("Digite um numero: ")
num2 = input("Digite um segundo valor: ")
num1 = float(num1)
num2 = float(num2)
if num1 == "" or num2 == "":
    print("Não brinque comigo")
else:
#1. Dar o direito de escolha da operação para o usuario
 print("veja as operações: \n 1.Adição \n 2.Subtração \n 3.Multiplicação \n 4.Divisão \n 5.Exponenciação")
 oper = input("informe a operação (A,S,M,D,E): ")
 oper = oper.lower()
 if oper != "a" and oper != "s" and oper != "m" and oper != "d" and oper != "e" and oper == "":
    print("Você não vai participar se for rebelde na hora de digitar, humano")
 else:
  if oper == "a":
   soma = num1 + num2
   print("A soma dos valores é: ", soma)

  elif oper == "s":
    subs = num1 - num2
    subs = round(subs, 3)
    print("A subtração dos valores é: ", subs)
  elif oper == "m":
    mult = num1 * num2
    print("A multiplicação dos valores é: ", mult)
  elif oper == "d":
     divi = num1 / num2
     divi = round(divi, 3)
     print("A divisão dos valores é: ", divi)
  elif oper == "e":
     expo = num1 ** num2
     print("o primeiro valor elevado ao segundo é: ", expo)
     print('-' * 12)
#arredondar os resultados para não mais que 3 casas
#math.max()??
print("\n A soma dos valores é: ", soma, "\n A subtração dos valores é: ", subs, "\n A multiplicação dos valores é: ", mult , "\n A divisão dos valores é: ", divi)
#adicionando a tabuada
sleep(4)
tabu = input("Vamos calcular uma tabuada também, basta informar um numero: ")

tabu = float(tabu)
if tabu == "":
    sleep(2)
    print("Informe um valor, plmds.")
elif tabu == 0:
    sleep(3)
    print("Tá de brincadeira?? me poupe")
else:
 print("Tabuada: \n")
 i = 0
 while i < 10:
   i += 1
   print(tabu * i)
print("-" * 12)
sleep(3)
eita = input("Input: ")
