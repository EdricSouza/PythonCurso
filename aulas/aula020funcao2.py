#Funções
aula = 'Aula 20'
print(f'{aula:=^50}')

def dobro(list):
    pos = 0
    while pos<len(list):
        list[pos] *= 2
        pos += 1
    print(valores)

def soma(list):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores temos {s}')

valores = [7,6,4,5,3]

print(valores)
dobro(valores)
soma(valores)