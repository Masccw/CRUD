#Função de editar items
# Lista de cursos
cursos = [
    {"id": 1, "nome": "Python Básico", "descrição": "Introdução ao Python", "carga": "40h"},
    {"id": 2, "nome": "HTML - CSS", "descrição": "Do básico ao avançado em HTML e CSS", "carga": "60h"},
    {"id": 3, "nome": "JS - JavaScript Básico", "descrição": "Introdução a JS", "carga": "40h"},
    {"id": 4, "nome": "SQL", "descrição": "Do básico ao avançado SQL", "carga": "60h"},
    {"id": 5, "nome": "Java", "descrição": "Do básico ao avançado em Java", "carga": "80h"},
    {"id": 6, "nome": "PHP básico", "descrição": "Introdução a PHP", "carga": "40h"},
]

def atualizar_curso():
    try:
        id_curso = int(input("Digite o ID do curso que deseja atualizar: "))
    except ValueError:
        print("ID inválido! Digite apenas números.")
        return
    
    for curso in cursos:
        if curso["id"] == id_curso:
            print(f"\nCurso encontrado: {curso['nome']}")
            print("Deixe em branco para não alterar um campo.\n")
            
            novo_nome = input(f"Novo nome ({curso['nome']}): ") or curso["nome"]
            nova_descricao = input(f"Nova descrição ({curso['descrição']}): ") or curso["descrição"]
            nova_carga = input(f"Nova carga horária ({curso['carga']}): ") or curso["carga"]

            curso["nome"] = novo_nome
            curso["descrição"] = nova_descricao
            curso["carga"] = nova_carga

            print("\n✅ Curso atualizado com sucesso!")
            print(curso)
            return
    
    print("Curso não encontrado!")
