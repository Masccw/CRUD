#Função para listar cursos
from database import cursos

def listar_cursos():
    if not cursos:
        print("Nenhum curso cadastrado.\n")
        

    print("\n=== Lista de Cursos ===")
    for curso in cursos[1:6]:
        print(f"ID: {curso['id']} | Nome: {curso['nome']} | Carga Horária: {curso['carga']}")
    return curso

listar_cursos()