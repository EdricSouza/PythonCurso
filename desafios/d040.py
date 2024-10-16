#Media
desafio = 'desafio 40'
print(f'{desafio:=^50}')

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('Reprovado')
elif 6.9 < media > 5:
    print('Recuperação')
elif media >= 7:
    print('Aprovado')