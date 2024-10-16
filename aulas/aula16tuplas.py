#Tuplas
aula = 'Aula 16'
print(f'{aula:=^50}')

#alor = (parenteses não obrigatório)Tupla []Lista {}Dicionário
lanche = 'hamburguer', 'Suco', 'Pizza','Pudim', 'Batata Frita'
#print(lanche[1])
#print(lanche[-1])
#print(lanche[1:3])
#print(lanche[:2])
#print(lanche[::2])

#for elemento in lanche:
    #print(f'O lanche é {elemento}')

#for posicao, elemento in enumerate(lanche):
    #print(f'O lanche é {elemento}  na posição {posicao}')

#for posicao in range(0, len(lanche)):
    #print(f'O lanche é {lanche[posicao]} na posição {posicao}')

#print(sorted(lanche)) #forma ordenada

a = (2,4,5)
b = (5,8,7,2)

c = a + b

print(a)
print(b)
print(c) #junta as tuplas

print(c.count(5)) #conta quantas vezes o 5 aparece
print(c.index(2, 2)) #posição da primeira vez que valor aparece na tupla a partir do outro parametro

pessoa = ('Gustavo',39, 'M', 1.70)
print(pessoa)

for c in pessoa:
    print(c)

del(pessoa) #apaga a tupla