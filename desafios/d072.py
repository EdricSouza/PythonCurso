#Extensos
desafio = 'Desafio 72'
print(f'{desafio:=^50}')

extensos = ('zero', 'um', 'dois', 'três','quatro', 'cinco'
            , 'seis', 'sete', 'oito','nove','dez'
            , 'onze', 'doze', 'treze', 'quatorze','quinze'
            , 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número e 0 a 20: '))
    if numero > 0 or numero < 20:
        break
    print('Número não consta entre 0 e 20')

print(f'Você digitou o número: {extensos[numero]}')