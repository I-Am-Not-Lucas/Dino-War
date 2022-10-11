import imp
from Dino import Dinos
from random import randint

Dinos.bem_vindo()

escolha_jogador = Dinos.cria_seu_dino(Dinos.escolha_dino()) #filtra o resultado

oponente = Dinos.cria_oponente(randint(1, 3))

Dinos.mostra_caracter(escolha_jogador) ## i need finish the text here...

opcao_luta = Dinos.mostra_opcoes()
    