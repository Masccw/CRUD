#Arquivo principal com o menu
from adicionar import adicionar_curso
from pesquisar import pesquisar_curso
from edit import atualizar_curso
from remove import remover_curso
from list import listar_cursos

while True:
    try:
        opcao_curso = int(input("1 - Adicionar curso\n"          
                            "2 - Pesquisar curso\n"       
                            "3 - Editar curso\n"         
                            "4 - Remover curso\n"         
                            "5 - Listar todos os cursos\n"
                            "6 - Sair → encerrar o programa\n"
                            "Escolha uma opção: "
                            ))
    except ValueError:
        print("Somente números")
        continue

    if opcao_curso == 1:
        nome = input("Digite o nome do curso novo: ")
        descricao = input("Digite a descrição do curso novo: ")
        carga = input("Digite a carga do curso novo: ")
        adicionar_curso(nome, descricao, carga)
    elif opcao_curso == 2:
       pesquisar_curso()
    elif opcao_curso == 3:
       atualizar_curso()
    elif opcao_curso == 4:
       try:
        id_curso = int(input("Digite o ID do curso que deseja remover: "))
        remover_curso(id_curso)
       except ValueError:
        print("ID inválido! Digite apenas números.")
    elif opcao_curso == 5:
       listar_cursos()
    elif opcao_curso == 6:
       print("Programa encerrando...")
       break
    else:
       print("Opção inválida. Tente novamente")

