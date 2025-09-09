#Função de remover items
from database import cursos

def remover_curso(id_curso):
    for i, curso in enumerate(cursos):
        if curso["id"] == id_curso:
            curso_removido = cursos.pop(i)
            print(f"Curso '{curso_removido['nome']}' (ID {id_curso}) removido com sucesso!")
            return
    print(f"Curso com ID {id_curso} não encontrado.")

if __name__ == "__main__":
    try:
        id_curso = int(input("Digite o ID do curso que deseja remover: "))
        remover_curso(id_curso)
    except ValueError:
        print("ID inválido! Digite apenas números.")
