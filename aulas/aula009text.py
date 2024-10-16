#Manipulação de texto

aula = 'Aula 09'
print(f'{aula:=^50}')

frase = "Estudando Python Até o Final"

print(frase[0])
print(frase[3:])
print(frase[:12])
print(frase[:20:2])
print(frase[3:12:2])


print(len(frase))
print(frase.count('o',2,15))
print(frase.find('s'))

print('Python' in frase)

print(frase.capitalize())
print(frase.title())

dividido = frase.split()
print(dividido[4][3])

juncao = "".join(dividido[0]), "".join(dividido[4])
print(juncao)

print(frase.upper())

""""
05:10 - Fatiamento de String;
13:50 - Análise:
    14:15 - len();
    14:50 - count();
    16:35 - find();
    18:55 - in;
19:35 - Transformação:
    19:55 - replace();
    20:50 - upper();
    21:50 - lower();
    22:25 - capitalize();
    23:04 - title();
    24:34 - strip();
    25:08 - rtrip();
    25:50 - lstrip();
26:35 - Divisão:
    26:50 - split();
28:20 - Junção:
    28:35 - join();
"""