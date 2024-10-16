# triangulo
desafio = 'desafio 35'
print(f'{desafio:=^50}')

s1 = int(input('Digite o valor do primeiro segmento: '))
s2 = int(input('Digite o valor do segundo segmento: '))
s3 = int(input('Digite o valor do terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')