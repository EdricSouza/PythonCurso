#Listas
aula = 'Aula 17'
print(f'{aula:=^50}')

#formas de criar listas
valores = []
lista = list()

valores.append(5)
valores.append(4)
valores.append(1)
print('_________________')

for cont in range (0,5):
    lista.append(input('Digite um número: '))
print('_________________')

print('Temos os valores: ', end='')
for valor in valores:
    print(f'{valor}', end=' ')

print('\n')
print('_________________')

for posic, valor in enumerate(valores):
    print(f'Na posição {posic} tem o valor {valor}')
print('fim')

print(lista)
print('_________________')

#ligação entre listas
a = [2,3,4,7]
b = a
b[2] = 8

print(a)
print(b)

print('_________________')
#cópia entre listas
a = [2,3,4,7]
b = a[:]
b[2] = 8

print(a)
print(b)