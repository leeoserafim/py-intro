print(' Calculador de IMC'.center(50,"*"))
peso = input('Informe seu peso em KG:')
altura = input('Informe sua altura em cm:')
auxx = altura.replace('.','')
aux = peso.replace('.','')

if not aux.isdigit():
    print('Precisa ser valor numérico')
    exit()
if not auxx.isdigit(): 
    print('Precisa ser valor numérico')
    exit()

peso = float(peso)
altura = float(altura)

altura_metro= float(altura/100)

print(f' O seu IMC é de {peso / (altura_metro*altura_metro):.2f}') 
      

imc= peso / (altura_metro*altura_metro)

if imc < 18.5:
   print('A baixo do peso ideal')
elif imc >= 18.5 and imc<=24.9:
    print('Peso ideal')
elif imc >= 25 and imc<=29.99:
    print('Sobrepeso')
elif imc>=30 and imc<=34.9:
    print('Obesidade Grau I')
elif imc>=35 and imc<=39.9:
    print('Obesidade Grau II')
elif imc>= 40:
    print('Obesidade Grau III ou Mórbida')
