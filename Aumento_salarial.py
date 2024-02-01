sal = float(input("Informe o seu salário: "))

if sal < 2000:
 au = sal + (sal * 20/100)
 print("O seu novo sálario é de: ", au ," proletariado")
elif sal >= 2000 and sal < 4000:
 au = sal + (sal * 10/100)
 print("o seu novo salário é de: ", au, "agora tendo melhores condições")
elif sal >= 4000 and sal < 6000:
 print("Você não terá aumento")
elif sal == "":
    print("Informe o valor")
elif sal <= 0:
 print("Você está na escravidão??")
else:
 print("Você é um burguês dono dos meios de produção.(brincadeira)")