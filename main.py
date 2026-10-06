from utilidades import leiaInt

while True:
    print('''
    ========== SISTEMA ESCOLAR ==========
    [0] Sair
    [1] Cadastrar aluno
    [2] Listar alunos
    [3] Consultar aluno
    [4] Calcular estatísticas
    =====================================
    ''')
    escolha = leiaInt('Escolha uma opção:')
    match leiaInt:
        case 0:
            break
        case 1:
            print('Cadastrar aluno')
        case 2:
            print('Listar alunos')
        case 3:
            print('Consultar aluno')
        case 4:
            print('Calcular estatísticas')
        case _:
            print('Opção inválida!')
            continue