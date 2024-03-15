import customtkinter as ctk

largura = 400
altura = 300



janela = ctk.CTk()

lagura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

posx = lagura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.title("SISCAD - Tela de Login")
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) # largura x altura + posição x + posição y
janela.resizable(False, False)

############## Componentes ##############

ctk.CTkLabel(janela,
             text="FAÇA LOGIN",
             font=("Georgia", 40),
             ).place(x=80, y=20)

ctk.CTkEntry(janela,
             placeholder_text="Username...",
             corner_radius=30,
             width=250
             ).place(x=80, y=100)

ctk.CTkEntry(janela,
             placeholder_text="Password...",
             corner_radius=30,
             width=250,
             show="*"
             ).place(x=80, y=150)

def realiza_conexao():
    print("Você clicou no botão CONECTAR...")
    print("Configurar para realizar o login com o banco de dados...")
    pass

ctk.CTkButton(janela,
              text="Conectar",
              command=realiza_conexao,
              width=200,
              corner_radius=30
              ).place(x=105, y=200)

janela.mainloop()