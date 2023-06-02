from os import system

system('cls')

print('Vamos calcular raiz quadrada'.center(50,"*"))
raiz_quadrada = input('Digite um numero:')
print(f'O numero é um valor inteiro?: {raiz_quadrada.isnumeric()}')
print(f'O valor é um numero com  casas decimais?: {raiz_quadrada.isdecimal()}')
raiz = int(raiz_quadrada) ** (1/2)
print(f'A raiz quadrada de', raiz_quadrada,'é:', raiz )