#Transformador de texto
desafio = 'desafio 22'
print(f'{desafio:=^50}')

texto = input('Digite a frase: ')

print(texto.upper())
print(texto.lower())

print(len("".join(texto.split())))

print(len(texto.strip().split()[0]))

texto = "".join(texto.split())
print(len(texto))

