import tkinter as tk
from backend.UsuarioBanco import UsuarioBanco
from . import Tela_Filme 
from . import Tela_Serie
from . import Tela_filmeInfantil

mywindow = None
textb = None
textb_senha = None

def buttonPress():
    global textb
    global textb_senha
    global mywindow
    global label

    nome_digitado = textb.get()
    senha_digitado = textb_senha.get()

    print("Pessoa digitou o username: " + nome_digitado)
    print("Pessoa digitou a senha   : " + senha_digitado)

    gerenciador_usuario = UsuarioBanco()
    usuario_banco = gerenciador_usuario.get_usuario_by_username(nome_digitado)

    if usuario_banco is not None:
        senha_armazenada = str(usuario_banco.get_senha())  # Convertendo para string
        print("Senha armazenada no banco de dados: " + senha_armazenada)

        # Comparar as senhas, removendo espaços em branco e comparando como strings
        if senha_digitado.strip() == senha_armazenada.strip():
            label.config(text="Você fez o login com sucesso!!!")
            print("Você fez o login com sucesso!!!")
            Tela_Filme.run()
            Tela_Serie.run()
            Tela_filmeInfantil.run()
        else:
            label.config(text="Senha errada!")
            print("Senha errada!")
    else:
        label.config(text="Usuário não encontrado!!!")
        print("Usuário não encontrado!!!")

def textBox():
    print(textb.get())
    

def run():
    global textb
    global textb_senha
    global mywindow
    global label
    

    mywindow = tk.Tk()

    #Label
    label = tk.Label(mywindow, text="Label Text")
    label.grid(row=0,column=1)

    #Button
    button = tk.Button(mywindow,text='Press',command=buttonPress)
    button.grid(row=1,column=1)

    #Textbox
    textb = tk.Entry(mywindow,      text="Entry")
    textb.grid(row=2,column=1)

    textb_senha = tk.Entry(mywindow,text="Entry2")
    textb_senha.grid(row=3,column=1)


    mywindow.mainloop()