from os import system, name

opcao=''
lista_nome=[]
lista_celular=[]

while opcao.lower() != 'n':
    system ('cls') if name == 'nt' else system('clear')
    nome= input('informe um nome: ')
    celular= input('informe o celular: ')
    opcao= input('\n Deseja inserir outro nome? [N]ão, qualquer tecla para seguir')

    lista_nome.append(nome)
    lista_celular.append(celular)

lista_celular.pop() #remove o item
lista_nome.pop()    #remove o item
print()

system ('cls') if name == 'nt' else system('clear')
for i in range(len(lista_nome)):
    print(f'Nome: {lista_nome[i]: <20} - Celular: {lista_celular[i]}')


print()

lista_nome.remove('11')   #remove apenas o valor
lista_celular.remove('11')  #remove apenas o valor 

print()

for i in range(len(lista_nome)):
    print(f'nome: {lista_nome[i]: <20} - Celular: {lista_celular[i]}')

lista_celular.clear() #limpa a lista toda
lista_nome.clear()    #limpa a lista toda