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





