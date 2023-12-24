def computador():
    print('O computador irá escolher um número de 0 a 5, tente adivinhar qual é esse número')
    print('Olá, acabei de pensar em um número! ')
    numero = random.randint(0, 5)
    dn = int(input('Diga um numero de 0 a 5: '))
    
    if dn == numero:
        print('Você acertou!!')
    else:
        print('Você errou!!')
    print(f'O numero era: {numero}')
computador()