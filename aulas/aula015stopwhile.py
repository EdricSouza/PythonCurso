#interrupção de repetições while
aula = 'Aula 15'
print(f'{aula:=^50}')

cont = 1

while True:
    print(cont, ' -> ', end='')
    cont += 1
    if cont == 112:
        break
print('Fim')