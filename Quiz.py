from time import sleep
#é melhor usar while
print("Quiz -> ")
aceito = input("Você aceita participar? (S/N) ")
print(aceito)
#perguntas = 0
score = 0
aceito = aceito.lower()
#while perguntas <= 2:
if aceito != "s":
    print("encerrando")
    quit()
else:
    print("Vamos começar!! \n")
    sleep(2)
    print("Quanto é 1 + 1? \n a) 1  \n b) 2  \n c) 11  \n d) 0 ")

    resp1 = int(input("resposta: "))

if resp1 in "bB2":
    score = score + 1
    print("Você acertou! ")
    sleep(2)
else:
    sleep(2)
    print("incorreto")
    sleep(2)
    print("vamos ver se você acerta a proxima (duvido)")
    sleep(2)



print("O que é H2O? \n a) Sal \n b) Uma banda \n c) um H e 2 O \n d) Água")
resp2 = input("resposta: ")
resp2 = resp2.lower()
if resp2 == "Água" or resp2 in "d":
    score = score + 1
    sleep(2)
    print("acertou pelo menos")


else:
    sleep(2)
    print("incorreto")
    sleep(2)
    print("a sua incopetencia me espanta, humano")
    sleep(2)


print("Em que ano o Brasil virou uma ditadura? \n a) 2023 \n b) 1891 \n c) 8800 a.c \n d) 1964")
resp3 = str(input("resposta: "))
if resp3 in "1964d":
    score = score + 1
    print("Acabou, veja sua nota...")
    sleep(2)
    print("pontuação: ", score)


if score == 3:
    print("Você está de parabens")
    print("pontuação: ", score)
elif score == 2:
    print("você conseguiu")
    print("pontuação: ", score)
else:
    sleep(2)
    print("infelizmente você não passou")
    print("pontuação: ", score)

print("-" * 10)