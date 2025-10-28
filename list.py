#Função para listar cursos
from database import cursos

class List:
    @staticmethod
    def listar_cursos():
        if not cursos:
            print("Nenhum curso cadastrado.\n")
            return
   
        print("\n=== Lista de Cursos ===")
        for curso in cursos:
            print(f"ID: {curso.id} | Nome: {curso.nome} | Descrição: {curso.descricao} | Carga Horária: {curso.carga}")



