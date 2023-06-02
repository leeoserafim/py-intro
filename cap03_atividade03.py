from os import system, name

system ('cls') if name == 'nt' else system('clear') # if ternario

print('Folha de pagamento'.center(50,"$"))

salario = input('\n Informe o salario:')

aux = salario.replace('.','')

if not aux.isdigit():
    print('O salario deve ser um valor numérico')
    exit()

salario = float(salario)
if salario>7507.49:
    inss_desconto=877.22
else:
    if salario >= 3856.95:
        inss_alicota=0.14
    elif salario >= 2571.3:
        inss_alicota=0.12
    elif salario >= 1302.01:
        inss_alicota=0.09
    else:
        inss_alicota=0.075
    inss_desconto= salario*inss_alicota

base= salario-inss_desconto


if base > 4664.48:
    ir_alicota = 0.275
    deducao=869.36
elif base>= 3751.06:
    ir_alicota=0.225
    deducao=636.13
elif base>= 2826.66:
    ir_alicota=0.15
    deducao=354.8
elif base>= 1903.99:
    ir_alicota=0.075
    deducao=142.8
else:
    ir_alicota=0
    deducao=0

ir = base *ir_alicota - deducao
salario_liquido= base - ir

print(f'Salario bruto = {salario:.2f}\n'\
     f'Salario base = {base:.2f}\n' \
     f'INSS : {inss_desconto:.2f} \n' \
     f'% IR: {ir_alicota*100:.2f} \n' \
     f'Valor do IR: {ir:.2f} \n' \
     f'Salario liquido: {salario_liquido:.2f}')
