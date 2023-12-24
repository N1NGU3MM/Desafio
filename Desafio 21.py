def km():
    km = int(input('Quantos Km terá a viagem? '))
    distancia = (km * 0.40)
    distancia2 = (km * 0.45) 
    if km == 199:
        print(f'O valor da sua viagem de {km}Km, custará R${distancia}')
    else:
        print(f'O valor da sua viagem de {km}Km, custará R${distancia2}')    
km()