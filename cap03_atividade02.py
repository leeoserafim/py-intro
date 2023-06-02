from os import system

system ('cls')

print('Conversor de medida'.center(50,"*"))

medida = input('Informe a medida em centimetros: \n ')

aux = medida.replace('.','')

if aux.isdigit():
    medida = float(medida)

    print('\n Escolha a unidade desejada: \n 1-Polegada \n 2-Pé \n 3-Jarda')
    
    menu = input('Opção:')
    
    if menu == '1':
        resultado =  medida / 2.54
        op = "polegadas"
    elif menu == "2":
        resultado = medida / 30.48
        op = "pés"
    elif menu=="3":
        resultado = medida / 91.44
        op = "jardas"   
    else:
        print('Opção invalida')

    if menu == '1' or menu=='2' or menu == '3':
        print(f'Resultado: o valor {medida} em centimetros é igual a {resultado:.2f} em {op}')

else:
    print('Valor informado não é numerico')

