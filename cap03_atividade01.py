from os import system

numero = int(input('Informe um numero: \n'))

div= numero % 2

if div == 0:
    print(f'O numero {numero} é par  pq o resto da divisão por 2 é igual a {div}'.center(50,"-"))
else :
    print(f'O numero {numero} é impar pq o resto da divisão por 2 é igual a {div}'.center(50,"-"))