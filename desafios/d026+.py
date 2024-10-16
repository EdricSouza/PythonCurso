#Ocorrencia
desafio = 'desafio 26'
print(f'{desafio:=^50}')

frase = input('Digite uma frase: ').lower()
frase = frase.strip()

print(frase)

print(f'A letra "a" aparece {frase.count('a')} vezes')
print(f'A primeira vez que aparece é na {frase.find('a')+1}° posição')
print(f'A última é na {frase.rfind('a')+1}° posição')