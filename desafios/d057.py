#F ou M
desafio = 'desafio 57'
print(f'{desafio:=^50}')

s = str(input('Digite qual é o seu gênero: \n\u001b[34mM - masculino\n\u001b[35mF - Feminino\n')).capitalize().strip()
print('-------------------------------')
if s[0] != 'M' and s[0] != 'F':
    while s[0] != 'F' and s[0] != 'M':
        print('Valor inexistente')
        print('\u001b[34mM - masculino')
        print('\u001b[35mF - Feminino')
        s = str(input('Digite qual é o seu gênero: ')).capitalize().strip()
        print('-------------------------------')
elif s[0] == 'M':
    print('Você é do sexo masculino')
elif s[0] == 'F':
    print('Você é do sexo feminino')