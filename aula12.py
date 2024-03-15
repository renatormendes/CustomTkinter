import customtkinter as ctk # Importando a biblioteca
from tkinter import *
from PIL import Image

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 12")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 12 (Button)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)
######################################################################

img = ctk.CTkImage(
					light_image=Image.open("./icones/clique.png"), 
					dark_image=Image.open("./icones/clique.png"),
					size=(80, 80)
				)

def evento():
	print("O botão foi clicado.")
	pass


ctk.CTkButton(
				janela,
				text="YouTube",
				command=evento, 
				width=300,
				height=100,
				fg_color="transparent",
				hover_color="green",
				text_color="red",
				font=("arial bold", 18),
				border_color="#ABF",
				border_width=3,
				border_spacing=2,
				corner_radius=20,
				state="normal",
				image=img
			).pack(pady=30)




######################################################################
janela.mainloop()