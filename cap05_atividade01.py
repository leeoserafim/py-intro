from os import system, name

system ('cls') if name == 'nt' else system('clear')

numeros=('zero ', 'um', 'dois', 'três','quarto','cinco','seis','sete','oito','nove')
dez=('dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove')
dezenas=('','','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa')

pos=int(input('digite um numero entre 0 e 99: '))

extenso=''

if pos < 10:
    extenso=numeros[pos]
elif pos <20:
    extenso=dez[pos-10]
elif pos<=99:
    dezena=int(pos/10)
    numeral=pos%10
    numero=''
    if numeral != 0:
        numero=  'e', + numeros[numeral]
    extenso = dezenas[dezena] + numero
    
else:
    print('Numero invalido. Maior ou igual a 100')

print(extenso)
