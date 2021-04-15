import random

def cria_baralho():
    baralho = ['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥', 'A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠']

    random.shuffle(baralho)
    
    return baralho

def extrai_naipe(carta):
    return carta[len(carta)-1]

def extrai_valor(carta):
    valor = ''
    for i in range(len(carta)-1):
        valor += carta[i]
        
    return valor

def lista_movimentos_possiveis(baralho, indice):
    movimentos = []

    if indice == 0:
        return movimentos
    elif indice < 3:
        if (extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-1])) or (extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-1])):
            movimentos.append(1)
    else:
        if (extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-1])) or (extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-1])):
            movimentos.append(1)

        if (extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-3])) or (extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-3])):
            movimentos.append(3)
    
    return movimentos

def empilha(baralho, origem, destino):
    carta = baralho[origem]
    del baralho[origem]
    baralho[destino] = carta

    return baralho

def possui_movimentos_possiveis(baralho):
    for carta in baralho:
        if lista_movimentos_possiveis(baralho, baralho.index(carta)) != []:
            return True
    
    return False

def print_colorido(baralho):
    for carta in baralho:
        naipe = extrai_naipe(carta)

        if naipe == '♣':
            #verde
            colorida = '\033[1;32;40m' + formatacao_da_carta(carta) + '\033[0;37;40m'
        elif naipe == '♦':
            #roxo
            colorida = '\033[1;35;40m' + formatacao_da_carta(carta) + '\033[0;37;40m'
        elif naipe == '♥':
            #vermelho
            colorida = '\033[1;31;40m' + formatacao_da_carta(carta) + '\033[0;37;40m'
        else:
            #amarelo
            colorida = '\033[1;33;40m' + formatacao_da_carta(carta) + '\033[0;37;40m'
        
        posicao = formatacao_do_numero(baralho, carta)

        print('{0}. {1}'.format(posicao, colorida))

    print()

def formatacao_da_carta(carta):
    if len(carta) < 3:
        return ' '+carta
    else:
        return carta

def formatacao_do_numero(baralho, carta):
    if baralho.index(carta)+1 < 10:
        posicao = ' '+ str(baralho.index(carta)+1)
    else:
        posicao = str(baralho.index(carta)+1)
    
    return posicao