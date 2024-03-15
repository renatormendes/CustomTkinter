import customtkinter
import customtkinter as ctk # Importando a biblioteca


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 18")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela
janela.resizable(False, False)

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 18 (RadioButton)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)



######################################################################

radio_var = ctk.IntVar(value=0)

def radio_event():
	v = radio_var.get()

	if v == 1:
		print("Masculino")
	else:
		print("Feminino")
	
	#print(radio_var.get())
	pass

radio1 = ctk.CTkRadioButton(janela,
								text="Masculino",
								command=radio_event,
								variable=radio_var,
								value=1
							).pack(pady=20)

radio2 = ctk.CTkRadioButton(janela,
								text="Feminino",
								command=radio_event,
								variable=radio_var,
								value=2
							).pack(pady=20)
######################################################################

janela.mainloop()