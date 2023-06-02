from os import system, name

system ('cls') if name == 'nt' else system('clear')

#print('Tabuada'.center(50,'*'))

#linhas=int(input('informe um numero de linha:')) + 1
#colunas=int(input('informe um numero de coluna:')) + 1
#for i in range(1,11):
    #print(f'{i}*{multiplicador} = {i*multiplicador}')


#for i in range(1,multiplicador):
    #print(f'{i: >4}'\
          #f'{i*2: >4}'\
          #f'{i*3: >4}'\
          #f'{i*4: >4}'\
          #f'{i*5: >4}'\
          #f'{i*6: >4}'\
          #f'{i*7: >4}'\
          #f'{i*8: >4}'\
          #f'{i*9: >4}'\
          #f'{i*10: >4}'\
            #)

#print("*"*80)

#for i in range(1,linhas):
#    linha= f'{i: >4}'
#    for j in range(2,colunas):
#        linha+= f'{i*j: >4}'

#    print(linha)


#i=1
#while(i <=linhas):
    
 #   print(i)
  #  i+=1

print(' O numero é PRIMO '.center(80,"*"))

numero= input("informe um numero inteiro:")
if numero.isdigit():
    i=2
    numero=int(numero)
    divisor=0
    tipo='O numero dever ser maior que 2'
    while i<numero:
        tipo='O numero é primo'
        x=numero % i
        if x == 0:
            divisor=i
            tipo='O numero não é primo'
            break
        i += 1
    print (tipo)
    print(f'O menor divisor é: {divisor}' if divisor >0 else '')
else:
    print('O valor informado nao é um numero inteiro')        
