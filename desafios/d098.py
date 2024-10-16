from time import sleep

#Contador
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))
msg('Contador')

def contador(inicio, fim, passo):
    print('=-'*20)
    if passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    elif passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo*-1} em {passo*-1}')
    if passo != 0:
        for num in range(inicio, fim, passo):
            print(num, end = ' ', flush=True)
            sleep(0.5)
        print(' ')
    else:
        print('Não é possível fazer essa contagem')

contador(1,10,1)
contador(10, 0, -2)

print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))

contador(inicio = i, fim = f, passo = p)