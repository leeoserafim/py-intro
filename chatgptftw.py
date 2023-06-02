import tkinter as tk
#import pyperclip

vigas = []

def adicionar_viga():
    largura = float(largura_entry.get())
    comprimento_viga = float(comprimento_entry.get())
    quantidade_vigas = int(largura / 0.43) + 1
    metro_linear = quantidade_vigas * comprimento_viga
    
    # Novo código para obter as quantidades de reforço
    um_quarto_valor = um_quarto_entry.get()
    cinco_dezesseis_valor = cinco_dezesseis_entry.get()
    tres_oito_valor = tres_oito_entry.get()
    meio_valor = meio_entry.get()
    
    # Concatenar as quantidades de reforço em uma string
    reforco = ""
    if um_quarto_valor:
        reforco = f"{um_quarto_valor}br de 1/4 "
    if cinco_dezesseis_valor:
        reforco = f"{cinco_dezesseis_valor} br de 5/16 "
    if tres_oito_valor:
        reforco = f"{tres_oito_valor} br de 3/8 "
    if meio_valor:
        reforco = f"{meio_valor} br de 1/2 "
    
    if reforco:
        vigas.append((quantidade_vigas, comprimento_viga, reforco.strip()))
        lista_vigas.insert(tk.END, f"{quantidade_vigas} VG {comprimento_viga} - {reforco.strip()}")
    else:
        vigas.append((quantidade_vigas, comprimento_viga))
        lista_vigas.insert(tk.END, f"{quantidade_vigas} VG {comprimento_viga}")

def apagar_viga():
    if len(vigas) > 0:
        # Remove a última viga da lista
        viga_removida = vigas.pop()
        # Remove a última viga da lista tkinter
        lista_vigas.delete(tk.END)
        # Exibe uma mensagem com a viga removida
        resultado_label.config(text=f"Viga removida: {viga_removida}")
    else:
        resultado_label.config(text="Não há vigas para remover.")


def calcular():
  
    # zera as variáveis de reforço
    um_quarto_total = 0
    cinco_dezesseis_total = 0
    tres_oito_total = 0
    meio_total = 0
    # calcula o metro linear total
    metro_linear_total = sum([v[0]*v[1] for v in vigas])
    metro_quadrado = metro_linear_total * 0.43
    malhas = round(metro_quadrado/5)
    for viga in vigas:
        comprimento_linear = viga[0] * viga[1]
        if len(viga) > 2:
            # verifica o tipo de reforço da viga
            if "br de 1/4" in viga[2]:
                um_quarto_total += viga[0] * viga[1]
            if "br de 5/16" in viga[2]:
                cinco_dezesseis_total += viga[0] * viga[1]
            if "br de 3/8" in viga[2]:
                tres_oito_total += viga[0] * viga[1]
            if "br de 1/2" in viga[2]:
                meio_total += viga[0] * viga[1]
    # atualiza a label de resultado
    resultado_label.config(text=f"Metro linear TOTAL: {metro_linear_total:.2f}m\nMetro quadrado: {metro_quadrado:.2f} M² \nRef 1/4: {um_quarto_total:.2f}m\nRef 5/16: {cinco_dezesseis_total:.2f}m\nRef 3/8: {tres_oito_total:.2f}m\nRef 1/2: {meio_total:.2f}m")

def copiar_vigas():
    # Criar uma string com as informações das vigas
    viga_str = ""
    for viga in vigas:
        viga_str += f"{viga[0]} VG {viga[1]}"
        if len(viga) == 3:
            viga_str += f" - {viga[2]}"
        viga_str += "\n"

    # Copiar a string para a área de transferência
    #pyperclip.copy(viga_str)

