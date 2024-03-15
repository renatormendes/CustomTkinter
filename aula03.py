# Importando a biblioteca
import customtkinter as ctk

# Criando a nossa janela
janela = ctk.CTk()


# Configurando a janela principal
janela.title("App Teste - aula03")
janela.geometry("700x400")

# width = altura
# height = largura
janela.maxsize(width = 900, height = 550)
janela.minsize(width = 500, height = 300)
janela.resizable(width = False, height = False)



# Customizando tema da nossa aplicação = Aula-03
# light
# dark
# system
janela._set_appearance_mode("dark")

# Executando a nossa janela
janela.mainloop()