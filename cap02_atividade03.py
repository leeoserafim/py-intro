from os import system


nome_completo = input('Informe seu nome completo: ')
#print('1. Quantidade de caracteres:', len(nome_completo))
print(f'1. Quantidade de caracteres: {len(nome_completo)} ')
#print('2. Nome em maiusculo:', nome_completo.upper())
print(f'2. Nome em maiusculo: {nome_completo.upper()}')
#print('3. Nome em minusculo:', nome_completo.lower())
print(f'3. Nome em minusculo: {nome_completo.lower()}')
#print('4. Primeira letra em maiusculo:', nome_completo.capitalize())
print(f'4. Primeira letra em maiusculo: {nome_completo.capitalize()}')

espaco=nome_completo.find(' ')
#print('5. Somente o primeiro nome:', nome_completo[0:espaco])
print(f'5. Somente o primeiro nome:{nome_completo[0:espaco]}')
#print('6. Nome sem espacos:', nome_completo.replace(' ', ''))
print(f'6. Nome sem espaços: {nome_completo.replace(" ","")}')
#print('7. Tem somente letras?', nome_completo.replace(' ', '').isalpha())
print(f'7. Tem somente letra?{nome_completo.replace(" ","").isalpha()}')
#print('8. É alphanumerico? tem letras ou numeros?:', nome_completo.replace(' ','').isalnum())
print(f'8. É alphanumerico? tem letra ou numero?: {nome_completo.replace(" ","").isalnum()}')
#print('9. Quebrar o texto a cada espaço em branco:', nome_completo.split(" "))
print(f'9. Quebrar o texto a cada espaço em branco:{nome_completo.split(" ")}')
#print('10. Centralizar o nome entre*')
print(f'10. Centralizar o nome entre *: \n {nome_completo.center(80,"*")}')
#print(nome_completo.center(80,"*"))