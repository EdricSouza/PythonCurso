#Analise
desafio = 'desafio 56'
print(f'{desafio:=^50}')

maior = 0
maiorp = 0
media = 0
mulhermenor = 0

for p in range (1,5):
    print(f'-----------{p}ª Pessoa-----------')
    nome = input(f'Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').upper()

    media += idade

    if sexo[0] == 'M': #ou if sexo[0] == 'M' and maior < idade:
        if maior < idade:
            maior = idade
            maiorp = nome
    elif sexo[0] == 'F': #elif sexo[0] == 'F' and idade < 20:
        if idade < 20:
            mulhermenor += 1

print('\u001b[32mA média das idades é de: ', media / 4, 'anos')
print(f'\u001b[36m CyanO homem mais velho é {maiorp} com {maior} anos')
if mulhermenor == 1:
    print(f'\u001b[35mMagentaTem {mulhermenor} mulher menor de idade')
else:
    print(f'\u001b[35mMagentaTem {mulhermenor} mulheres menor de idade')
