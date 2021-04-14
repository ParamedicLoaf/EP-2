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