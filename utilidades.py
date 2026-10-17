# utilidades

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print('Por favor digite um número inteiro válido.')
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            print('Por favor digite um número real válido.')
        else:
            return num

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

def leiaNota(msg):
    while True:
        nota = leiaFloat(msg)
        if 0 <= nota <= 10:
            break
        print('Por favor insira uma nota entre 0 e 10.')
    return nota
    