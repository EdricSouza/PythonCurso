#Maior e Menor
desafio = 'Desafio 78'
print(f'{desafio:=^50}')

numeros = []
maior = 0
menor = 0
pmaior = []
pmenor = []

for cont in range (1,6):
    numeros.append(int(input('Digite um número: ')))
    if cont == 1:
        maior = menor = numeros[cont-1]
    else:
        if numeros[cont-1] > maior:
            maior = numeros[cont-1]
        elif numeros[cont-1] < maior:
            maior = numeros[cont-1]
    cont =+1

for posic in range(len(numeros)):
    if numeros[posic] == maior:
        pmaior.append(posic+1)

for posic in range(len(numeros)):
    if numeros[posic] == menor:
        pmenor.append(posic+1)

print(f'O maior número é {maior} nas posições: {pmaior}')
print(f'O menor número é {menor} nas posições: {pmenor}')