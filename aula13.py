import customtkinter
import customtkinter as ctk # Importando a biblioteca
from tkinter import *
from PIL import Image

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 13")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela

ctk.CTkLabel(janela, 
				text="Curso de CustomTkinter - Aula 13 (Imagem)", 
				font=("arial bold", 20),
				bg_color="transparent",
			).pack(pady=20,padx=5)

# Customizando tema da nossa aplicação
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

######################################################################

# Carregando uma imagem e definindo seu tamanho
img1 = ctk.CTkImage(
					light_image=Image.open("./icones/mensagem.png"), 
					dark_image=Image.open("./icones/mensagem.png"),
					size=(80, 80)
				)

img2 = ctk.CTkImage(
					light_image=Image.open("./icones/mundo.png"), 
					dark_image=Image.open("./icones/mundo.png"),
					size=(80, 80)
				)

# Colocando uma imagem dentro de um label
ctk.CTkLabel(janela,
				text=None,
				image=img1, 
				bg_color="transparent"
			).pack()

ctk.CTkLabel(janela,
				text=None,
				image=img2,
				bg_color="transparent"
			).pack()

######################################################################
janela.mainloop()