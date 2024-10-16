#Controle de Terrenos
desafio = 'Desafio 96'
print(f'{desafio:=^50}')

def msg(msg):
    print(f' {msg}')
    print('-'*22)
    
msg('Controle de Terrenos')

def area(l, c):
    area = l * c
    print(f'A área de um terreno com {l} de largura e {c} de altura é: {area}m²')

largura = float(input('Digite o valor da largura[m]: '))
comprimento = float(input('Digite o valor do comprimento[m]: '))

area(largura, comprimento)