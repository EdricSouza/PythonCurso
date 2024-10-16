#SS
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))

msg('Verificação de número')

def leiaInt(msg):
    while True:
        num = input(f'{msg}: ')
        if num.isnumeric():  
            return num
        else:    
            print('\u001b[31m Não é número \u001b[0m')

numero = leiaInt('Digite um número')
print(f'Você acabou de digitar o número {numero}')