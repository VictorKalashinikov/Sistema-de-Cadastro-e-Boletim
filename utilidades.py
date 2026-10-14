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


    