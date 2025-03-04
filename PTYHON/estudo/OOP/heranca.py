# Com herança, podemos criar uma classe base (superclasse) e derivar outras subclasses, que 
# herdam seus atributos e métodos, evitando código repetitivo e organizando melhor a 
# estrutura do programa.

# HERANÇA SIMPLES: 

class Animal:   # Superclasse (classe que servirá de base para outras)
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico de animal"


class Cachorro(Animal):  # Herdando atributos e métodos de 'Animal'
    def emitir_som(self):
        return "Au Au!"


class Gato(Animal):  # Herdando atributos e métodos de 'Animal'
    def emitir_som(self):
        return "Miau!"


# Programa:
dog = Cachorro("Rex")
cat = Gato("Mimi")

print(dog.nome, "faz:", dog.emitir_som())  # Rex faz: Au Au!
print(cat.nome, "faz:", cat.emitir_som())  # Mimi faz: Miau!

# USANDO .SUPER():

# A função super() permite acessar métodos da superclasse dentro da subclasse.

class Passaro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)  # Chama o construtor da superclasse
        self.cor = cor

    def descrever(self):
        return f"{self.nome} é um pássaro {self.cor}"


# Programa:
p = Passaro("Azulão", "azul")
print(p.descrever())  # Azulão é um pássaro azul

# HERANÇA MULTIPLA:

class Mamifero:     # Superclasse
    def amamentar(self):
        return "Este animal amamenta seus filhotes."


class Felino:   # Superclasse
    def cacar(self):
        return "Este animal caça presas."


class Leao(Mamifero, Felino):  # Subclasse herdando de duas classes
    def rugir(self):
        return "ROARRR!"


# Programa:
simba = Leao()
print(simba.amamentar())  # Este animal amamenta seus filhotes.
print(simba.cacar())      # Este animal caça presas.
print(simba.rugir())      # ROARRR!
