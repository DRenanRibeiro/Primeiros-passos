from random import choice
a1 = str(input('Digite o nome de um aluno:'))
a2 = str(input('Digite o nome de outro aluno:'))
a3 = str(input('Digite o nome de outro aluno:'))
a4 = str(input('Digite o nome de outro aluno:'))
lista = [a1, a2, a3]
print('O aluno sorteado foi {}' .format(choice(lista)))