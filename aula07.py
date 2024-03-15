# Importando a biblioteca
import customtkinter as ctk

# Criando a nossa janela
janela = ctk.CTk()


# Configurando a janela principal
janela.title("App Teste - aula06 - Tabs (Abas)")
janela.geometry("700x400")

# width = altura
# height = largura
janela.maxsize(width = 900, height = 550)
janela.minsize(width = 500, height = 300)
janela.resizable(width = False, height = False)

# Customizando tema da nossa aplicação
# light, dark ou system

#janela._set_appearance_mode("light")

# Aula 07 - TextBox (Caixa de texto no CustomTkinter)

textbox = ctk.CTkTextbox(
							janela, 
							width=300, 							 # largura
							height=350,							 # altura
							scrollbar_button_color="green",      # Altera a cor da barra de rolagem
							scrollbar_button_hover_color="cyan", # Altera a cor da barra de rolagem na passagem do mouse
							border_color="red", 				 # Cor da borda
							border_width=5, 					 # Tamanho da borda
							corner_radius=15,					 # Raio do corner
							fg_color="teal",					 # Cor de fundo do TextBox
							border_spacing=20,					 # Espaçamento da borda
							activate_scrollbars=True			 # Oculta ou mostra a barra de rolagem vertical
						)
textbox.pack()

textbox.insert("0.0", "Título do seu texto\n\n" + "Olá dev, estou aqui programando interfaces gráficas com customtkinter no canal set-escola de programação e esta sendo uma boa.\n\n" * 20)


# Executando a nossa janela
janela.mainloop()