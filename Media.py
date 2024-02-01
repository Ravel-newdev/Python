nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota:"))

media = (nota1 + nota2 + nota3)/3
media_p = ((nota1 * 2) + (nota2 * 4) + (nota3 * 3))/9
print("A sua media é: ", media)
media = round(media, 2)
print("A sua media ponderada: ", media_p)
media_p = round(media_p, 2)