numero = input('Digite um numero: ')

n = '0000' + numero

print(f'A unidade do numero digitado e {n[-1]}'.format(n))
# Usamos f'texto{n[-1]} para definir uma unidade, assim sucetivamente, para poder esta definino, unidade, dezena, centena...  

print(f'A dezena do numero digitado e {n[-2]}'.format(n))
print(f'A centena do numero digitado e {n[-3]}'.format(n))
print(f'A milha do numero digitado e {n[-4]}'.format(n))