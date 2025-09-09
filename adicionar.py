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