#Encapsulamento
class Aluno:
    def __init__(self, nome): #metodo
        self.nome = nome
        self.notas = []
        
    def adicionar_notas(self,notas):
        self.notas.append(notas)
    
    def calcular_media(self):
        total = sum(self.notas) #sum é uma função
        media = total/len(self.notas)
        return media
    
    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "APROVADO"
        elif media >= 5:
            return "RECUPERAÇÃO"
        else:
            return "REPROVADO"

aluno1 = Aluno("Layssa")
aluno1.adicionar_notas(7)
aluno1.adicionar_notas(8)
aluno1.adicionar_notas(9)
print("Média do aluno:", aluno1.nome, aluno1.calcular_media())
print("Situação do aluno:", aluno1.nome, aluno1.verificar_situacao())