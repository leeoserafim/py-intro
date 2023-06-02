from os import system,name

system('cls') if (name == 'nt') else system('clear')

from cap08_atividade03classe import tabCat
from cap08_atividade03classe import tabProd

cat=tabCat()
prod=tabProd()
dicCategoria=cat.dicCat()
listaProduto=prod.listProd()
caminho=''
arquivo=caminho+'relatorio.txt'
relatorio=open(arquivo, mode='w' , encoding='utf-8')
for cat in dicCategoria:
    titulo = '{}\n{}\n\nProdutos\n'.format(dicCategoria[cat][0].upper(),dicCategoria[cat][1])
    prod=[]
    for p in listaProduto:
        if str(p[2]) == cat:
            valor='{:.2f}'.format(p[8])
            produto='{:<60} | R$ {:>8}'.format(str(p[1].capitalize()+' ' + p[3][0:60]),valor)
            prod.append(produto)
    prod.sort()
    lista=''
    i=1
    for p in prod:
        lista+='{:>4}. {}\n'.format(i,p)
        i+=1
    divisor='Categoria'.center(80,'*')
    relatorio.write(divisor+'\n' + titulo + lista + '\n\n')
categorias='Total de Categorias: {:>4}'.format(len(dicCategoria))
produtos='Total de Produtos: {:>4}'.format(len(listaProduto))
resumo='Resumo '.center(80,'*')
final='{}\n\n{:>80}\n{:>80}'.format(resumo,categorias,produtos)
relatorio.write(final)
relatorio.close()
