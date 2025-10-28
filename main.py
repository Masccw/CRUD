#Arquivo principal com o menu
from adicionar import Add
from pesquisar import Search
from edit import Edit
from remove import Remove
from list import List

while True:
    print(
        "\n---Menu de cursos---\n"
        "1 - Adicionar curso\n"
        "2 - Pesquisar curso\n"
        "3 - Editar curso\n"
        "4 - Remover curso\n"
        "5 - Listar todos os cursos\n"
        "6 - Sair → encerrar o programa\n"
    )
    try:
        opcao_curso = int(input("Escolha uma opção: "))
    except ValueError:
        print("Somente números")
        continue

    if opcao_curso == 1:
        nome = input("Digite o nome do curso novo: ")
        descricao = input("Digite a descrição do curso novo: ")
        carga = input("Digite a carga do curso novo: ")
        Add.adicionar_curso(nome, descricao, carga)
    elif opcao_curso == 2:
        Search.pesquisar_curso()
    elif opcao_curso == 3:
        Edit.atualizar_curso()
    elif opcao_curso == 4:
        try:
            id_curso = int(input("Digite o ID do curso que deseja remover: "))
            Remove.remover_curso(id_curso)
        except ValueError:
            print("ID inválido! Digite apenas números.")
    elif opcao_curso == 5:
        List.listar_cursos()
    elif opcao_curso == 6:
        print("Programa encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente")


