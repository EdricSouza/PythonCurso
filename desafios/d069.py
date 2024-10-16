#cad
desafio = 'Desafio 69'
print(f'{desafio:=^50}')

maior = 0
homem = 0
mulher = 0

while True:
    idade = int(input('Digite a idade: '))
    s = str(input('Qual o seu sexo: ')).capitalize().strip()

    if idade > 18:
        maior += 1
    if s[0] == 'M':
        homem += 1
    if s[0] == 'F' and idade < 20:
        mulher += 1
    
    c = input('Deseja continuar? ').capitalize().strip()
    if c[0] == 'N':
        break
    print('_________________________________')

print(f'Há {maior} pessoas maior de idades cadastradas')
print(f'{homem} homens foram cadastrados')
print(f'Das mulheres cadastradas apenas {mulher} possuem menos que 20 anos')