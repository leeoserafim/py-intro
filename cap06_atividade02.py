from os import system,name
system('cls')

def soma(x,y):
    try:
        print(f'Soma: {float(x)+float(y)}')
    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')
def subtracao(x,y):
    try:
        print(f'Soma: {float(x)-float(y)}')
    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')
def multiplicacao(x,y):
    try:
        print(f'Soma: {float(x)*float(y)}')
    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')
def divisao(x,y):
    try:
        print(f'Soma: {float(x)/float(y)}')
    except Exception as erro:
        print(f'Ocorreu um erro: {erro}')

while True:
    system ('cls') if name == 'nt' else system('clear')
    valor1=float(input('Primeiro numero: '))
    valor2=float(input('Segundo numero: '))

    print('1.Somar\n2.Subtrair\n3.Multiplicar\n4.Dividir')

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