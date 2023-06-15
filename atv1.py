# CLASSE

class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome                            #atributos
        self.idade = idade
        self.cpf = cpf
    
    def apresentar(self):                          #metodos
        print("Olá, meu nome é: ",self.nome)
    
    def envelhecer(self, anos):
        self.idade += anos
        print("Minha idade é: ",self.idade)
        
    def mostrar_cpf(self):
        print("Este é meu cpf: ",self.cpf)
        
pessoa1 = Pessoa("Layssa", 23, "12345678900")      #objeto
pessoa1.apresentar()
pessoa1.envelhecer(2)
pessoa1.mostrar_cpf()
