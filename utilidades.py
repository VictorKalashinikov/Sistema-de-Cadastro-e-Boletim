def leiaInt(msg):
    try:
        num = int(input(msg))
    except:
        print('Por favor digite um número inteiro válido.')
    else:
        return num
    