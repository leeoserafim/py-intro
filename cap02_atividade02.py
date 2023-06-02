print ('vamos calcular a area do retangulo:')
base = (input ('informe o valor da base: '))
altura = (input ('informe o valor da altura: '))

print(f'base é numerico: {base.isnumeric()}')
print(f'altura é decimal: {altura.isdecimal()}')

base = int(base)
altura = int(altura)

print(f'tipo da base: {type(base)}')
print(f'tipo da altura:{type(altura)}')

print(f'a area do triangulo é : { base * altura }')