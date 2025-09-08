cursos = []
contador_id = 1

def adicionar_curso():
    global contador_id
    nome = input("Nome do curso: ")
    descricao = input("Descrição: ")
    carga_horaria = input("Carga horária (em horas): ")

    curso = {
        "id": contador_id,
        "nome": nome,
        "descricao": descricao,
        "carga_horaria": carga_horaria
    }

    cursos.append(curso)
    contador_id += 1
    print("Curso adicionado com sucesso!\n")

def listar_cursos():
    if not cursos:
        print("Nenhum curso cadastrado.\n")
        return

    print("\n=== Lista de Cursos ===")
    for curso in cursos:
        print(f"ID: {curso['id']} | Nome: {curso['nome']} | Carga Horária: {curso['carga_horaria']}h")
    print()

def pesquisar_curso():
    termo = input("Digite o nome do curso para buscar: ").lower()
    encontrados = [c for c in cursos if termo in c['nome'].lower()]

    if not encontrados:
        print("Nenhum curso encontrado com esse termo.\n")
    else:
        print("\nCursos encontrados:")
        for c in encontrados:
            print(f"ID: {c['id']} | Nome: {c['nome']} | Carga Horária: {c['carga_horaria']}h")
        print()

def menu():
    while True:
        print("=== MENU CURSOS ===")
        print("1. Adicionar curso")
        print("2. Listar cursos")
        print("3. Pesquisar curso")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_curso()
        elif opcao == "2":
            listar_cursos()
        elif opcao == "3":
            pesquisar_curso()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


