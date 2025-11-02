class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self):
        print('Plim plim...')

    def parar(self):
        print('Parando a bicicleta!')
        print('Bicicleta Parada.')

    def correr(self):
        print('Vrummmmmm...')

    def tracar_marcha(self, nro_marcha):
        print('Trocando marcha')

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                self.marcha = nro_marcha
                print('Marcha trocada')
            else:
                print('Não foi possivel trocar a marcha')

    # def __str__(self):
    #     return f'Bicicleta: {self.cor}, {self.modelo}, {self.ano}, R$:{self.valor:.2f}'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.cor}, {self.modelo}, {self.ano}, R$:{self.valor:.2f}'

    # def __str__(self):
    #     return f'{self.__class__.__name__}: {', '.join([f'{valor}' for valor in self.__dict__.values()])}'


b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1)
