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