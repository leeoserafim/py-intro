from tkinter import *

janela_principal= Tk()

class janela():
    def __init__(self):
        self.janela_principal= janela_principal
        self.janela()
        self.frames()
        self.botao()
        janela_principal.mainloop()
    def janela(self):
        self.janela_principal.title('Calculadora de Lajes')
        self.janela_principal.configure(background='#000080')
        self.janela_principal.geometry('1200x800')
        self.janela_principal.resizable(True,True)
        self.janela_principal.maxsize(width=1920, height=1080)
        self.janela_principal.minsize(width=500,height=500)
    def frames(self):
        self.frame_titulo = Frame(self.janela_principal, bg='yellow', highlightbackground='white',highlightthickness=3)  
        self.frame_titulo.place(relx=0.02,rely=0.022, relwidth=0.97, relheight=0.045)
        self.frame_titulo.configure(background='yellow')
        
        self.frame_cliente= Frame(self.janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
        self.frame_cliente.place(relx=0.02,rely=0.1, relwidth=0.97, relheight=0.1)
        self.frame_cliente.configure(background='white')

        self.frame_vigas = Frame(self.janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
        self.frame_vigas.place(relx=0.02,rely=0.22, relwidth=0.3, relheight=0.6)
        self.frame_vigas.configure(background='white')

        self.frame_lista = Frame(self.janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
        self.frame_lista.place(relx=0.33,rely=0.22, relwidth=0.4, relheight=0.6)
        self.frame_lista.configure(background='white')

        self.frame_resultado = Frame(self.janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
        self.frame_resultado.place(relx=0.74,rely=0.22, relwidth=0.25, relheight=0.6)
        self.frame_resultado.configure(background='white')
        
        self.frame_botao= Frame(self.janela_principal, bg='#FFD700', highlightbackground='#FFD700',highlightthickness=3)  
        self.frame_botao.place(relx=0.33,rely=0.83, relwidth=0.66, relheight=0.1)
        self.frame_botao.configure(background='white')

    def botao(self):
        self.bt_apaga_u=Button(self.frame_botao, text='Apagar', relief=RAISED)
        self.bt_apaga_u.place(relx=0.015,rely=0.2,relwidth=0.1, relheight=0.6)

        self.bt_apaga_s=Button(self.frame_botao, text='Apagar viga selecionada ->', relief=RAISED)
        self.bt_apaga_s.place(relx=0.12,rely=0.2,relwidth=0.2, relheight=0.6)

        self.bt_limpar=Button(self.frame_botao, text='vazio')
        self.bt_limpar.place(relx=0.33,rely=0.2,relwidth=0.05, relheight=0.6)

        self.bt_calc=Button(self.frame_botao, text='Calcular', relief=RAISED)
        self.bt_calc.place(relx=0.41,rely=0.2,relwidth=0.25, relheight=0.6)

        self.bt_save=Button(self.frame_botao, text='Salvar (Criar arquivo .txt)', relief=RAISED)
        self.bt_save.place(relx=0.7,rely=0.2,relwidth=0.25, relheight=0.6)
        
        self.bt_adicionar=Button(self.frame_vigas, text='Adicionar viga', relief=RAISED)
        self.bt_adicionar.place(relx=0.3,rely=0.89,relwidth=0.4, relheight=0.1)
 

        self.titulo=Label(self.frame_titulo, text='CALCULADORA DE MATERIAS PARA LAJE PREMOLDADA',font=('Helvetica',18))
        self.titulo.pack(side=TOP)
        self.titulo.configure(background='yellow')


        #  MEDIDAS E QUANTIDADES DE VIGAS MAIS REFORÇOS
        self.vigas=Label(self.frame_vigas, text="Largura do comodo em METROS\n (calcula a quantidade de vigas)")
        self.vigas.place(relx=0.03,rely=0.047)
        self.vigas.configure(background='white')

        self.vigas_entry=Entry(self.frame_vigas)
        self.vigas_entry.place(relx=0.6,rely=0.06,relwidth=0.3,relheight=0.05)
        self.vigas_entry.configure(background='lightgray')

        self.dash=Label(self.frame_vigas, text="----------------------------------------------------------------")
        self.dash.place(relx=0.03,rely=0.15)
        self.dash.configure(background='white')

        self.tamanho=Label(self.frame_vigas, text='Tamanho das vigas em METROS')
        self.tamanho.place(relx=0.03, rely=0.2)
        self.tamanho.configure(background='white')
        
        self.tamanho_entry=Entry(self.frame_vigas)
        self.tamanho_entry.place(relx=0.6,rely=0.2,relwidth=0.3,relheight=0.05)
        self.tamanho_entry.configure(background='lightgray')

        self.dash2=Label(self.frame_vigas, text="----------------------------------------------------------------")
        self.dash2.place(relx=0.03,rely=0.25)
        self.dash2.configure(background='white')

        self.lista_reforco=Label(self.frame_vigas, text='Selecione a quantidade de barras de reforço adicional:')
        self.lista_reforco.place(relx=0.03,rely=0.3)
        self.lista_reforco.configure(background='white')

        self.cinco_mm=Label(self.frame_vigas, text='5mm ------------->',bg='white')
        self.cinco_mm.place(relx=0.1,rely=0.37)

        self.cinco_mm_entry=Entry(self.frame_vigas, bg='lightgray')
        self.cinco_mm_entry.place(relx=0.4,rely=0.37,relwidth=0.3,relheight=0.05)

        self.seis_mm=Label(self.frame_vigas, text='1/4 -- 6mm ------>',bg='white')
        self.seis_mm.place(relx=0.1, rely=0.44)

        self.seis_mm_entry=Entry(self.frame_vigas, bg='lightgray')
        self.seis_mm_entry.place(relx=0.4,rely=0.44,relwidth=0.3,relheight=0.05)

        self.oito_mm=Label(self.frame_vigas, text='5/16 -- 8mm ----->',bg='white')
        self.oito_mm.place(relx=0.1,rely=0.51)

        self.oito_mm_entry=Entry(self.frame_vigas, bg='lightgray')
        self.oito_mm_entry.place(relx=0.4, rely=0.51, relwidth=0.3,relheight=0.05)

        self.dez_mm=Label(self.frame_vigas, text='3/8 -- 10mm ----->',bg='white')
        self.dez_mm.place(relx=0.1,rely=0.58)

        self.dez_mm_entry=Entry(self.frame_vigas, bg='lightgray')
        self.dez_mm_entry.place(relx=0.4, rely=0.58, relwidth=0.3,relheight=0.05)

        self.doze_mm=Label(self.frame_vigas, text='1/2 -- 12,5mm --->',bg='white')
        self.doze_mm.place(relx=0.1,rely=0.65)

        self.doze_mm_entry=Entry(self.frame_vigas, bg='lightgray')
        self.doze_mm_entry.place(relx=0.4, rely=0.65, relwidth=0.3,relheight=0.05)

        self.dezesseis_mm=Label(self.frame_vigas, text='5/8 -- 16mm ----->',bg='white')
        self.dezesseis_mm.place(relx=0.1,rely=0.72)

        self.dezesseis_mm_entry=Entry(self.frame_vigas, bg='lightgray')
        self.dezesseis_mm_entry.place(relx=0.4, rely=0.72, relwidth=0.3,relheight=0.05)

        # DADOS DO CLIENTE
        self.nome=Label(self.frame_cliente, text='Nome:', bg='white')
        self.nome.place(relx=0.12,rely=0.1)

        self.nome_entry=Entry(self.frame_cliente, bg='lightgray')
        self.nome_entry.place(relx=0.16,rely=0.11,relwidth=0.2)

        self.cpf=Label(self.frame_cliente, text='CPF:', bg='white')
        self.cpf.place(relx=0.37,rely=0.1)

        self.cpf_entry=Entry(self.frame_cliente, bg='lightgray')
        self.cpf_entry.place(relx=0.4,rely=0.11,relwidth=0.2)

        self.telefone=Label(self.frame_cliente, text='Contato:', bg='white')
        self.telefone.place(relx=0.6,rely=0.1)

        self.telefone_entry=Entry(self.frame_cliente, bg='lightgray')
        self.telefone_entry.place(relx=0.65,rely=0.11,relwidth=0.2)

        self.endereco=Label(self.frame_cliente, text='Endereço:', bg='white')
        self.endereco.place(relx=0.05,rely=0.6)

        self.endereco_entry=Entry(self.frame_cliente, bg='lightgray')
        self.endereco_entry.place(relx=0.1,rely=0.6,relwidth=0.8)

janela()

