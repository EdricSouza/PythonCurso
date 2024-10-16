#triangulo
desafio = 'desafio 42'
print(f'{desafio:=^50}')

s1 = int(input('Digite o valor do 1° segmento: '))
s2 = int(input('Digite o valor do 2° segmento: '))
s3 = int(input('Digite o valor do 3° segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s3:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')