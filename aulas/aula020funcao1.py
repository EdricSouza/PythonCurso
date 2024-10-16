#Funções
aula = 'Aula 20'
print(f'{aula:=^50}')

def contador(*num):
    tamanho = len(num)
    for valor in num:
        print(valor, end=' ')
    print('Fim')
    print(f'São {tamanho} numeros')

contador(5,6,7,4,3)
contador(2,3,5,2)