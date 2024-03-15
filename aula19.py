import customtkinter
import customtkinter as ctk # Importando a biblioteca


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 19")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela
janela.resizable(False, False)

# Label de Apresentação
ctk.CTkLabel(janela, 
				text="Curso de CustomTkinter - Aula 19 (ProgressBar)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)


######################################################################

progressbar = ctk.CTkProgressBar(janela, 
									width=300, 
									height=20, 
									corner_radius=30,
									fg_color="#003",
									progress_color="#060"
								)
progressbar.pack(pady=20)
progressbar.start()
#progressbar.step()
#progressbar.stop()

######################################################################

janela.mainloop()