
class Aluno:
   
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome                                          #atributos
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def apresentar(self):                                         #metodos
        print("Olá, meu nome é: ",self.nome)
        
    def media(self):
        m = (self.nota1 + self.nota2 + self.nota3)/3
        print ("A media das minhas notas é: ",m)
        if m > 7:
            print("Aprovado por média")
        else:
            print("Reprovado por média")
        
pessoa1 = Aluno("Layssa",7,7,7)                  #objeto
pessoa1.apresentar()
pessoa1.media()
