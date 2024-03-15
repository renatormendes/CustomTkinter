import customtkinter
import customtkinter as ctk # Importando a biblioteca


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 17")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 17 (CheckBox)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)



######################################################################

ctk.CTkLabel(janela,
				text="Usando um CheckBox com CustomTKinter",
				font=("arial bold", 15)
			).pack(pady=30)

check_var = ctk.StringVar(value="off")

def check_value():
	valor=check_var.get()

	if valor == "on":
		print("Tema Claro")
		ctk.set_appearance_mode("Light")
	elif valor == "off":
		print("Tema escuro")
		ctk.set_appearance_mode("Dark")
	else:
		print("Tema do sistema")
		ctk.set_appearance_mode("System")
	print(valor)

checkbox = ctk.CTkCheckBox(janela,
							text="Checkbox - Altera o tema",
							variable=check_var,
							onvalue="on",
							offvalue="off",
							command=check_value
						).pack(pady=10)

######################################################################

janela.mainloop()