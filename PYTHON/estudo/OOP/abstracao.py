# A abstração serve para ocultarmos detalhes de uma classe, focando apenas no que a classe
# deve fazer ao invés de como fazer. É como um carro, você sabe dirigir , mas não precisa
# entender de motor para pilotá-lo.

# --------------------------------Quando usar Abstração?--------------------------------
# Quando quer criar uma estrutura comum para várias classes.
# Quando quer evitar código repetitivo e garantir que todas as classes sigam um padrão.
# Quando quer esconder detalhes desnecessários e deixar o código mais intuitivo.

from abc import ABC, abstractmethod


class Forma(ABC):  # Classe abstrata

    # (Note que a classe abstrata não possui atributos.)

    @abstractmethod # Declaração de um método abstrato
    def area(self):
        pass

    @abstractmethod # Declaração de um método abstrato
    def perimetro(self):
        pass


class Quadrado(Forma):  # Implementando a abstração
    def __init__(self, lado):
        self.lado = lado

    def area(self): # A classe que herda os métodos de 'Forma' deve implementá-los.
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

# Programa:

quadrado1 = Quadrado(2)
print(quadrado1.area())
print(quadrado1.perimetro())
