import customtkinter as ctk # Importando a biblioteca

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 10 - Labels")		# Colocando título
janela.geometry("700x400")			 				# Dimensão inicial da janela
janela.maxsize(700, 400)							# Tamanho máximo da janela
janela.minsize(700, 400)							# Tamanho mínimo da janela

# Aula 10 - customTkinter  Labels
ctk.CTkLabel(janela, text="Curso de CustomTkinter - Aula 10 (Labels)", font=("arial bold", 20)).pack(pady=20,padx=5)

ctk.CTkLabel(janela, text="Digite seu nome completo: ").pack()

# Trabalhando com label de forma dinâmica

# 1ª forma - introduzindo texto por input

text_var = ctk.StringVar(value=input("Digite seu nome completo: "))

lab = ctk.CTkLabel(janela, 
					textvariable=text_var, 
					width=200, 
					height=25, 
					text_color="red", 
					font=("arial bold", 16)
				)

lab.pack(pady=10)




janela.mainloop()