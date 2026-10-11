from utilidades import leiaInt, leiaFloat
alunos = []

def mostrar_aluno(indice, aluno):
    print(f'ID {indice} ',end='')
    for chave, valor in aluno.items():
        print(f'{chave}: {valor}')


def procura_aluno(alunos):
    encontrado = False
    nome = input('Qual o nome do(a) aluno(a) buscado? ').strip()
    for indice, aluno in enumerate(alunos):
        if aluno['nome'] == nome:
            print('Aluno(a) encontrado!')
            print()
            encontrado = True
            return True, indice, aluno
    if not encontrado:
        print('Aluno(a) não encontrado ou não cadastrado.')
        return False, 0, '0'

def nao_encontrado():
    print('ERRO! Aluno(a) não encontrado!')

def escolher():
    escolha = leiaInt('Escolha uma opção: ')
    return escolha


def mostrar_invalido():
    print('Opção inválida!')

def atualiza_media_situacao(aluno):
    aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
    if aluno['media'] >= 7:
        aluno['situacao'] = 'Aprovado'
    elif aluno['media'] >= 5:
        aluno['situacao'] = 'Recuperação'
    else:
        aluno['situacao'] = 'Reprovado'
    return aluno



while True:
    print('''
    ========== SISTEMA ESCOLAR ==========
    [0] Sair
    [1] Cadastrar aluno
    [2] Listar alunos
    [3] Consultar aluno
    [4] Calcular estatísticas
    [5] Editar aluno
    =====================================
    ''')
    escolha = escolher()
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
            aluno = atualiza_media_situacao(aluno)
            print(f"{aluno['nome']} está {aluno['situacao']}")
            alunos.append(aluno)

        case 2:
            print('ALUNOS CADASTRADOS')
            for aluno in alunos:
                for chave, valor in aluno.items():
                    print(f'{chave}: {valor}')
        case 3:
            print('Consultar aluno')
            encontrou, indice, aluno = procura_aluno(alunos)
            if encontrou:
                mostrar_aluno(indice, aluno)
            else:
                nao_encontrado()
            
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

        case 5:
            encontrou, indice, aluno = procura_aluno(alunos)
            if encontrou:
                print('''
    [1] Alterar a idade
    [2] Alterar notas
    [3] Alterar todos os dados
                ''')
                escolha2 = escolher()
                match escolha2:
                    case 1:
                        aluno['idade'] = leiaInt('Nova idade: ')
                        alunos[indice] = aluno
                    case 2:
                        aluno['nota1'] = leiaFloat('Nova nota 1: ')
                        aluno['nota2'] = leiaFloat('Nova nota 2: ')
                        aluno = atualiza_media_situacao(aluno)
                        print(f"{aluno['nome']} está {aluno['situacao']}")

                    case 3:
                        aluno['idade'] = leiaInt('Nova idade: ')
                        aluno['nota1'] = leiaFloat('Nova nota 1: ')
                        aluno['nota2'] = leiaFloat('Nova nota 2: ')
                        atualiza_media_situacao(aluno)
                        print(f"{aluno['nome']} está {aluno['situacao']}")
                    case _:
                        print('Opção inválida!')
            else:
                mostrar_invalido()
        case _:
            mostrar_invalido()
            continue