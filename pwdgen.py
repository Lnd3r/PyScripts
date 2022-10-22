from pyperclip import copy
from sys import argv
import random

### O objetivo deste script é gerar uma senha de tamanho especificado pelo usuário, ###
###            seja usando este como um script primário ou secundário.              ###


# Function para separar caracteres de uma string e adicionar para uma list.
def vtls(var):
    list = []
    for item in var:
        list.append(item)
    return list

# Function para somar items de duas lists para uma nova list.
def apls(ls1, ls2):
    list = []
    for item in ls1:
        list.append(item)
    for item in ls2:
        list.append(item)
    return list

# Letras comuns e acentuadas.
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
cap_alfabeto = alfabeto.upper()
acento = 'ãâäáàẽêëéèĩîïíìõôöóòũûüúùñç'
cap_acento = acento.upper()

# Alfabeto e acentos separados.
new_alfabeto = apls(alfabeto, cap_alfabeto)
new_acento = apls(acento, cap_acento)

# Números e símbolos.
numeros = '1234567890'
simbolos = '!@#$£§%&*+-_<>='

# Base padrão para geração de senhas.
base = apls(apls(vtls(new_alfabeto), vtls(new_acento)), apls(vtls(numeros), vtls(simbolos)))

# Function para uso principal do script.
def genpwd(len):
    senha = ''.join(random.sample(base, int(len)))
    copy(senha)
    print(f'Senha de {len} caracteres criada:\n{senha}\nNova senha copiada.')
    return senha

# if name = main para uso de script individualmente.
if __name__ == '__main__':
    genpwd(argv[1])

#____NEVER GONNA GIVE YOU UP! NEVER GONNA LET YOU DOWN!____#