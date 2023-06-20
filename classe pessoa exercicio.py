'''Crie em python as classes de um sistema de uma universidade que tem como atores:
Professores;
Alunos;
Secretariado;
Terceirizados.'''

class Pessoa:
    def __init__(self, nome, idade, turno, disciplina, codigo, salario, departamento):
        self.nome = nome
        self.idade = idade
        self.turno = turno
        self.disciplina = disciplina
        self.codigo = codigo
        self.salario = salario
        self.departamento = departamento
    

