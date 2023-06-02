from os import system, name
import random


opcao= 's'
pc=0
player=0
while opcao.upper() == 'S':
    system ('cls') if name == 'nt' else system('clear')
    computador = random.randint(0,2) 
    jogador = (input('''Escolha uma opção:
    [0]pedra
    [1]papel
    [2]tesoura
    Digite a sua escolha. \n'''))

    teste=jogador.replace('.','')
    if '.' in jogador or not teste.isdigit():
        opcao=input('Jogar novamente? Aperte S(sim) para jogar novamente.')
        continue

    jogador = int(jogador[0])

    if jogador >=0 and jogador <= 2:
        pecas=('pedra','papel','tesoura')
        print(f'Voce escolheu: {pecas[jogador]}')
        print(f'O computador escolheu: {pecas[computador]}')

        tabelas = ((0,1,-1),(-1,0,1),(1,-1,0))
        
        jogada = tabelas[computador][jogador]
        if jogada == 0:
            resultado = 'Deu empate, voces escolheram a mesma peça'
        elif jogada == 1:
            resultado='Voce ganhou!'
            player = player+1
        else:
            resultado='O computador ganhou'
            pc = pc+1
        placar = print(f'Computador: ({pc})  x Jogador= ({player})')   
        print (resultado)
        opcao=input('Jogar novamente? Aperte S(sim) para jogar novamente.')
    else:
        print('Valor escolhido é invalido!')  
        opcao=input('Jogar novamente? Aperte S(sim) para jogar novamente.')
else:
    opcao=input('Jogar novamente? Aperte S(sim) para jogar novamente.')  
