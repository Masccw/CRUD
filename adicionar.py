#Função de adicionar items
from database import Curso, cursos

class Add:
    @staticmethod
    def adicionar_curso(nome, descricao, carga):
        novo_id = cursos[-1].id + 1 if cursos else 1 
        novo_curso = Curso(novo_id, nome, descricao, carga) 
        cursos.append(novo_curso)
        print(f"Curso '{nome}' adicionado com sucesso!")
        return novo_curso