def salvar():
    # zera as variáveis de reforço
    um_quarto_total = 0
    cinco_dezesseis_total = 0
    tres_oito_total = 0
    meio_total = 0
    # calcula o metro linear total
    metro_linear_total = sum([v[0]*v[1] for v in vigas])
    metro_quadrado = metro_linear_total * 0.43
    malhas = round(metro_quadrado/5)
    for viga in vigas:
        if len(viga) > 2:
            # verifica o tipo de reforço da viga
            if "1br de 1/4" in viga[2]:
                um_quarto_total += viga[0] * viga[1]
            if "1br de 5/16" in viga[2]:
                cinco_dezesseis_total += viga[0] * viga[1]
            if "1br de 3/8" in viga[2]:
                tres_oito_total += viga[0] * viga[1]
            if "1br de 1/2" in viga[2]:
                meio_total += viga[0] * viga[1]
    # atualiza a label de resultado
    resultado_label.config(text=f"Metro linear TOTAL: {metro_linear_total:.2f}m\nMetro quadrado: {metro_quadrado:.2f} M² \nRef 1/4: {um_quarto_total:.2f}m\nRef 5/16: {cinco_dezesseis_total:.2f}m\nRef 3/8: {tres_oito_total:.2f}m\nRef 1/2: {meio_total:.2f}m")

    # Cria um arquivo de texto com as informações das vigas e do cliente
    with open(f"{cliente_entry.get()}.txt", "w") as f:
        f.write(f"Cliente: {cliente_entry.get()}\n\n")
        for viga in vigas:
            if len(viga) == 3:
                f.write(f"{viga[0]} VG {viga[1]} - {viga[2]}\n")
            else:
                f.write(f"{viga[0]} VG {viga[1]}\n")
        f.write(f"Metro linear TOTAL: {metro_linear_total:.2f}m\nMetro quadrado: {metro_quadrado:.2f} M² \nRef 1/4: {um_quarto_total:.2f}m\nRef 5/16: {cinco_dezesseis_total:.2f}m\nRef 3/8: {tres_oito_total:.2f}m\nRef 1/2: {meio_total:.2f}m")

# Cria a janela principal

janela = tk.Tk()
janela.title("Cálculo de Vigas")
janela.geometry("800x600")

#Frame para os campos de entrada
entrada_frame = tk.Frame(janela)
entrada_frame.pack(padx=20, pady=20)

#Campos de entrada
cliente_label = tk.Label(entrada_frame, text="Nome do Cliente:", font=("Helvetica", 12))
cliente_label.grid(row=0, column=0, sticky="w")

cliente_entry = tk.Entry(entrada_frame, font=("Helvetica", 12), width=30)
cliente_entry.grid(row=0, column=1, padx=5)

largura_label = tk.Label(entrada_frame, text="Largura:")
largura_label.grid(row=1, column=0)

largura_entry = tk.Entry(entrada_frame)
largura_entry.grid(row=1, column=1)

comprimento_label = tk.Label(entrada_frame, text="Comprimento da Viga:")
comprimento_label.grid(row=2, column=0)

comprimento_entry = tk.Entry(entrada_frame)
comprimento_entry.grid(row=2, column=1)

um_quarto_label = tk.Label(entrada_frame, text="1/4")
um_quarto_label.grid(row=3, column=0)

um_quarto_entry = tk.Entry(entrada_frame)
um_quarto_entry.grid(row=3, column=1)

cinco_dezesseis_label = tk.Label(entrada_frame, text="5/16")
cinco_dezesseis_label.grid(row=4, column=0)

cinco_dezesseis_entry = tk.Entry(entrada_frame)
cinco_dezesseis_entry.grid(row=4, column=1)

tres_oito_label = tk.Label(entrada_frame, text="3/8")
tres_oito_label.grid(row=5, column=0)

tres_oito_entry = tk.Entry(entrada_frame)
tres_oito_entry.grid(row=5, column=1)

meio_label = tk.Label(entrada_frame, text="1/2")
meio_label.grid(row=6, column=0)

meio_entry = tk.Entry(entrada_frame)
meio_entry.grid(row=6, column=1)

#Botão para adicionar viga
adicionar_viga_button = tk.Button(janela, text="Adicionar Viga", command=adicionar_viga)
adicionar_viga_button.pack(pady=10)

#Frame para a lista de vigas
lista_frame = tk.Frame(janela)
lista_frame.pack()

#Lista de vigas
lista_vigas = tk.Listbox(lista_frame, width=50)
lista_vigas.pack(side=tk.LEFT, fill=tk.BOTH)

#Scrollbar para a lista de vigas
scrollbar = tk.Scrollbar(lista_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Conectar a scrollbar com a lista de vigas
lista_vigas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_vigas.yview)

#Botão para apagar viga
apagar_viga_button = tk.Button(janela, text="Apagar Viga", command=apagar_viga)
apagar_viga_button.pack(pady=10)

#Botão para calcular
calcular_button = tk.Button(janela, text="Calcular", command=calcular)
calcular_button.pack(pady=10)

#Label para o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

#Botão para copiar vigas
copiar_vigas_button = tk.Button(janela, text="Copiar Vigas", command=copiar_vigas)
copiar_vigas_button.pack(pady=10)

#Botão para salvar
salvar_button = tk.Button(janela, text="Salvar", command=salvar)
salvar_button.pack(pady=10)

janela.mainloop()