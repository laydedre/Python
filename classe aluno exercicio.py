'''Crie a classe aluno com atributos e métodos para dizer se ele está aprovado ou não:
São feitas 3 avaliações;
A média final é 7;
Se o aluno fizer mais de 15 pontos e menos de 21 deve ser informado que ele fará prova final;
Ele deve ter que menos que 20 faltas para ser aprovado. '''

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.faltas
       
    def adicionar_notas(self,notas):
        if len(notas) > 3: #até 3 notas o programa não pede mais notas
            print("3 NOTAS LANÇADAS")
        self.notas.append(notas)
        
    def calcular_media(self):
        total = sum(self.notas)
        media = total/3
        return media
    
    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "APROVADO"
        elif media > 5 and media < 7:
            print("RECUPERAÇÃO")
        else:
            return "REPROVADO"
    
    def calcular_faltas(self, faltas):
        faltas = self.faltas
        if faltas > 20:
            print("APROVADO")