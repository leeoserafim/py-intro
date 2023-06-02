from os import system
system('cls')

def soma(x,y):
    print(f'soma de {valor1} + {valor2}:  {x+y}')
def subtracao(x,y):
    print(f'subtração de {valor1} - {valor2} : {x-y}')
def multiplicacao(x,y):
    print(f'multiplicação {valor1} * {valor2}: {x*y}')
def divisao(x,y):
    print(f'divisão {valor1} / {valor2}: {x/y}')

while True:
    valor1=float(input('Primeiro numero: '))
    valor2=float(input('Segundo numero: '))

    print('1.Somar\n 2.Subtrair\n3.Multiplicar\n4.Dividir')

    operador=int(input('Opção: '))

    if operador == 1:
        soma(valor1,valor2)
    if operador == 2:
        subtracao(valor1,valor2)
    if operador==3:
        multiplicacao(valor1,valor2)
    if operador==4:
        divisao(valor1,valor2)

    opcao= input('Deseja continuar? [N]ão:')
    if opcao.lower() == 'n':
        break