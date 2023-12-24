def salario():
    salario = float(input('Qual é o valor do salario do funcionario? '))
    salario1  = (((salario * 10) / 100) + 1250.00)
    salario2 = (((salario * 15) / 100) + 1250.00) 
    if salario == 1250:
        print(f'O salario do funcionario é de R${salario1} ') 
    else:
        print(f'O salario do funcionario R${salario2}')
salario()