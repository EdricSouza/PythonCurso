#Condições

aula = 'Aula 10'
print(f'{aula:=^50}')

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a primeira nota: '))

m = (n1+n2)/2

print(f'Sua media foi {m}')

if m >= 6:
    print('Aprovado')
else:
    print('reprovado')