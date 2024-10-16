#pintar parede
desafio = 'desafio 11'
print(f'{desafio:=^50}')

altura = float(input('Digite o valor da altura: '))
largura = float(input('Digite o valor da largura: '))

area = largura * altura

tinta = area/2

print(f'Dados os valores {altura} e {largura} em metros, será necessário {tinta}L de tinta para pintar a parede com uma área de {area}m²!')