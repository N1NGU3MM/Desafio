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

def carro():
    print('Escolha um direção que o carro deverar seguir')
    carro = input('O carro deverar ir pela esquerda ou pela direita? ')
    carro = carro.lower()
    carro = carro.title()
    if carro == 'Esquerda':
        print('O carro esta seguindo o caminho da esquerda')
    else:
        print('O carro esta seguindo o caminho da direita')
carro()

def computador():
    print('O computador irá escolher um número de 0 a 5, tente adivinhar qual é esse número')
    print('Olá, acabei de pensar em um número! ')
    numero = random.randint(0, 5)
    dn = int(input('Diga um numero de 0 a 5: '))
    
    if dn == numero:
        print('Você acertou!!')
    else:
        print('Você errou!!')
    print(f'O numero erá: {numero}')
computador()

def velocida():
    velocida = int(input('Diga a velocida que o carro está: '))
    multa = ((velocida - 60) * 7)
    
    if velocida <= 60:
        print('O carro nao foi multado')
    else:
        print(f'O veiculo ultapassou a veiculo permitida, e recebeu uma multa de: R${multa}')
velocida()

def numero():
    numero = int(input('Digite um numero:'))
    
    if numero % 2 == 0:
        print(f'O numero {numero} é par')
    else:
        print(f'O numero {numero} é impar')
numero()

def km():
    km = int(input('Quantos Km terá a viagem? '))
    distancia = (km * 0.40)
    distancia2 = (km * 0.45) 
    if km == 199:
        print(f'O valor da sua viagem de {km}Km, custará R${distancia}')
    else:
        print(f'O valor da sua viagem de {km}Km, custará R${distancia2}')    
km()

def ano():
    ano = int(input('Digite um ano? '))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('É ano bissexto')      
    else:
        print('Não é ano bissexto')
ano()

def n_m ():
    numeros = []
    for i in range(3):
        numero = int(input(f'Digite um numeros: {i+1}º'))
        numeros.append(numero)

    numeros.sort()
    maior = numeros[-1]
    menor = numeros[0]
    print(f'O maior numero é {maior},e o menor é {menor} ')   
n_m()

def salario():
    salario = float(input('Qual é o valor do salario do funcionario? '))
    salario1  = (((salario * 10) / 100) + 1250.00)
    salario2 = (((salario * 15) / 100) + 1250.00) 
    if salario == 1250:
        print(f'O salario do funcionario é de R${salario1} ') 
    else:
        print(f'O salario do funcionario R${salario2}')
salario()

