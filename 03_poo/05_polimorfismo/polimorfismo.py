# =-=-=-=-=-=-=-=-= O que é polimorfismo =-=-=-=-=-=-=-=-=
"""
O que é?
  A palavra polimorfismo significa ter muitas formas. Na programação, polimorfismo
significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos
diferentes.
"""

# exemplo
print(len("python"))
print(len([10, 20, 30]))

# =-=-=-=-=-=-=-=-= Polimorfismo com herança =-=-=-=-=-=-=-=-=
"""
Mesmo método com comportamento diferente.
  Na herança, a classe filha herda os métodos da classe pai. No entanto, é possivel
modificar um método em uma classe filha herdada da classe pai. Isso é particulamente
útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente
na classe filha.
"""


class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


# FIXME: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("O avião esta decolando....")


def plano_de_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(Aviao())
