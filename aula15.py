import customtkinter		# Importando a biblioteca
import customtkinter as ctk 
from tkinter import *
from PIL import Image


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 15")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 15 (Segmented Button)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)

######################################################################

def btn(value):
	print("Esta no segmento ", value)

	
segmented_button_var = ctk.StringVar(value="Django")

segmented_button = ctk.CTkSegmentedButton(janela,
									values=[
											"Tkinter",
											"Django",
											"Flask"
									],
									variable=segmented_button_var,
									command=btn, 
									corner_radius=15,
									fg_color="teal", 
									selected_color="red", 
									selected_hover_color="green"
								).pack(pady=20)

######################################################################

janela.mainloop()