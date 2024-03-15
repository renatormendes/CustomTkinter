import customtkinter
import customtkinter as ctk # Importando a biblioteca


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 09")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela
janela.resizable(False, False)

ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 12 (Button)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)



######################################################################



######################################################################

janela.mainloop()