class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} -> {valor}' for chave, valor in self.__dict__.items()])}'


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico


class Gato(Mamifero):
    pass


class Ornintorrinco(Mamifero, Ave):
    def __init__(self, nro_patas, cor_pelo, cor_bico):
        print(Ornintorrinco.mro())
        print(Ornintorrinco.__mro__)

        super().__init__(nro_patas=nro_patas, cor_pelo=cor_pelo, cor_bico=cor_bico)


gato = Gato(nro_patas=4, cor_pelo='Preto')
print(gato)

ornintorrinco = Ornintorrinco(nro_patas=4, cor_pelo='Verde', cor_bico='Laranja')
print(ornintorrinco)
