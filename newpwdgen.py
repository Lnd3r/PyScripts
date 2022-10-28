from pyperclip import copy
from sys import argv
from random import sample as sp
import string

# Function que passa objetos indexáveis para uma nova list.
def tols(*args):
    lista = []                 # cria list vazia.
    for ls in args:            # for loop para cada list recebida como argumento.
        for item in ls:        # for loop para cada item da list do loop anterior.
            lista.append(item) # adiciona item à nova list.
    return lista # retorna a nova list

# Funciton que passa objetos de uma lista para uma string.
def tostr(charls= list):
    text = ''                # cria string vazia.
    text = text.join(charls) # junta items da list recibida no argumento.
    return text              # retorna nova string.

# Function que multiplica os caracteres disponíveis na base.
def extend(arg):
    count = 0               # armazena contagem do while loop.
    extbase = base_dict     # define base para "multiplicação" da base usada.
    while count < int(arg): # while loop enquanto contagem menor que argumento recebido.
        extbase = tostr(tols(extbase, base_dict)) # soma base à ela mesma.
        count += 1          # adiciona "1" à contagem.
    extbase = tostr(sp(extbase, len(extbase))) # Embaralha base à ser usada.
    return extbase          # retorna nova base extendida.

# Function que pega a senha aleatória com comprimento definido pelo usuário.
def pickrandom(base, len):
    pswrd = ''.join(sp(base, int(len))) # colhe senha da base com comprimento definido por argumento.
    copy(pswrd)             # copia senha para clipboard.
    return pswrd            # retorna senha.

# Function que retorna senha gerada via CLI.
def cli(): # só executa o print abaixo.
    print(f'Sua senha é: {senha}\nBase extendida {argv[2]} vezes, comprimento máx. de até {len(usedbase)} caracteres.')
    if input('Mostrar base?(s/N): ') in ('s','S'): # if para opção do usuário.
        print(f'Base usada:\n{usedbase}') # "printa" base usada.
    return None

# Funtion para uso em outro script.
def genpass(pslen, dlen):
    usedbase = extend(dlen) # armazena base usada.
    senha = pickrandom(usedbase, pslen) # gera senha.
    return usedbase, senha  # retorna base usada e senha.

# Variáveis usadas na execução do código.
simbolos = '£§!@#$%&*=-+_?' # Define caracteres especiais, evitando bugs ao colhê-los do mód. string.
base_dict = (tols(string.ascii_letters, string.digits, simbolos)) # Colhe caracteres e junta-os em uma list.

# If main 
if __name__ == '__main__':
    usedbase = extend(argv[2]) # chama função que extende e embaralha base usada.
    senha = pickrandom(usedbase, argv[1]) # chama function que gera senha.
    cli() # chama function que mostra info no console.
