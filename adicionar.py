#Função de adicionar items
from database import cursos

def adicionar_curso(nome, descricao, carga):
    global cursos
    novo_id = cursos[-1]["id"] + 1 if cursos else 1  
    novo_curso = {
        "id": novo_id,
        "nome": nome,
        "descrição": descricao,
        "carga": carga
    }
    cursos.append(novo_curso)
    print(f"Curso '{nome}' adicionado com sucesso!")
    return novo_id, novo_curso

# Teste isolado (só roda se executar adicionar.py diretamente)
if __name__ == "__main__":
    novo_id, novo_curso = adicionar_curso( "C", "Curso de C", "100h")
    print("ID: ", novo_id)
    print("Curso: ", novo_curso)
    