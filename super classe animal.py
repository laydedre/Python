
class Animal: #super classe
    def __init__(self, nome, idade):
        self.nome = nome #atributos
        self.idade = idade
        
    def fazer_barulho(self): #metodo
        print("O animal faz barulho")
    
class Cachorro(Animal):
    def __init__(self, nome, idade, raca): #herdando os atributos nome e idade da classe Animal e raca é um atributo individual da classe Cachorro
        super().__init__(nome, idade)
        self.raca = raca
    
    def abana_rabo(self): 
        print("O",self.nome,"está abanando o rabo")
        
class Gato(Animal):
    def ronronar(self):
        print("O",self.nome,"está ronronando")
        
cachorro1 = Cachorro("Rex", 5, "Pitbull")
cachorro1.fazer_barulho()
cachorro1.abana_rabo()

gato1 = Gato("Binzin", 5)
gato1.fazer_barulho()
gato1.ronronar()


