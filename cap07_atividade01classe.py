from num2words import num2words
class Recibo:
    def __init__(self,nome):
        self.nome=nome

    def descricao(self,value):
        self._descricao=value

    @property
    def valor(self):
        return (self._valor)
    
    @valor.setter
    def valor(self, value):
        self._valor=value

    def  extenso(self):
        valor_extenso= num2words(self._valor, lang='ar', to='currency'), num2words(self._valor, lang='ko', to='currency'),num2words(self._valor, lang='hu', to='currency'),num2words(self._valor, lang='pt_BR', to='currency')
        return valor_extenso
    
    def __str__(self):
        texto=f'Recebemos de {self.nome} a quantia de R${self._valor:.2f} ({self.extenso()})'
        descricao= '\nReferente {}'.format(self._descricao if (self._descricao!='')else '')
        dados ='{}\n{}{}'.format('RECIBO'.center(len(texto),'*'),texto,descricao)
        return dados
