from cap07_atividade01classe import Recibo
nome_cliente= input('Nome:')
valor_compra= float(input('Digite o valor da compra:'))
criar_recibo= Recibo (nome_cliente) 
criar_recibo.valor= valor_compra
criar_recibo.descricao('desenvolvimento de sistemas em Python')
print(criar_recibo._descricao)

print()
print(criar_recibo)

