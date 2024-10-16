#Funções
aula = 'Aula 20'
print(f'{aula:=^50}')

def soma(a, b):
    print(f'a = {a} e b = {b}')
    s = a + b
    print(f'A soma é = {s}')

soma(a = 4, b = 5)
soma(b = 2, a = 3)
soma(14, 15)
# soma(4) vai dar erro pois deve ter a mesma quantidade de parametros