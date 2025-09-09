#Função de editar items
from database import cursos

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
            return
    
    print("Curso não encontrado!")

if __name__ == "__main__":
    atualizar_curso()

