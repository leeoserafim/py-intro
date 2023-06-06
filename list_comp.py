frutas=['maça','banana','abacaxi','kiwi','coco']
frutas_com_a=[]

for x in frutas:
    if 'a' in x:
        frutas_com_a.append(x)
print(frutas_com_a)

nova_lista_com_a= [x for x in frutas if 'a' in x]
print(nova_lista_com_a)