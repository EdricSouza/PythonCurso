#calculadora
desafio = 'desafio 59'
print(f'{desafio:=^50}')

frase = 'Calculadora virtual'
print(f'{frase:=^50}')

oper = 0
valor = 0
n1 = float(input('Digite o valor do primeiro número: '))
n2 = float(input('Digite o valor do segundo número: '))

while oper != 5:
    print('1 - Soma')
    print('2 - Multiplicação')
    print('3 - Maior')
    print('4 - Novos números')
    print('5 - Sair do programa')
    oper = int(input('Qual operação deseja fazer: '))
    
    if oper == 1:
        valor = n1 + n2
        print(f'A soma é igual a {valor}')
    elif oper == 2:
        valor = n1 * n2
        print(f'A multiplicação é igual a {valor}')
    elif oper == 3:
        if n1 > n2:
            print(f'{n1} é maior')
        else:
            print(f'{n2} é maior')
    elif oper == 4:
        n1 = float(input('Digite o novo valor do primeiro número: '))
        n2 = float(input('Digite o novo valor do segundo número: '))
    else:
        print('Função não existente')
    print('________________________________________________')