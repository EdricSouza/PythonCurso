#SS
def msg(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))

msg('Notas')

def notas(*num, sit = False):
    nota = {}
    nota['maior'] = max(num)
    nota['min'] = min(num)
    nota['total'] = len(num)
    nota['media'] = sum(num)/len(num)
    if sit == True:
        if nota['media'] > 7:
            nota['sit'] = 'Boa'
        elif 6 >= nota['media'] < 7:
            nota['sit'] = 'Razoável'
        else:
            nota['sit'] = 'Ruim'

    return nota

resp = notas(5.5, 9.6, 10, 6.5, sit = True)
print(resp)