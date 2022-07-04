#Condicionais
# if, elif e else
'''
  E ae jhonatan, bora dar uma saida hoje?
  Se eu terminar meu trabalho aqui, eu consigo.
'''
trabalho_terminado = True

if trabalho_terminado == True:
    print('Opa!Bora dar uma saida.')
else:
    print('Não posso sair agora.')
'''
Ei, você consegue me ajudar a mover essas caixas lá para fora hoje a tarde?
Se eu estiver livre, sim. Mas se não der pede para meu irmãp para te ajudar.
'''
estou_livre = False
if estou_livre == True:
    print('Ok, posso ajudar hoje sim!')
else:
    print('Peça o meu irmão para te ajudar')
'''
  Eu cheguei atrasado na aula, ainda posso entrar?
  Se essas não for a sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão.
'''
numero_de_atrasos = 2
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, porém caso tome mais 1 falta, irá ser suspenso')
else:
    print('Pode entrar')
'''
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
  print o primeiro valor é maior
else
  print o segundo valor é maior
'''

primeiro_valor = input('Insira o primeiro valor')
segundo_valor = input('Insira o segundo valor')
if int(primeiro_valor) > int(segundo_valor):
    print('Primeiro valor é maior')
else:
    print('O segundo valor é maior')
  
