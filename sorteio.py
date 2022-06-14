import random
participante1 = str(input('Digite um nome: '))
participante2 = str(input('Digite um nome: '))
participante3 = str(input('Digite um nome: '))
participante4 = str(input('Digite um nome: '))
lista = (participante1, participante2, participante3, participante4)
sorteio = random.choice(lista)
print('O sorteado é: {}!'.format(sorteio))
