# Importando a biblioteca
import customtkinter as ctk

# Criando a nossa janela
janela = ctk.CTk()


# Configurando a janela principal
janela.title("App Teste - aula02")
janela.geometry("700x400")

# width = altura
# height = largura
janela.maxsize(width = 900, height = 550)
janela.minsize(width = 500, height = 300)
janela.resizable(width = True, height = False)
janela.iconify()
janela.deiconify()




# Executando a nossa janela
janela.mainloop()