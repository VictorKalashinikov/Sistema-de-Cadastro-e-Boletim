from utilidades import leiaInt, leiaFloat
alunos = []

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
    escolha = leiaInt('Escolha uma opção: ')
    match escolha:
        case 0:
            break
        case 1:
            print('Cadastrar aluno')
            aluno = {}
            aluno['nome'] = input('Nome do aluno(a): ').strip()
            aluno['idade'] = leiaInt('Idade: ')
            aluno['nota1'] = leiaFloat('Primeira nota: ')
            aluno['nota2'] = leiaFloat('Segunda nota: ')
            aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
            if aluno['media'] >= 7:
                aluno['situacao'] = 'Aprovado'
            elif aluno['media'] >= 5:
                aluno['situacao'] = 'Recuperação'
            else:
                aluno['situacao'] = 'Reprovado'
            print(f'{aluno['nome']} está {aluno['situacao']}')
            alunos.append(aluno)

        case 2:
            print('ALUNOS CADASTRADOS')
            for id, aluno in enumerate(alunos):
                for chave, valor in aluno.items():
                    print(f'{chave}: {valor}')
        case 3:
            print('Consultar aluno')
            nome = input('Qual o nome do(a) aluno(a) buscado? ').strip()
            for aluno in alunos:
                if aluno['nome'] == nome:
                    print('Aluno(a) encontado!')
                    print()
                    for chave, valor in aluno.items():
                        print(f'{chave}: {valor}')
        case 4:
            print('ESTATÍSTICAS')
            aprovados = reprovados = recuperacao = media_turma = 0
            maior_media = menor_media = alunos[0]['media']
            for aluno in alunos:
                if aluno['situacao'] == 'Aprovado':
                    aprovados += 1
                if aluno['situacao'] == 'Recuperação':
                    recuperacao += 1
                if aluno['situacao'] == 'Reprovado':
                    reprovados += 1
                if aluno['media']


            print(f'Alunos cadastrados: {len(alunos)}')
            print(f'Aprovados: {aprovados}')
            print(f'Recuperação: {recuperacao}')
            print(f'Reprovados: {reprovados}')



        case _:
            print('Opção inválida!')
            continue