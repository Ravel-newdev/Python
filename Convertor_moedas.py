real = float(input("Informe a quantidade de dinheiro que você quer converter: "))

dolar = real / 4.92
L_E = real / 6.28
euro = real / 5.37
dolar = round(dolar, 2)
L_E = round(L_E, 2)
euro = round(euro, 2)
print("O valor do seu dinheiro convertido para dólar é: ", dolar, "\n Convertido para libra esterlina: ", L_E, "\n Convertido para euro: ", euro)
input("Coloque a sua opnião sobre isso: ")
print("Concordo.")