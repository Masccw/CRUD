#Onde você guarda a lista de dados
class Curso:
    def __init__(self, id, nome, descricao, carga):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.carga = carga
    
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Descrição: {self.descricao} | Carga Horária: {self.carga}"
    
cursos = []
