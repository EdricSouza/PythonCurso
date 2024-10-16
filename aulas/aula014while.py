from time import sleep
#Estrutura de Repetição while
aula = 'Aula 14'
print(f'{aula:=^50}')

c = 0

while c != 10:
    c += 1
    print(c)
print('Fim')

v = int(input('Digite qual será o tempo: '))

for i in range(v,0,-1):
    print(i)
    sleep(1)

d = 0
numero = 0
while d != 1:
    soma = int(input('Digite o valor: '))
    numero += soma
    d = int(input('Deseja somar mais? 1 - sim 2 - não\n'))

print(numero)