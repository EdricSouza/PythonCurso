#cadastro
desafio = 'Desafio 84'
print(f'{desafio:=^50}')

cad = []
pessoa = []
mai = men = 0

while True:
    pessoa.append(input('Digite o nome: '))
    pessoa.append(int(input('Digite a idade: ')))

    if len(cad) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[0]
        elif pessoa[1] < men:
            men = pessoa[0]

    cad.append(pessoa[:])

    brk = input('Deseja cadastrar outra pessoa: [N/S]').capitalize().strip()
    if brk[0] == 'N':
        break
    else:
        pessoa.clear()
    

print(f'{len(cad)} pessoas foram cadastradas')
print(f'A pessoa mais velha da lista é {mai}')
print(f'A pessoa mais nova da lista é {men}')

print(cad)