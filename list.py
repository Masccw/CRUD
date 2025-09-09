#Função para listar cursos
from database import cursos

def listar_cursos():
    if not cursos:
        print("Nenhum curso cadastrado.\n")
    return
        
    print("\n=== Lista de Cursos ===")
    for curso in cursos:
        print(curso)

if __name__ == "__main__":
    listar_cursos()
