from Funcoes import *

#Mensagem inicial
print('Paciência Acordeão')
print('==================') 
print()
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')
print()
print('Existem apenas dois movimentos possíveis:')
print()
print('1. Empilhar uma carta sobre a carta imediatamente anterior;') 
print('2. Empilhar uma carta sobre a terceira carta anterior.') 
print()
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:') 
print()
print('1. As duas cartas possuem o mesmo valor ou') 
print('2. As duas cartas possuem o mesmo naipe.') 
print()
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.') 
print()
input('Aperte [Enter] para iniciar o jogo...')

jogo = True
while jogo:
    baralho = cria_baralho()
    print_colorido(baralho)

    jogo = False

