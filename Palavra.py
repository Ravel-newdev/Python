word = "javascript"
letters = []
chances = 6
#variavel "ganhou"
win = False

while True:
 for letter in word:
  if letter.lower() in letters:
       print(letter, end=" ")
 else:
   print("_", end=" ")
   print(" ")

   tente = input("Informe a letter: ")
   letters.append(tente.lower())
   if tente.lower() not in word.lower():
    chances -= 1

   if chances == 0:
       print("Você não conseguiu")
       break
"""
   if win:
    print("Você conseguiu, parabéns.")
   else:
    print('perdeu, otário')
"""

