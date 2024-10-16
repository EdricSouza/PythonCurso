#SS
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))

msg('Fatoração')

def fatorial(num = 1, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser fatorado
    :param show: (opcional) Mostrar ou não a conta
    :return: o valor do fatorial de um número n
    """
    n = 1
    for c in range (num, 0, -1):
        n *= c
    if show == True:
        for c in range (num, 0, -1):
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c}', end='')
        print(' =', end=' ')
    return n

res = fatorial(num = 5, show = True)
print(res)
help(fatorial)