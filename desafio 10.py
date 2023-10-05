from math import hypot
co = float(input('Comprimento do catero oposto: '))
ca = float(input('Comprimento do cateto adjasente: '))
hi = (co**2 + ca**2) ** (1/2)

# Para somar o valor de cada cateto, elevamos cada lado do catero a 2 e depois buscamos a haiz do valor da soma dos
# dois catetos

hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Aqui esta sendo usado a segundao form de calcular o valor da umpotenusa, impotando o hypot de math  
print('A soma da hipotenusa e {:.2f}'.format(hip))