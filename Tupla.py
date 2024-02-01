valor_tupla = []
for c in range(0,5):
 valor_tupla.append(float(input(f'Informe um valor para inserir na posição {c +1} da lista: ')))
 #print(valor_tupla)
 maior = max(valor_tupla)
 menor = min(valor_tupla)
 p_maior = valor_tupla.index(maior) +1
 p_menor = valor_tupla.index(menor) +1
print('você digitou os numeros: ', valor_tupla , "\n O maior valor da lista é: ",maior,"\n O menor valor da lista: ",menor)
print(f'O valor: {maior} está na posição: {p_maior} \n O valor: {menor} está na posição: {p_menor}')
