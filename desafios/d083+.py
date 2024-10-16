#xpre
desafio = 'Desafio 83'
print(f'{desafio:=^50}')

expr = str(input('Digite a expressão: '))

pilha = []
for simb in expr:
    if simb in '(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('sua expressão é valida')
else:
    print('Está errada')