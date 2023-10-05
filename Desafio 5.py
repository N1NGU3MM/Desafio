s = input('Digite uma numero:')
# Só usamos "int" para valores inteiros.
print(type(s))

print('É Alfanumerico?', s.isalnum())
print('É alfabetico?', s.isalpha())
print('É numerico?', s.isnumeric())
