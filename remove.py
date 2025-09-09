#Função de remover items
from database import cursos

def remover_curso(id_curso):
    global cursos
    for i, curso in enumerate(cursos):
        if curso["id"] == id_curso:
            curso_removido = cursos.pop(i)
            print(f"Curso '{curso_removido['nome']}' (ID {id_curso}) removido com sucesso!")
            return
    print(f"Curso com ID {id_curso} não encontrado.")

