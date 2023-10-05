import math
# Usamos ímport para baixar toda a geleria. Podemos usar "From" para baixar apenas um codigo da galeira.
# Assim dicando "from'+galeria+import+nome do que deiseja importa" assim baixando uma função especifica.
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de um numero {} é a raiz de {:.2f}'.format(num, math.ceil(raiz))) 
#podeos usar a galeria baixada e usar uma função especifica usanod o comando "galeria{Nome da galeria}+ . e função"
# Exemplo: math.ciel(raiz)

n = float(input("Diga um numero: "))
it = math.trunc(n)
print('A parte intereia {} do numero e {:.2f}'.format(math.trunc(it), n ))