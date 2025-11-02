class Veiculo:
    def __init__(self, cor, placa, numero_roda):
        self.cor = cor
        self.placa = placa
        self.numero_roda = numero_roda

    def ligar_motor(self):
        print('Ligando o motor')


class Motocicleta(Veiculo):
    ...


class Carro(Veiculo):
    ...


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_roda, carregado: bool):
        super().__init__(cor, placa, numero_roda)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'Caminhão carregado: {'Sim' if self.carregado else 'Não'}')


moto = Motocicleta('preta', 'ABC-1234', 2)
moto.ligar_motor()

carro = Carro('branco', 'XDE-0098', 4)
carro.ligar_motor()

caminhao = Caminhao('roxo', 'GFD-8712', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao.cor)
