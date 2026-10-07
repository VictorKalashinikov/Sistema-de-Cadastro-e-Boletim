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
            print(f"{aluno['nome']} está {aluno['situacao']}")
            alunos.append(aluno)

        case 2:
            print('ALUNOS CADASTRADOS')
            for aluno in alunos:
                for chave, valor in aluno.items():
                    print(f'{chave}: {valor}')
        case 3:
            encontrado = False
            print('Consultar aluno')
            nome = input('Qual o nome do(a) aluno(a) buscado? ').strip()
            for aluno in alunos:
                if aluno['nome'] == nome:
                    print('Aluno(a) encontrado!')
                    print()
                    for chave, valor in aluno.items():
                        print(f'{chave}: {valor}')
                    encontrado = True
            if not encontrado:
                print('Aluno(a) não encontrado ou não cadastrado.')
        case 4:
            print('ESTATÍSTICAS')
            if not alunos:
                print('Nenhum aluno(a) foi cadastrado(a) ainda.')
            else:
                total = len(alunos)
                aprovados = reprovados = recuperacao = soma = 0
                maior_media = menor_media = alunos[0]['media']
                for aluno in alunos:
                    if aluno['situacao'] == 'Aprovado':
                        aprovados += 1
                    if aluno['situacao'] == 'Recuperação':
                        recuperacao += 1
                    if aluno['situacao'] == 'Reprovado':
                        reprovados += 1
                    if aluno['media'] > maior_media:
                        maior_media = aluno['media']
                    if aluno['media'] < menor_media:
                        menor_media = aluno['media']
                    soma += aluno['media']
                media_geral = soma / total
                print(f'Alunos cadastrados: {total}')
                print(f'Aprovados: {aprovados}')
                print(f'Recuperação: {recuperacao}')
                print(f'Reprovados: {reprovados}')
                print(f'Maior média: {maior_media:.2f}')
                print(f'Menor média: {menor_media:.2f}')
                print(f'Média geral: {media_geral:.2f}')



        case _:
            print('Opção inválida!')
            continue