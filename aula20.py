
# Place (eixo x e eixo y ambos em pixels)
# Pack
# Grid

import customtkinter
import customtkinter as ctk # Importando a biblioteca


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 20")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela
janela.resizable(False, False)

'''
ctk.CTkLabel(
				janela, 
				text="Curso de CustomTkinter - Aula 20 (Widgets com Place)", 
				font=("arial bold", 20)
			).pack(pady=20,padx=5)
'''


######################################################################

btn1 = ctk.CTkButton(janela, text="Botão 1")
btn1.place(x=20, y=40)

# Posicionamento normal
btn2 = ctk.CTkButton(janela, text="Botão 2")
btn2.place(x=70, y=40)

# Posicionamento com responsividade
btn3 = ctk.CTkButton(janela, text="Botão 3")
btn3.place(relx=0.1, rely=0.2)

#btn4 = ctk.CTkButton(janela, text="Botão 4'")
#btn4.place(relx=0.2, rely=0.1)

######################################################################

janela.mainloop()