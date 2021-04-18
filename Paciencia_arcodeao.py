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

    print()
    print('Estado atual do baralho:')
    print_colorido(baralho)

    while possui_movimentos_possiveis(baralho):
        escolha = input('Escolha uma carta (digite um número entre 1 e {0}): '.format(len(baralho)))
        while not escolha in range_em_strings(baralho):
            escolha = input('Posição inválida. Por favor, escolha um número entre 1 e {0}: '.format(len(baralho)))

        carta = baralho[int(escolha)-1]

        while len(lista_movimentos_possiveis(baralho, baralho.index(carta))) == 0:
            escolha = input('A carta {0} não pode se movida. Por favor, escolha um número entre 1 e {1}: '.format(carta_colorida(carta), len(baralho)))
            
            while not escolha in range_em_strings(baralho):
                escolha = input('Posição inválida. Por favor, escolha um número entre 1 e {0}: '.format(len(baralho)))
            
            carta = baralho[int(escolha)-1]
        
        movimentos = lista_movimentos_possiveis(baralho, baralho.index(carta))
        if len(movimentos) == 1:
            baralho = empilha(baralho, baralho.index(carta), baralho.index(carta)-movimentos[0])
        else:
            print('Sobre qual carta você quer empilhar o {0}?'.format(carta_colorida(carta)))
            opcoes = [baralho[baralho.index(carta)-movimentos[0]],baralho[baralho.index(carta)-movimentos[1]]]
            print_colorido(opcoes)
            escolha = input('Digite o número de sua escolha (1 ou 2): ')

            while escolha != '1' and escolha != '2':
                print('Opção inválida. Sobre qual carta você quer empilhar o {0}?'.format(carta_colorida(carta)))
                opcoes = [baralho[baralho.index(carta)-movimentos[0]],baralho[baralho.index(carta)-movimentos[1]]]
                print_colorido(opcoes)
                escolha = input('Digite o número de sua escolha (1 ou 2): ')

            escolha = int(escolha)

            if escolha == 1:
                baralho = empilha(baralho, baralho.index(carta), baralho.index(carta)-movimentos[0])
            else:
                baralho = empilha(baralho, baralho.index(carta), baralho.index(carta)-movimentos[1])

        print()
        print('Estado atual do baralho:')
        print_colorido(baralho)

    if len(baralho) == 1:
        print('Parabéns, você venceu e tem muita paciência!')
    else:
        print('Não há mais movimentos possíveis. Você perdeu.')
    
    print()
    de_novo = input('Deseja jogar novamente? (s/n): ')

    while de_novo != 's' and de_novo != 'n':
        de_novo = input('Opção inválida. Deseja jogar novamente? (Digite s para sim e n para não): ')
    
    if de_novo == 'n':
        jogo = False

print()
print('Até a próxima!')