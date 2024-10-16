from random import randint

#SS
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))

def aleatorio(list):
    for a in range (1, 6):
        list.append(randint(1, 10))
    print('Soteados 5 valores: ', end=' ')
    for num in list:
        print(f'{num}', end=' ')
    print()  

def somaPar(list):
    pars = 0
    for num in list:
        if num % 2 == 0:
            pars += num
    print(f'A soma dos valores pares de {list} é {pars}')

list = []

aleatorio(list)
somaPar(list)