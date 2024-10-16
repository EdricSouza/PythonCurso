#Vogais
desafio = 'Desafio 77'
print(f'{desafio:=^50}')

palavras = ('pastel', 'sabonete', 'panela', 'piada', 'pernambuco', 'cachorro', 'tabuada', 'paraguai', 'esquecido')

for p  in palavras:
    print(f'\nA palvra {p.upper()} tem: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')