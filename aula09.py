import customtkinter as ctk # Importando a biblioteca

janela = ctk.CTk() # Criar a nossa janela

# Configurando a nossa janela principal
janela.title("App Teste - Aula 09")		# Colocando título
janela.geometry("700x400") 				# Dimensão inicial da janela


# Aula 09 - Trabalhando com OptionMenu
ctk.CTkLabel(
				janela,
				text="Menu de Opções. Aula - 09",
				font=("arial bold", 20)
			).pack(pady=20, padx=5)

ctk.CTkLabel(
				janela,
				text="Escolha o seu mês de nascimento: ", 
				font=("arial bold", 14)
			).pack()


def mes_nascimento(escolha):
	print(f"O seu mês de nascimento é {escolha}")


mes = ctk.CTkOptionMenu(
					janela,
					values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
					command=mes_nascimento,
					corner_radius=30,
					fg_color="red",
					button_color="lightgreen",
					button_hover_color="teal",
					dropdown_fg_color="teal",
					dropdown_text_color="red",
					dropdown_font=("arial bold", 12),
					dropdown_hover_color="white"
				)
mes.pack(pady=10)
mes.set("Escolha o mês")




janela.mainloop()