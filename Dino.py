class Dinos: 

    def __init__(self, nome, vida, dano, velocidade, habilidade):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.velocidade = velocidade
        self.habilidade = habilidade
    
    def ataque(causador, recebedor):

        vida_final = recebedor.vida - causador.dano

        print(f'dano recebido: {recebedor.vida, causador.dano, vida_final}')

        return vida_final
    
    def mostra_opcoes():
        print('O que você deseja fazer')
        print("[1] Atacar")
        print("[2] Habilidade")
        print("[3] Dado da sorte")
        escolha_opcao = input('Sua escolha: ')
        return escolha_opcao
    

if __name__ == '__main__':
    Dinos.mostra_opcoes()





