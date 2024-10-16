#Listas
aula = 'Aula 18'
print(f'{aula:=^50}')

Pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maira', 45]]
print(Pessoas[2][0])

for p in Pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')