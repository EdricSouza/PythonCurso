#comparacao
desafio = 'desafio 55'
print(f'{desafio:=^50}')

maior = 0
menor = 0

for i in range (1,6):
    peso = float(input(f'Digite o  peso da {i}ª pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
        pessoama = i
        pessoame = i
    else:
        if peso > maior:
            maior = peso
            pessoama = i
        if peso < menor:
            menor = peso
            pessoame = i
print(f'\u001b[31mO maior peso é {maior} da {pessoama}ª pessoa')
print(f'\u001b[32mO menor peso é {menor} da {pessoame}ª pessoa')
