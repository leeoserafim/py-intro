from random import randint


def imprime_abertura():
    print("*"*28)
    print('jogo da forca'.center(28,'-'))
    print('*'*28)    

def carrega_palavra_secreta():
    arquivo=open('frutas.txt', 'r')
    palavras=[]
    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)
    arquivo.close()
    sorteio=randint(0,(len(palavras)))
    palavra_secreta=palavras[sorteio].upper()
    return palavra_secreta

def init_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def verifica_letra_repetida(letras_certas,letra):
    return letra in letras_certas


def gg():
    

    imprime_abertura
    palavra_secreta=carrega_palavra_secreta()
    letras_acertadas=init_letras_acertadas(palavra_secreta)
    letras_tentativas=[]


    morreu=False
    acertou=False
    erros=0
    #enquanto nao morreu e nao acertoua
    #quanto nao false
    #enquanto (True)

    while(not morreu and not acertou):
        tentativa =input('qual a letra?').strip().upper()
        

        if verifica_letra_repetida(letras_acertadas,tentativa):
            print(f'A letra {tentativa} ja foi utilizada')
            continue


        letras_tentativas.append(tentativa)
        index=0
        if tentativa in palavra_secreta:
            for letra in palavra_secreta:
                if (tentativa == letra):
                    letras_acertadas[index]=letra
                index+=1
            print(letras_acertadas)
        else:
            print("letra errada")
            erros+=1
            morreu= erros==7

        acertou = '_'not in letras_acertadas

    if acertou:
        print('venceu')

    else:
        print('perdeu')


                                                                                                                                                                                
    print('gg forca')
    print('\nObrigado por acertar!\n')

if __name__ == '__main__':
    gg()

