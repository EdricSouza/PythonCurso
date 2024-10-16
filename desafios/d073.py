#Times
desafio = 'Desafio 73'
print(f'{desafio:=^50}')

times = ("Flamengo","Santos","Palmeiras","Gremio",

             "Atletico Paranaense", "São Paulo","Internacional",

             "Conrithians","Fortaleza","Goias","Bahia","Vasco",

             "Atletico Mineiro","Fluminense","Botafogo","Ceará",

             "Cruzeiro","CSA","Chapecoense","Avaí")

print(f'Os 5 primeiros times são: {times[:6]}')
print(f'Os últimos quatro colocados são: {times[-4:]}')
print(f'Em ordem alfabético a ordem fica: {sorted(times)}')
print(f'O Bahia está na {times.index('Bahia') + 1}ª posição')