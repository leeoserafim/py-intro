arquivo='categorias.csv'
categorias=open(arquivo, 'r', encoding='utf-8')
dicCategoria={}
for line in categorias:
    colunas=line.strip().split(';')
    dados=[colunas[1], colunas[2]]
    dicCategoria[colunas[0]]=dados
categorias.close()

print(dicCategoria)
print('x')
print(dicCategoria['3'])
print('x')
print(dicCategoria['3'][1])

for x in dicCategoria:
    print(x)
    print(dicCategoria[x])

print('xxxxxxxxxxxxxxxxxxxxxxxx')

for v in dicCategoria.values():
    print(f'categoria :{v[0]: <15} | Produtos: {v[1]}')

print('xxxxxxxxxxxxxxxxxxxxxxxx')   

print(dicCategoria.keys())
print(dicCategoria.values())