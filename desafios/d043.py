#Peso
desafio = 'desafio 43'
print(f'{desafio:=^50}')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura**2

if imc < 18.5:
    print('Abaixo do peso normal')
elif imc > 18.6 and imc <24.9:
    print('Peso ideal')
elif imc > 25 and imc <29.9:
    print('levemente acima do peso')
elif imc > 30 and imc < 34.9:
    print('Obesidade grau 1')
elif imc > 35 and imc < 39.9:
    print('Obesidade grau 2 (morbida)')
elif imc > 40:
    print('Obesidade 3 (morbida)')