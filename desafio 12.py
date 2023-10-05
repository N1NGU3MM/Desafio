frase = '   Test de video   '

len(frase)
frase.count('e')

# Usado para contar quantas lestras similates tem dentro de uma frase
print(frase.count('e'))

# Usado para contar quantas caracteres tem dentro de uma frase
print(len(frase))

# Pode ser usado para encontrar uma determinada frase dentro de um texto ou frase
print(frase.find('vi'))

# Usado para verificar sem exite uma determinada palavra ou fase dentro de um texto ou frase
print('de' in frase)

# usado para mudar uma frase ou palavra dentro de um texto ou frase
print(frase.replace('video', 'Android'))

# Usado para colocar todas as letras em CAPS dentro de um texto ou frase
print(frase.upper())

# Usado para deixar todas as caracteres de uma frase ou texto em minuscolo
print(frase.lower())

# Usado para deixar apenas a primeira letra em CAPS
print(frase.capitalize())

# Usado para deixar todas as primeiras letra de uma palavra em CAPS
print(frase.title())

# Remove os espaço em brando do inico e fim da frase
print(frase.strip())

# Remove os espaço final das frases
print(frase.rstrip())

# Remove apenas os espaços iniciais das frase
print(frase.lstrip())

# Divide uma string em uma lista, fasendo que cada palavra leve um determinado numero
print(frase.split())

# Usado para separar caracteres no local de uma frase ou texto, deixando toda a frase S E P A R D A
print(''.join(frase))

# Podemos usar três " para print de um texto grande, sem precisar utilizar sempre varios print
print('''We're going to learn operations with strings in Python in 
this class. The main operations that we're going to see are 
Slicing, len() analysis, count(), find(), transformation using 
replace(), upper(), lower(), capitalize(), title(), strip(), merging with join().''')

# Podemos usar varios comando juntos 'capiralizer, lower...) e
# usaur find para encontra a posiçao de uma pelavra no texto
print(frase.capitalize().find('video'))
