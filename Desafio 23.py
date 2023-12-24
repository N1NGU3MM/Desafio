def n_m ():
    numeros = []
    for i in range(3):
        numero = int(input(f'Digite um numeros: {i+1}º'))
        numeros.append(numero)

    numeros.sort()
    maior = numeros[-1]
    menor = numeros[0]
    print(f'O maior numero é {maior},e o menor é {menor} ')   
n_m()
