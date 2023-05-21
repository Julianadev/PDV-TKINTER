import tkinter as tk
from tkinter import ttk
from datetime import datetime
import tkinter.filedialog

carrinho = []

def adicionar_item():
    item = item_entry.get()
    preco = float(preco_entry.get().replace(',', '.'))
    quantidade = float(quantidade_entry.get().replace(',', '.'))
    carrinho.append((item, preco, quantidade))
    atualizar_lista_itens()
    calcular_total()

def atualizar_lista_itens():
    lista_itens.delete(0, tk.END)
    for i, (item, preco, quantidade) in enumerate(carrinho, start=1):
        lista_itens.insert(tk.END, f'{i} - {item} - Preço: R$ {preco:.2f} - Quantidade: {quantidade}')

def calcular_total():
    total = sum(preco * quantidade for _, preco, quantidade in carrinho)
    total_label.config(text=f'Total: R$ {total:.2f}')

def gerar_nota_fiscal():
    nota_fiscal = f'=== Nota Fiscal ===\nData: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n\n'
    for i, (item, preco, quantidade) in enumerate(carrinho, start=1):
        nota_fiscal += f'{i} - {item} - Preço: R$ {preco:.2f} - Quantidade: {quantidade}\n'
    nota_fiscal += f'\nTotal: R$ {sum(preco * quantidade for _, preco, quantidade in carrinho):.2f}'

    # Criando a janela para exibir o cupom fiscal
    cupom_janela = tk.Toplevel(root)
    cupom_janela.title('Cupom Fiscal')

    cupom_texto = tk.Text(cupom_janela, height=20, width=40, font=('Arial', 12))
    cupom_texto.pack()
    cupom_texto.insert(tk.END, nota_fiscal)

    # Botões para salvar ou imprimir o cupom fiscal
    salvar_button = ttk.Button(cupom_janela, text='Salvar', command=salvar_cupom)
    salvar_button.pack(side=tk.LEFT, padx=10, pady=10)


def salvar_cupom(cupom_texto=None):
    arquivo = tk.filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Arquivo de texto', '*.txt')])

    if arquivo:
        nota_fiscal = cupom_texto.get('1.0', tk.END)
        arquivo.write(nota_fiscal)
        arquivo.close()


root = tk.Tk()
root.title('PDV Supermercado')

# Estilo para os campos de entrada
style = ttk.Style()
style.configure('TEntry', font=('Arial', 16), padding=10)

# Título
titulo_label = ttk.Label(root, text='PDV Supermercado', font=('Arial', 20, 'bold'))
titulo_label.pack(pady=20)

# Campos de entrada
item_label = ttk.Label(root, text='Item:')
item_label.pack()
item_entry = ttk.Entry(root)
item_entry.pack()

preco_label = ttk.Label(root, text='Preço:')
preco_label.pack()
preco_entry = ttk.Entry(root)
preco_entry.pack()

quantidade_label = ttk.Label(root, text='Quantidade:')
quantidade_label.pack()
quantidade_entry = ttk.Entry(root)
quantidade_entry.pack()

# Botão para adicionar item
adicionar_button = ttk.Button(root, text='Adicionar Item', command=adicionar_item)
adicionar_button.pack()

# Rótulo para exibir o total
total_label = ttk.Label(root, text='Total: R$ 0.00', font=('Arial', 18, 'bold'))
total_label.pack()

# Lista de itens
lista_itens = tk.Listbox(root, width=50, height=10, font=('Arial', 14))
lista_itens.pack()

# Botão para gerar nota fiscal
gerar_nf_button = ttk.Button(root, text='Gerar Nota Fiscal', command=gerar_nota_fiscal)
gerar_nf_button.pack()

root.mainloop()
