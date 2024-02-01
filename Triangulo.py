seg1 = float(input("Informe o valor do primeiro segmento: "))
seg2 = float(input("Informe o valor do segundo segmento: "))
seg3 = float(input("Informe o valor do terceiro segmento: "))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
 print("É triangulo")
 if seg1 == seg2 and seg2 == seg3:
  print("O triangulo é equilatero")
 elif seg1 == seg2 and seg1 != seg3 or seg2 == seg3 and seg2 != seg1 or seg3 == seg1 and seg3 != seg2:
  print("O triangulo é isoceles")
 else:
  print("O triangulo é escaleno")

else:
    print("Bicho réi burro sabe nem fazer um triangulo")