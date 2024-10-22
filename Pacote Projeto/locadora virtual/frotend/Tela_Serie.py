import tkinter as tk
from backend.SerieBanco import SerieBanco

mywindow2 = None
textbId = None
textbNome = None
textbAno = None
textbClassificacao = None
textbTemporadas = None
listbox = None

def buttonPress():
    
    global mywindow2
    global textbNome
    global textbAno
    global textbClassificacao
    global textbTemporadas
    
    nome = textbNome.get()
    ano = textbAno.get()
    classificacao = textbClassificacao.get()
    temporadas = textbTemporadas.get()

    s = SerieBanco()
    s.insert_new_serie(nome, ano, classificacao, temporadas)
    preencher_lista_series()
    
def textBox():
    pass

def preencher_lista_series():
    global listbox
    s = SerieBanco()
    lista_series_banco_dados = s.get_all_series("*")

    lista_nome_series = []
    for serie in lista_series_banco_dados:
        lista_nome_series.append(serie.get_nome())

    lista_nome_series.sort(reverse=True)
    listbox.delete(0, tk.END)
    for nome in lista_nome_series:
        listbox.insert(0, nome)
        
def buttonUpdate():
    global textbId
    global textbNome
    global textbAno
    global textbClassificacao
    global textbTemporadas

    id = textbId.get()  
    novo_nome = textbNome.get()  
    novo_ano = textbAno.get()  
    nova_temporadas = textbTemporadas.get()
    nova_classificacao = textbClassificacao.get()  

    l = SerieBanco()
    l.update_serie(id, novo_nome, novo_ano,nova_temporadas, nova_classificacao)
    preencher_lista_series()

def buttonDelete():
    global textbId
    
    id = textbId.get()  
    l = SerieBanco()
    l.delete_serie(id)
    preencher_lista_series()

def run():
    global mywindow2
    global textbId
    global textbNome
    global textbAno
    global textbClassificacao
    global textbTemporadas
    global listbox

    mywindow2 = tk.Toplevel()
    
    mywindow2.geometry("800x400")
    mywindow2.title("Gerenciamento de Séries")
    listbox = tk.Listbox(mywindow2)

    preencher_lista_series()
    
    listbox.grid(row=0, column=0)

    button = tk.Button(mywindow2, text='Adicionar Série', command=buttonPress)
    button.grid(row=0, column=1)
    
    button_update = tk.Button(mywindow2, text='Atualizar Serie', command=buttonUpdate)
    button_update.grid(row=0, column=2)

    button_delete = tk.Button(mywindow2, text='Deletar Serie', command=buttonDelete)
    button_delete.grid(row=0, column=3)
    
    textbId = tk.Entry(mywindow2, text="Id da série")
    textbId.grid(row=1, column=1)

    textbNome = tk.Entry(mywindow2, text="Nome da Serie")
    textbNome.grid(row=2, column=1)

    textbAno = tk.Entry(mywindow2, text= "Ano da Serie")
    textbAno.grid(row=3, column=1)

    textbClassificacao = tk.Entry(mywindow2, text="Classificação da Serie")
    textbClassificacao.grid(row=4, column=1)
    
    textbTemporadas = tk.Entry(mywindow2, text="Temporadas")
    textbTemporadas.grid(row=5, column=1)

    
    

