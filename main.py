#Arquivo principal com o menu
from adicionar import adicionar_curso
from pesquisar import pesquisar_curso
from edit import edit_curso
from remove import remove_curso
from database import list_curso

while True:
                           # 1 - cadastrar um novo curso (nome, duração, professor, etc.)
                           # 2 - procurar curso por nome ou código
                           # 3 - atualizar informações de um curso existente
                           # 4 - excluir curso do sistema
    opcao_curso = int(input("1 - Adicionar curso\n"          
                            "2 - Pesquisar curso\n"       
                            "3 - Editar curso\n"         
                            "4 - Remover curso\n"         
                            "5 - Listar todos os cursos\n"
                            "6 - Sair → encerrar o programa\n"
                            "Escolha uma opção: "
                            ))
    if opcao_curso == 1:
        adicionar_curso()
    elif opcao_curso == 2:
        pesquisar_curso()
    elif opcao_curso == 3:
        edit_curso()
    elif opcao_curso == 4:
        remove_curso()
    elif opcao_curso == 5:
        list_curso()
    elif opcao_curso == 6:
        break
    else:
        print("Opção inválida. Tente novamente")
     
    

