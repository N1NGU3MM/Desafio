nome = str(input('Qual é o seu primeiro nome? '))
sobrenome = str(input('Quando seu sobre nome? '))
s = nome + sobrenome

print('Seu nomere em CAPS é: {}'.format(nome.upper()))
print('Seu nome em letras minuscolas é: {}'.format(nome.lower()))
print('A quantidade de letras que tem seu nome é {} e seu sobre nome {}, a quantidade de letras total no seu nome é {}'
      .format(len(nome), len(sobrenome), len(s)))
print('Seu primeiro nome tem {} letras'.format(len(nome)))

print('Olá mundo') 