import random

def inico():
    nome = input('Qual é o seu nome? ')
    nome = nome.lower()
    nome = nome.title()
    if nome == 'Alessandro':
        print('Que nome bonito!')
    else:
        print('Que nome FEIO!')
inico()