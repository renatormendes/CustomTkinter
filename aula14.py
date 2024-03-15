import customtkinter
import customtkinter as ctk # Importando a biblioteca


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 14")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 14 (Slider)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)



######################################################################
def slider_value(value):
	if value == 0:
		slider.configure(fg_color="red")
	else:
		slider.configure(fg_color="green")
	print(value)


slider = ctk.CTkSlider(janela,
						from_=0, 
						to=100,
						command=slider_value,
						width=500,
						button_color="red",
						button_hover_color="teal",
						button_length=10,
						corner_radius=10,
						fg_color="green",
						progress_color="#028"
					).pack(pady=30)

######################################################################

janela.mainloop()