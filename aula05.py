# Importando a biblioteca
import customtkinter as ctk

# Criando a nossa janela
janela = ctk.CTk()


# Configurando a janela principal
janela.title("App Teste - aula05 - Frames, Bordas e Labels")
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

# Criando um frames, labels e bordas e posicionando os mesmos
frame1 = ctk.CTkFrame(janela, width = 200, height = 100, fg_color= "lightgreen", bg_color = "transparent", corner_radius = 10, border_color = "yellow", border_width = 10).place(x = 10, y = 10)
label1 = ctk.CTkLabel(frame1, text="CTkLabel1", bg_color="lightgreen").place(x = 75, y = 45)

frame2 = ctk.CTkFrame(janela, width = 200, height = 100, fg_color= "lightblue", bg_color = "transparent", border_color = "teal", corner_radius = 10, border_width = 10).place(x = 220, y = 10)
label2 = ctk.CTkLabel(frame2, text="CTkLabel2", bg_color="lightblue").place(x = 290, y = 45)

frame3 = ctk.CTkFrame(janela, width = 200, height = 100, fg_color= "magenta", bg_color = "transparent", border_color = "brown", corner_radius = 10, border_width = 10).place(x = 430, y = 10)
label3 = ctk.CTkLabel(frame3, text="CTkLabel3", bg_color="magenta").place(x = 500, y = 45)


# Executando a nossa janela
janela.mainloop()