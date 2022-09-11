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

def mostra_caracter(object): # How can i change the objetc here to return another thing
    

    print(object.nome)

    print(object.vida)

    print(object.velocidade)

    print(object.habilidade)

def duel (escolha, oponente): # 1 = is player / 2 = oponent

    vez = 0


    turno_player1 = escolha.velocidade
    turno_player2 = oponente.velocidade

    while escolha.vida > 0 and oponente.vida > 0:

        

        while turno_player1 < 20 and turno_player2 < 20:

            turno_player1 += turno_player1
            turno_player2 += turno_player2

            print(turno_player1, turno_player2)
        
        
        

    print('Saiu loop')


    # if turno_player1 > turno_player2:

    #     vez = 1 

    # if turno_player2 >= 20 and turno_player2 > turno_player1:

    #     vez = 2
    
    # else:

    #     vez = randint(1,2)


    

    






    



    

if __name__ == "__main__":

    bem_vindo()
    teste_escolha = escolha_dino()
  
