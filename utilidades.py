def leiaInt(msg):
    try:
        num = int(input(msg))
    except:
        print('Por favor digite um número inteiro válido.')
    else:
        return num

def leiaFloat(msg):
    try:
        num = float(input(msg))
    except:
        print('Por favor digite um número real válido.')
    else:
        return num