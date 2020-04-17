class Motor():
    def __init__(self, velocidade = 0):
        self.velocidade=velocidade
    def acelerar(self):
        self.velocidade +=1
        return print('Velocidade atual:',self.velocidade,'km/h')
    def frear(self):
        if self.velocidade - 2 < 0:
            self.velocidade=0
            return print('Você parou:', self.velocidade, 'km/h')
        else:
            self.velocidade-=2
            if self.velocidade ==0:
                return print('Você está parado:', self.velocidade,'km/h')
            else:
                return print('Velocidade atual:', self.velocidade, 'km/h')

class Volante():
    def __init__(self, direcao='Norte'):
        self.direcao = direcao

    def girar_a_direita(self):
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
            print('Direcao após virar à direita:', self.direcao)
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
            print('Direcao após virar à direita:', self.direcao)
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
            print('Direcao após virar à direita:', self.direcao)
        else:
            self.direcao = 'Norte'
            print('Direcao após virar à direira:', self.direcao)

    def girar_a_esq(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
            print('Direcao após virar à esquerda:', self.direcao)
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
            print('Direcao após virar à esquerda:', self.direcao)
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
            print('Direcao após virar à esquerda:', self.direcao)
        else:
            self.direcao = 'Norte'
            print('Direcao após virar à esquerda:', self.direcao)
class Carro():
    def __init__(self,motor,volante):
        self.motor = motor
        self.volante = volante

    def velocimetro(self):
        return self.motor.velocidade
    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return self.motor.frear()

    def caminho(self):
        return self.volante.direcao
    def girar_a_direita(self):
        return self.volante.girar_a_direita()
    def girar_a_esq(self):
        return self.volante.girar_a_esq()
if __name__ == '__main__':
    trajeto = int(input('Esclha entre o trajeto 1 ou 2:'))
    print('Trajeto escolhido: ',trajeto)
    if trajeto == 1:
            motor = Motor()
            volante = Volante()
            carro = Carro(motor,volante)
            print('Iniciando trajeto 1:')
            print(carro.caminho())
            print(carro.velocimetro())
            carro.acelerar()
            carro.acelerar()
            carro.acelerar()
            carro.acelerar()
            carro.acelerar()
            carro.acelerar()
            carro.frear()
            carro.girar_a_esq()
            carro.acelerar()
            carro.acelerar()
            carro.frear()
            carro.girar_a_esq()
            carro.acelerar()
            carro.acelerar()
            carro.frear()
            carro.girar_a_direita()
            carro.acelerar()
            carro.acelerar()
            carro.frear()
            carro.girar_a_esq()
            carro.frear()
            carro.frear()
            print('Chegada ao destino')

    elif trajeto ==2:
        motor = Motor()
        volante = Volante()
        carro = Carro(motor, volante)
        print('Iniciando trajeto 2:')
        print(carro.caminho())
        print(carro.velocimetro())
        carro.acelerar()
        carro.acelerar()
        carro.acelerar()
        carro.acelerar()
        carro.acelerar()
        carro.acelerar()
        carro.frear()
        carro.girar_a_direita()
        carro.acelerar()
        carro.acelerar()
        carro.frear()
        carro.girar_a_direita()
        carro.acelerar()
        carro.acelerar()
        carro.frear()
        carro.girar_a_direita()
        carro.acelerar()
        carro.acelerar()
        carro.frear()
        carro.girar_a_esq()
        carro.frear()
        carro.frear()
        print('Chegada ao destino')
    else:
        print('Trajeto não cadastrado.')
