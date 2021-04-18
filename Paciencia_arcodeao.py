from Funcoes import *

#mensagem inicial
print()
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

#jogo principal
jogo = True
while jogo:
    #cria o baralho e printa
    baralho = cria_baralho()

    print()
    print('Estado atual do baralho:')
    print_colorido(baralho)

    #analisa se o baralho tem movimentos possíves e continua a partida enquanto tiver
    while possui_movimentos_possiveis(baralho):

        #pede um número para o usuário que represente uma carta do baralho
        escolha = input('Escolha uma carta (digite um número entre 1 e {0}): '.format(len(baralho)))

        #garante que a escolha seja um número válido antes de tentar transformar a escolha em um int
        while not escolha in range_em_strings(baralho):
            escolha = input('Posição inválida. Por favor, escolha um número entre 1 e {0}: '.format(len(baralho)))

        carta = baralho[int(escolha)-1]

        #garante que a carta escolhida tenha movimentos possíveis
        while len(lista_movimentos_possiveis(baralho, baralho.index(carta))) == 0:
            escolha = input('A carta {0} não pode se movida. Por favor, escolha um número entre 1 e {1}: '.format(carta_colorida(carta), len(baralho)))
            
            #garante (de novo) que a escolha seja um número válido antes de tentar transformar a escolha em um int
            while not escolha in range_em_strings(baralho):
                escolha = input('Posição inválida. Por favor, escolha um número entre 1 e {0}: '.format(len(baralho)))
            
            carta = baralho[int(escolha)-1]
        
        #cria uma lista de movimentos da carta
        movimentos = lista_movimentos_possiveis(baralho, baralho.index(carta))

        #se a carta tiver apenas um movimento, empilhar a carta. Se tiver mais de um, perguntar ao usuário o movimento preferido.
        if len(movimentos) == 1:
            baralho = empilha(baralho, baralho.index(carta), baralho.index(carta)-movimentos[0])
        else:
            print('Sobre qual carta você quer empilhar o {0}?'.format(carta_colorida(carta)))
            opcoes = [baralho[baralho.index(carta)-movimentos[0]],baralho[baralho.index(carta)-movimentos[1]]]
            print_colorido(opcoes)
            escolha = input('Digite o número de sua escolha (1 ou 2): ')

            #garante que o movimento escolhido seja válido
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

    #analisa o baralho e diz se o usuário venceu ou não
    if len(baralho) == 1:
        print('Parabéns, você venceu e tem muita paciência!')
    else:
        print('Não há mais movimentos possíveis. Você perdeu.')
    
    print()

    #pergunta se o usuário quer jogar de novo
    de_novo = input('Deseja jogar novamente? (s/n): ')

    #garante que a escolha seja válida
    while de_novo != 's' and de_novo != 'n':
        de_novo = input('Opção inválida. Deseja jogar novamente? (Digite s para sim e n para não): ')
    
    if de_novo == 'n':
        jogo = False
    else:
        print('Vamos lá!')
        print()

#mensagem de despedida
print()
print('Até a próxima!')