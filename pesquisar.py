from database import cursos

def pesquisar_curso():
    termo = input("Digite o nome do curso para buscar: ").lower()
    encontrados = [c for c in cursos if termo in c['nome'].lower()]

    if not encontrados:
        print("Nenhum curso encontrado com esse termo.\n")
    else:
        print("\nCursos encontrados:")
        for c in encontrados:
            print(f"ID: {c['id']} | Nome: {c['nome']} | Carga Horária: {c['carga']}")

if __name__ == "__main__":
    pesquisar_curso("Python")


