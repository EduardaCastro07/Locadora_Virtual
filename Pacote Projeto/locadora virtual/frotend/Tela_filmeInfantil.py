import tkinter as tk
from backend.FilmesInfantisBanco import FilmeInfantilBanco

def preencher_lista_nome_filmes(listbox):
    l = FilmeInfantilBanco()
    lista_filmes_banco_dados = l.get_filmes_infantis("*")

    # Limpa a listbox antes de preencher
    listbox.delete(0, tk.END)

    for filme in lista_filmes_banco_dados:
        listbox.insert(tk.END, filme.nome)  # Supondo que a classe Filmes_Infantis tenha um atributo nome

def run():
    root = tk.Tk()
    root.title("Filmes Infantis")

    # Criação de um Listbox
    listbox = tk.Listbox(root, width=50)
    listbox.pack(pady=10)

    # Botão para preencher a lista
    preencher_btn = tk.Button(root, text="Carregar Filmes Infantis", command=lambda: preencher_lista_nome_filmes(listbox))
    preencher_btn.pack(pady=5)

    # Preenche a lista ao iniciar
    preencher_lista_nome_filmes(listbox)

    root.mainloop()


      
      