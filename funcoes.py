# escolher o dino / filtrar a escolha

def bem_vindo(nome="teste"):
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
    
        print(resultado)





if __name__ == "__main__":

    bem_vindo()
    teste_escolha = escolha_dino()
  
