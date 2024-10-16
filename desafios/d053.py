#palindromo
desafio = 'desafio 53'
print(f'{desafio:=^50}')

frase = str(input('Digite a frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
print(junto)

inverso = ''

for l in range (len(junto) - 1, -1, -1):
    inverso += junto[l]
print(junto, inverso)

if junto == inverso:
    print(f'\u001b[33mÉ palindromo')