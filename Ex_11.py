"""
Andar, correr, comer, beber, latir, miar
"""


class Animal:
    def __init__(self, nome, cor, peso, raca):
        self.nome = nome
        self.cor = cor
        self.peso = peso
        self.raca = raca

    def andar(self):
        print(f"{self.nome} está andando.")

    def correr(self):
        print(f"{self.nome} está correndo.")

    def comer(self):
        print(f"{self.nome} está comendo.") 

    def beber(self):
        print(f"{self.nome} está bebendo.")

    def deitar(self):
        print(f"{self.nome} está deitado.")

class Cachorro(Animal):
    def __init__(self, nome, cor, peso, raca):
        super().__init__(nome, cor, peso, raca)

    def latir(self):
        print(f"{self.nome} está latindo: Au! Au! Au!")

    def brincar(self):
        print(f"{self.nome} está brincando.")

class Gato(Animal):
    def __init__(self, nome, cor, peso, raca):
        super().__init__(nome, cor, peso, raca)

    def miar(self):
        print(f"{self.nome} está miando: Miau! Miau!")

    def ronronar(self):
        print(f"{self.nome} está ronronando: Prrrr! Prrrr!")


C1 = Cachorro("Dalia", "Marrom", 20, "Pastor Alemão")
C2 = Cachorro("Sally", "Branca e Marrom", 15, "Beagle")
C3 = Cachorro("Lady", "Preta", 18, "Curly Retriever")
C4 = Cachorro("Margot", "Marrom e Branca", 10, "Shih Tzu")


G1 = Gato("Piu Piu", "Preta e Branca", 1.5, "Frajola")
G2 = Gato("Perséfone", "Laranja", 2, "Bengal")
G3 = Gato("Lyana", "Branca e Cinza", 1.8, "Ragdoll")
G4 = Gato("Alessia", "Cinza", 2.5, "Maine Coon")

C1.deitar()
C2.brincar()
C3.latir()
C4.correr()

G1.correr()
G2.ronronar()
G3.deitar()
G4.miar()