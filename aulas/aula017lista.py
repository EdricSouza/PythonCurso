#Listas
aula = 'Aula 17'
print(f'{aula:=^50}')

lista = ['GOW', 'Spider-Man', 'Dead Cells', 'Snap', 'Jumanji']
lista[1] = 'Iron-Man'

print(lista)

lista.append('OP') #adiciona no final
lista.insert(2, 'MK1') #adiciona na posição descrita
lista.sort() #Ordem seja numerica ou alfabetica
lista.sort(reverse=True) #Ordem reversa
print(len(lista)) #tamanho da lista
lista.remove('GOW') #remove na posição descrita
lista.insert(3, 'MK1') #adiciona na posição descrita

if 'LOR' in lista: #se tiver na lista remove
    lista.remove('LOR')
else:
    print('não achei a palavra LOR')


print(lista)