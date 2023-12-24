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