sal = float(input("Informe o seu salário: "))
compra = float(input("Informe o quanto você pretende gastar: "))
emp = float(input("informe a quantidade de parcelas que você irá pagar o empréstimo: "))

valor_emp = compra / emp
valor_emp = round(valor_emp, 2)

if valor_emp > (sal * 30/100):
 print("O valor mensal do empréstimo será:", valor_emp,", você não pode tirar o emprestimo")
else:
 print("O valor mensal do empréstimo será:", valor_emp,", vá tirar, pobre")