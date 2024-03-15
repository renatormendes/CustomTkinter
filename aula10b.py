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
# Introduzindo texto por ENTRY (forma mais prática)
def enviar():
	t = entry.get()
	lab1.configure(text=str(t))



lab1 = ctk.CTkLabel(janela, 
					text="", 
					width=200, 
					height=25, 
					text_color="lightblue", 
					font=("arial bold", 16), 
					fg_color="teal", 
					corner_radius=10
				)

lab1.pack(pady=10)

entry = ctk.CTkEntry(janela, width=200)
entry.pack()

ctk.CTkButton(janela, text="Enviar", width=200, command=enviar).pack(pady=10)



janela.mainloop()