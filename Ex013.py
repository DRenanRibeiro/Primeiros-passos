salário = float(input('Qual é o salário do Funcionário? R$'))
porcentagem = int(input("Qual a porcentagem de aumento do Funcionário?"))
aumento = salário + (salário *(porcentagem/100))
print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${}.' .format (salário, porcentagem, aumento))
