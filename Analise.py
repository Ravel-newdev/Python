
print("-"*3, "1 Pessoa", "-"*3)
nome = input("Informe o primeiro nome: ")
idade = int(input("Informe sua idade: "))
sexo = input("Informe o sexo [M/F]: ")
sexo = sexo.lower()

if sexo == "" or idade == "" or nome == "" or idade < 0 or sexo != "m" and sexo != "f":
 print("Informe todos os valores")
else:
 p1 = [nome, idade, sexo]

print("-"*3, "2 Pessoa", "-"*3)
nome2 = input("Informe o segundo nome: ")
idade2 = int(input("Informe sua idade: "))
sexo2 = input("Informe o sexo [M/F]: ")
sexo2 = sexo2.lower()

if sexo2 == "" or idade2 == "" or nome2 == "" or idade2 < 0 or sexo2 != "m" and sexo2 != "f":
 print("Informe todos os valores")
else:
 p2 = [nome2, idade2, sexo2]

print("-"*3, "3 Pessoa", "-"*3)
nome3 = input("Informe o terceiro nome: ")
idade3 = int(input("Informe sua idade: "))
sexo3 = input("Informe o sexo [M/F]: ")
sexo3 = sexo3.lower()

if sexo3 == "" or idade3 == "" or nome3 == "" or idade3 < 0 or sexo3 != "m" and sexo3 != "f":
 print("Informe todos os valores")
else:
 p3 = [nome3, idade3, sexo3]

print("-"*3, "4 Pessoa", "-"*3)
nome4 = input("Informe o quarto nome: ")
idade4 = int(input("Informe sua idade: "))
sexo4 = input("Informe o sexo [M/F]: ")
sexo4 = sexo4.lower()

if sexo4 == "" or idade4 == "" or nome4 == "" or idade4 < 0 or sexo4 != "m" and sexo4 != "f":
 print("Informe todos os valores")
else:
 p4 = [nome4, idade4, sexo4]

print("-"*3, "5 Pessoa", "-"*3)
nome5 = input("Informe o quinto nome: ")
idade5 = int(input("Informe sua idade: "))
sexo5 = input("Informe o sexo [M/F]: ")
sexo5 = sexo5.lower()

if sexo5 == "" or idade5 == "" or nome5 == "" or idade5 < 0 or sexo5 != "m" and sexo5 != "f":
 print("Informe todos os valores")
else:
 p5 = [nome5, idade5, sexo5]

media_idade = ((p1[1]) + (p2[1]) + (p3[1]) + (p4[1]) + (p5[1]))/5
maior_idade = (p1[1], p2[1], p3[1], p4[1], p5[1])
maior_idade = max(maior_idade)
 print("A media da idade é de:", media_idade,"\nA maior idade é", maior_idade ,"e pertence á:")
"""
sexo = str(input("Informe seu sexo: ")).strip().upper()

while sexo not in "MmFf":
 sexo = str(input("Tente informar seu sexo: ")).strip().upper()
 if sexo in "Mm":
  print("Deu certo, você informou o sexo masculino ")
  break
 elif sexo in "Ff":
  print("Deu certo você informou o sexo feminino")
  break
"""