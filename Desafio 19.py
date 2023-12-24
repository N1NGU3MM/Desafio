def velocida():
    velocida = int(input('Diga a velocida que o carro está: '))
    multa = ((velocida - 60) * 7)
    
    if velocida <= 60:
        print('O carro nao foi multado')
    else:
        print(f'O veiculo ultapassou a veiculo permitida, e recebeu uma multa de: R${multa}')
velocida()
