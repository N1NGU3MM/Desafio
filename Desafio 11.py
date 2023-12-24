from math import sin, cos, tan, radians
angulo = float(input('Digite uma ângulo que deseja: '))
seno = sin((radians(angulo)))
cosseno = cos((radians(angulo)))
tangente = tan((radians(angulo)))
print('O angulo de {} tem so SENO de {:.2f}, o COSSENO de {:.2f}, e a TANGENTE de {:.2f}'.format(angulo, seno, cosseno, tangente))