import tkinter as tk
from backend.FilmeBanco import FilmeBanco

mywindow2 = None
textb = None
textb_senha = None
textbId = None
textbNome = None
textbAno = None
textbClassificacao = None
textbUsername = None
listbox = None

def buttonPress():
    global mywindow2
    global textbNome 
    global textbAno
    global textbClassificacao
    global textbUsername
    
    nome   = textbNome.get()
    ano  = textbAno.get()
    classificacao   = textbClassificacao.get()
    username = textbUsername.get()

    l = FilmeBanco()
    l.insert_new_filme(nome, ano, classificacao, username)
    preencher_lista_nome_filmes()

    
def textBox():
    pass
    
def preencher_lista_nome_filmes():
    global listbox 
    l = FilmeBanco()
    lista_filmes_banco_dados  = l.get_all_filmes("*")

    lista_nomes_filmes = []
    for filme in lista_filmes_banco_dados:
        lista_nomes_filmes.append(filme.get_nome())
    
    lista_nomes_filmes.sort(reverse=True)   
    listbox.delete(0, tk.END)
    for nome in lista_nomes_filmes:
      listbox.insert(0, nome)
      
def buttonUpdate():
    global textbId
    global textbNome
    global textbAno
    global textbClassificacao

    id = textbId.get()  
    novo_nome = textbNome.get()  
    novo_ano = textbAno.get() 
    nova_classificacao = textbClassificacao.get()  
    
    l = FilmeBanco()
    l.update_filme(id, novo_nome,novo_ano, nova_classificacao)
    preencher_lista_nome_filmes()

def buttonDelete():
    global textbId
    
    id = textbId.get() 
    l = FilmeBanco()
    l.delete_filme(id)
    preencher_lista_nome_filmes()

def run():
    global mywindow2
    global textbId
    global textbNome 
    global textbAno
    global textbClassificacao  
    global textbUsername
    global listbox 

    mywindow2 = tk.Toplevel()

    mywindow2.geometry("800x400")
    mywindow2.title("Listbox in Tk")
    listbox = tk.Listbox(mywindow2)

    preencher_lista_nome_filmes()

    listbox.grid(row=0, column=0)
   
    button_add = tk.Button(mywindow2, text='Adicionar Filme', command=buttonPress)
    button_add.grid(row=0, column=1)

    button_update = tk.Button(mywindow2, text='Atualizar Filme', command=buttonUpdate)
    button_update.grid(row=0, column=2)

    button_delete = tk.Button(mywindow2, text='Deletar Filme', command=buttonDelete)
    button_delete.grid(row=0, column=3)
    
    textbId = tk.Entry(mywindow2, text="Id do Filme")
    textbId.grid(row=1, column=1)

    textbNome = tk.Entry(mywindow2, text="Nome do Filme")
    textbNome.grid(row=2, column=1)

    textbAno = tk.Entry(mywindow2, text="Ano do filme")
    textbAno.grid(row=3, column=1)

    textbClassificacao = tk.Entry(mywindow2, text="Classificação")
    textbClassificacao.grid(row=4, column=1)
    
    textbUsername = tk.Entry(mywindow2, text="Username")
    textbUsername.grid(row=5,column=1)


 