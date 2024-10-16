# base conversor
desafio = 'desafio 37'
print(f'{desafio:=^50}')

numero = int(input('Digite o valor: '))
option = int(input('Qual é a opção de conversão: \n1 - binario \n2 - octal \n3 - hexadecimal '))

if option == 1:
    print(f'O numero {numero} em binário é {numero, bin(numero)[2:]}')
elif option == 2:
    print(f'O numero {numero} em octal é {numero, oct(numero)[2:]}')
elif option == 3:
    print(f'O numero {numero} em hexadecimal é {numero, hex(numero)[2:]}')
else:
    print('Opção não existe')