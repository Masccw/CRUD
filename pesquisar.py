from database import cursos

class Search:
    @staticmethod
    def pesquisar_curso():
        if not cursos:
            print("Nenhum curso cadastrado")
            return
        
        termo = input("Digite o nome do curso para buscar: ").lower()
        encontrados = [c for c in cursos if termo in c.nome.lower()]

        if not encontrados:
            print("Nenhum curso encontrado com esse termo.\n")
        else:
            print("\nCursos encontrados:")
            for curso in encontrados:
                print(curso)




