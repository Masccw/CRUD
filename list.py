#Função para listar cursos
from database import cursos

def listar_cursos():
    if not cursos:
        print("Nenhum curso cadastrado.\n")
        return
   
    print("\n=== Lista de Cursos ===")
    for curso in cursos:
        print(f"ID: {curso['id']} | Nome: {curso['nome']} | Descrição: {curso['descrição']} | Carga Horária: {curso['carga']}")

if __name__ == "__main__":
    listar_cursos()

