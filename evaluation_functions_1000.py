import copy
from othello import *

tabela_casas_basilio = {(1,1) : 100, (1,2) : -25, (1,3) : 10, (1,4) : 5, (1,5) : 5, (1,6) : 10, (1,7) : -25, (1,8) : 100,
                        (2,1) : -25, (2,2) : -25, (2,3) : 1, (2,4) : 1, (2,5) : 1, (2,6) : 1, (2,7) : -25, (2,8) : -25,
                        (3,1) : 10, (3,2) : 1, (3,3) : 5, (3,4) : 2, (3,5) : 2, (3,6) : 5, (3,7) : 1, (3,8) : 10,
                        (4,1) : 5, (4,2) : 1, (4,3) : 2, (4,4) : 1, (4,5) : 1, (4,6) : 2, (4,7) : 1, (4,8) : 5,
                        (5,1) : 5, (5,2) : 1, (5,3) : 2, (5,4) : 1, (5,5) : 1, (5,6) : 2, (5,7) : 1, (5,8) : 5,
                        (6,1) : 10, (6,2) : 1, (6,3) : 5, (6,4) : 2, (6,5) : 2, (6,6) : 5, (6,7) : 1, (6,8) : 10,
                        (7,1) : -25, (7,2) : -25, (7,3) : 1, (7,4) : 1, (7,5) : 1, (7,6) : 1, (7,7) : -25, (7,8) : -25,
                        (8,1) : 100, (8,2) : -25, (8,3) : 10, (8,4) : 5, (8,5) : 5, (8,6) : 10, (8,7) : -25, (8,8) : 100}
    
def func_basilio_aux(estado,jogador,tabela) :
    clone=copy.deepcopy(estado)
    if clone.the_end():
        winner=clone.the_winner()
        if winner!=0:
            return infinity if winner==jogador else -infinity
        return 0 # em caso de empate
    # se não reconhecemos o final do jogo:
    soma = 0
    for p,j in clone.board.items() :
        if j == jogador:
            soma += tabela[p]
        else :
            soma -= tabela[p]
    return soma

func_basilio = lambda estado, jogador: func_basilio_aux(estado,jogador,tabela_casas_basilio)

def func_pecas(estado,jogador) :
    clone=copy.deepcopy(estado)
    resultado=clone.number_pieces(jogador)
    return resultado[0]-resultado[1]