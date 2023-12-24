numero = input('Digite um numero: ')
n = '000' + numero

print('Seu numero é {}'.format(numero))
print(f'Seu numero tem {n[-1]} unidade')
print(f'Sua dezena é {n[-2]}')
print(f'Sua centena é {n[-3]}')
print(f'Sua milha é {n[-4]}')
