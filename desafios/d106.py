#SS
def msg(msg):
    print('\u001b[43m')
    print('~'*(len(msg)+2))
    print(f' {msg} ')
    print('~'*(len(msg)+2))
    print('\u001b[0m')

msg('Sistema de ajuda HELP')

def helps():
    while True:
        h = input('Função ou Bibliotéca > ')
        if h == 'fim':
            print('\u001b[41m')
            print('~'*(len(h)+25))
            print('          Até logo')
            print('~'*(len(h)+25))
            print('\u001b[0m')
            break
        print('\u001b[46m')
        print('~'*(len(h)+25))
        print(f' Acessando manual de: {h} ')
        print('~'*(len(h)+25))
        print('\u001b[0m')

        print('\u001b[47m')
        help(h)
        print('\u001b[0m')
        
        def msg(msg):
            print('\u001b[43m')
            print('~'*(len(msg)+2))
            print(f' {msg} ')
            print('~'*(len(msg)+2))
            print('\u001b[0m')

        msg('Sistema de ajuda HELP')
helps()