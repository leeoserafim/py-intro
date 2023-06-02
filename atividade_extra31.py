from os import system, name

system ('cls') if name == 'nt' else system('clear')


conta=''
while conta != '5':
    valor_a = input('Digite um valor:')
    valor_b = input('Digite outro valor:')
    teste_a= valor_a.replace('.','')
    teste_b= valor_b.replace('.','')

    if not teste_a.isdigit():
        print('precisa ser um valor numerico')
        exit()
    if not teste_b.isdigit():
        print('precisa ser um valor numerico:')
        exit()
    valor_a = float(valor_a)
    valor_b = float(valor_b)

    conta = input('Selecione uma das operações que deseja:\n 1 -> + \n 2 -> - \n 3 -> x \n 4 -> / \n Precione 5 para sair do menu.\n Opção: ')
    if conta == '1':
        print(f'{valor_a:.2f} + {valor_b:.2f} = {valor_a + valor_b:.2f}')
        
    if conta == '2':
        print (f'{valor_a:.2f} - {valor_b:.2f} = {valor_a - valor_b:.2f}')
        
    if conta == '3':
        print (f'{valor_a:.2f} x {valor_b:.2f} = {valor_a*valor_b:.2f}')
        
    if conta == '4':
        print (f'{valor_a:.2f} / {valor_b:.2f} = {valor_a / valor_b:.2f}')
    
    conta = input('Precione 5 para sair ou qualquer tecla para continuar\n')
    system('cls')


        