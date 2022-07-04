na = input('Digite o nome do Aluno:')
n1 = float(input('Digite uma nota:'))
n2 = float(input('Digite uma nota:'))
m = float(( n1 + n2 ) / 2)
print('As médias do aluno {} é {}.' .format(na, m))

#ou

na = input('Digite o nome do aluno:')
n3 = float(input('Digite a primeira nota do aluno:'))
n4 = float(input('Digite a segunda nota do aluno:'))
m2 = float(( n3 + n4 ) / 2)
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n3, n4, m2))