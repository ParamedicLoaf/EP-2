import random
from Funcoes import *
l = [0, 'bolacha', 2, 'bola', 4]
print(l)
# [0, 1, 2, 3, 4]

random.shuffle(l)
print(l)
# [4, 3, 2, 1, 0]

print("\033[1;32;40m4") #Verde
print("\033[1;31;40m4") #Vermelho
print("\033[1;35;40m4") #Roxo
print("\033[1;33;40m4") #Amarelo
print("\033[0;37;40m4") #Normal

print(extrai_naipe('A♣'))
print(extrai_valor('A♣'))
cria_baralho()
baralho = ['6♥', 'J♥', '9♣', '9♥']

print(lista_movimentos_possiveis(baralho,3))

print(int(' 1'))