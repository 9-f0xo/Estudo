# 'Métodos' são funções definidas dentro de uma classe, geralmente os métodos usam 'self' que representa a instância atual e serve para acessarem atributos e outros métodos da classe.

# Exemplo:
class MinhaClasse:
    def meu_metodo(self):
        return "Olá, mundo!"

objeto = MinhaClasse() # Instanciando (criando um objeto)
print(objeto.meu_metodo()) # Chamando o método
# Nesse caso, a classe tem um método chamado 'meu_metodo' que retorna uma string 'Olá, mundo!'



''' 
Métodos Especiais:
__init__: O construtor, chamado ao criar uma nova instância da classe.
__str__: Define a representação em string de um objeto (usado pela função print()).
__repr__: Define uma representação não ambígua do objeto (usado por repr()).
__eq__: Define o comportamento do operador de igualdade (==).
__lt__: Define o comportamento do operador de menor que (<).
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Pessoa: {self.nome}, {self.idade} anos"

    def __eq__(self, outra_pessoa):
        return self.nome == outra_pessoa.nome and self.idade == outra_pessoa.idade

# Criando novas instâncias
pessoa1 = Pessoa("Foxo", 16)
pessoa2 = Pessoa("Yan", 17)

# Usando __str__ com print
print(pessoa1)  # Saída: Pessoa: Foxo, 15 anos

# Usando __eq__ para comparação
print(pessoa1 == pessoa2)  # Saída: False



# Métodos de Classe e Métodos Estáticos:
# @classmethod recebe a própria classe como primeiro parâmetro, convencionalmente chamado de cls.
class MinhaClasse:
    contador = 0

    def __init__(self):
        MinhaClasse.contador += 1

    @classmethod
    def obter_contador(cls):
        return cls.contador
    # Neste exemplo, 'obter_contador' é um método de classe que retorna o número de instâncias criadas da classe MinhaClasse.

# '@staticmethod' não recebem automaticamente nenhum parâmetro adicional (nem a instância, nem a classe) e funcionam como funções normais dentro do contexto da classe.
class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b
    # Essa função pode ser chamada a qualquer momento pela classe ou pela instância

'''
Métodos Privados:
O prefixo '__' indica que ele é destinado ao uso interno da classe. Isso é conhecido como name mangling, onde o interpretador Python altera o nome do método para incluir o nome da classe, dificultando o acesso externo.
'''
class MinhaClasse:
    def __meu_metodo_privado(self):
        return "Este é um método privado."

# Para acessar este método fora da classe, seria necessário usar o nome modificado:
objeto = MinhaClasse()
print(objeto._MinhaClasse__meu_metodo_privado())

