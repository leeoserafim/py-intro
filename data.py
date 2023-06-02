from datetime import datetime
from os import system

system('cls')

print(datetime.now())

atual=datetime.now()

print(type(atual))

montar_data = datetime(2023, 1, 16)

print(f'Data montada: {montar_data}, tipo: {type(montar_data)}')

print(atual.strftime('%d/%m/%Y %H:%M'))

try:
    data_nascimento=input('informe sua data de nascimento: (dd/mm/aaaa)')
    data_nascimento=datetime.strptime(data_nascimento, '%d/%m/%Y')
    print(f'Data de nascimento:{data_nascimento} tipo: {type(data_nascimento)}')

except ValueError as e:
    print(f'Valor errado. Atente ao formado dd/mm/aaaa \n Erro : {e}')

def idade(nascimento):
    today=datetime.today()
    return today.year - nascimento.year - ((today.month,today.day) < \
                                           (nascimento.month, nascimento.day))
def idade2(nascimento):
    today = datetime.today()
    diferenca=today-nascimento
    return int(diferenca.days / 365.25)

print(f'Voce tem : {idade(data_nascimento)} anos')
print(f' -- Voce tem : {idade2(data_nascimento)} anos')

hoje=(4, 20)
niver=(4, 20)
print(f'tipo  HOJE: {type(hoje)}')
print(f'tipo NIVER: {type(niver)}')

resultado = hoje < niver

print(f'Resultado : {resultado}, tipo: {type(resultado)}')
print(f'Convertendo bool para int: {int(resultado)}')

def dias(nascimento):
    today=datetime.today()
    return(today-nascimento).days

print(f'Voce ja viveu {dias(data_nascimento)} dias')