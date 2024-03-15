import customtkinter as ctk # Importando a 
from tkinter import *

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 11 (Entry)")		# Colocando título
janela.geometry("700x400") 						# Dimensão inicial da janela

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 11 (Entry)", 
				font=("arial bold", 20)).pack(pady=20,padx=5)


def pegar():
	print(entry.get())
	entry.delete(0, END)
	

'''
def apagar():
	entry.delete(0, END)
	pass


ctk.CTkButton(janela, width=300, text="Apagar Texto", command=apagar).pack(pady=5)
'''

entry = ctk.CTkEntry(
						janela, 
						width=300, 
						placeholder_text="Digite o seu nome completo...",
						placeholder_text_color="green",
						fg_color="transparent",
						text_color="teal",
						font=("arial bold", 16),
						border_width=2,
						border_color="#FFF",
						state="normal", 
						corner_radius=20
					)
entry.pack(pady=20)

ctk.CTkButton(
				janela, 
				width=300,
				text="Pegar Texto",
				command=pegar
			).pack()






janela.mainloop()