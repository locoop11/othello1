from othello import *
import evaluation_functions_1000 as ef
from evaluation_functions_1000 import *

"""
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
"""



def fruc_pecas_estaveis(estado,jogador) :
    # Stable pieces are ones that can not be flipped by the opponent. Corners are always stable, but also pieces that are in the same row, column or diagonal as a corner, are stable.
    clone=copy.deepcopy(estado)
    
    return resultado[0]-resultado[1]

def func_casas_e_pecas(estado,jogador):
    return ef.func_basilio(estado,jogador) + ef.func_pecas(estado,jogador)


def jogador_1000_v1(jogo,estado) :
    return alphabeta_cutoff_search_new(estado,jogo,3,eval_fn=func_casas_e_pecas)

def jogador_casas_e_pecas_3(jogo,estado) :
    return alphabeta_cutoff_search_new(estado,jogo,3,eval_fn=func_casas_e_pecas)


jogo=Othello()
jogo.display(jogo.initial)


quem_ganhou=0
for i in range(50):
    resultado = jogo.jogar(jogador_1000_v1,jogador_casas_e_pecas_3,verbose=False)
    print(resultado)
    quem_ganhou += resultado[2]
print(quem_ganhou)