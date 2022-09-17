# criar o objeto dino / criar o ponente
from Dino import *
from random import randint

def bem_vindo():
    print('-' * 23)
    print("Bem vindo ao dino war!")
    print('-' * 23)


def escolha_dino():

    filtro = lambda escolha: escolha.isnumeric()
    resultado = False
    
    print("[1] Tiranossauro Rex")
    print("[2] Velociraptor")
    print("[3] Triceratops")

    while resultado != True:

        escolha = input("Qual dino vc quer usar?")

        resultado = filtro(escolha)     
    
    return escolha

def cria_seu_dino(jogador):

    if int(jogador) == 1:

        jogador = Dinos('Tiranossauro Rex', 2000, 300, 5, 'Rugido ensurdecedor')
        
        return jogador

    if int(jogador) == 2:

        jogador = Dinos('Velociraptor', 1500, 200, 7, 'Sorrateiro')
        
        return jogador
    
    if int(jogador) == 3:

        jogador = Dinos('Triceratops', 3000, 150, 5, 'armadura de ferro')
        
        return jogador

def cria_oponente(random_number):

    #print(random_number)

    if int(random_number) == 1:

        random_number = Dinos('Tiranossauro Rex', 2000, 300, 5, 'Rugido ensurdecedor')
        
        return random_number

    if int(random_number) == 2:

        random_number = Dinos('Velociraptor', 1500, 200, 7, 'Sorrateiro')
        
        return random_number
    
    if int(random_number) == 3:

        random_number = Dinos('Triceratops', 3000, 150, 5, 'armadura de ferro')
        
        return random_number

    else:
        return "algo deu errado"

def mostra_caracter(object): # How can i change the objetc here to return another thing / change the text
    
    print('*' * 30)
    print(f'Nome: {object.nome}')

    print(f'vida: ', end="")
    print(object.vida)

    print("Velocidade: ", end='')
    print(object.velocidade)

    print("Habilidade: ", end="")
    print(object.habilidade)

    print('*' * 30)
def duel (escolha, oponente): # 1 = is player / 2 = machine

    vez = 0


    turno_player1 = escolha.velocidade
    turno_maquina = oponente.velocidade

    while escolha.vida > 0 and oponente.vida > 0:
        

        while turno_player1 < 20 and turno_maquina < 20:

            turno_player1 += turno_player1
            turno_maquina += turno_maquina

        if turno_player1 >= turno_maquina: # duel itself
            Dinos.ataque(escolha,oponente)
            break

        else:
            Dinos.ataque(oponente, escolha)
            break


