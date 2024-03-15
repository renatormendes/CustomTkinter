# Importando a biblioteca
import customtkinter as ctk

# Criando a nossa janela
janela = ctk.CTk()


# Configurando a janela principal
janela.title("App Teste - aula08 - Caixa de Diálogo")
janela.geometry("700x400")

# width = altura
# height = largura
janela.maxsize(width = 900, height = 550)
janela.minsize(width = 500, height = 300)
janela.resizable(width = False, height = False)

# Customizando tema da nossa aplicação
# light, dark ou system

#janela._set_appearance_mode("light")

# Aula 08 - Caixa de Dialogo

def abrir():
	dialog = ctk.CTkInputDialog(
									title="Caixa de Diálogo", 
									text="Digite o seu número de celular...", 
									entry_border_color="red"
								)
	print("Número de Celular informado: ", dialog.get_input()) # Imprime no terminal o conteúdo digitado na caixa de texto



btn = ctk.CTkButton(janela, text="Abrir caixa de Diálogo", command=abrir)
btn.pack()


# Executando a nossa janela
janela.mainloop()