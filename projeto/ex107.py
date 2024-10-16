from tools import metade, dobro, aumentar

num = int(input('Digite um valor: '))

met = metade.metade(num)
dob = dobro.dobro(num)
aument = aumentar.aumentar(num)

print(f'O dobro de {num} é {dob}')
print(f'{num} aumentado em 10% é {aument}')
print(f'A metade de {num} é {met}')