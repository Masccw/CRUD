#Arquivo principal com o menu
from import
from import
from import
from import
from import

while True:
    opcao_curso = int(input("1 - Adicionar curso\n" \         #cadastrar um novo curso (nome, du ração, professor, etc.)
                            "2 - Pesquisar curso\n" \         #procurar curso por nome ou código   
                            "3 - Editar curso\n"\           #atualizar informações de um curso existente
                            "4 - Remover curso\n"\           #excluir curso do sistema
                            "5 - Listar todos os cursos\n"\
                            "6 - Sair → encerrar o programa"))
    if opcao_curso == 1:
        adicionar_curso()
    elif opcao_curso == 2:
        pesquisar_curso()
    elif opcao_curso == 3:
        remover_curso()
    elif opcao_curso == 4:
        remove_curso()
    elif opcao_curso == 5:
        list_curso()
    elif opcao_curso == 6:
        break
    else:
        print("Opção inválida")
     
    

