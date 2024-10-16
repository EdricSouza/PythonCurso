# () ** * / // % + - ordem de precedência

aula = 'Aula 07'
print(f'{aula:=^50}')

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite o segundo numero: '))

soma = numero1 + numero2
subtração = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisaoint = numero1 // numero2
potencia = numero1 ** numero2
raiz = numero1**(1/numero2)
resto = numero1 % numero2


print('\nOperações\n')
print(f'A soma é {numero1+numero2}', end=' >>> ')
print(f'A subtração é {subtração}')
print(f'A multiplicação é {multiplicacao}', end=' >>> ')
print(f'A divisão é {divisao}')
print(f'A divisão inteira é {divisaoint}')
print(f'A potência é {potencia}', end=' >>> ')
print(f'A raiz é {raiz}')
print(f'O resto é {resto}')