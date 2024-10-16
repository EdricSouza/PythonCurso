from math import hypot as hipo

#Hipotenusa
desafio = 'desafio 17'
print(f'{desafio:=^50}')

catetoop = int(input('Digite o valor do cateto oposto: '))
catetoadj = int(input('Digite o valor do cateto adjacente: '))

hipotenusa = hipo(catetoop, catetoadj)

print(f'O valor da hipotenusa de {catetoop} e {catetoadj} é: {hipotenusa}')
