import customtkinter
import customtkinter as ctk # Importando a biblioteca


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 16")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 16 (Switch)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)


######################################################################
switch_var = ctk.StringVar(value="on")

def event():

	if switch_var.get() == "Ativado":
		ctk.set_appearance_mode("Light")
	elif switch_var.get() == "Desativado":
		ctk.set_appearance_mode("Dark")
	else:
		ctk.set_appearance_mode("System")
	

switch = ctk.CTkSwitch(janela,
						text="Switch",
						command=event,
						variable=switch_var,
						onvalue="Ativado",
						offvalue="Desativado",
						fg_color="teal"
					).pack(pady=30)

######################################################################

janela.mainloop()