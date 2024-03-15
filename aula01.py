# Importando a biblioteca
import customtkinter as s


# Criando a nossa janela
janela = s.CTk()

# Define a cor da tela
janela._set_appearance_mode("dark")
# janela._set_appearance_mode("light")
# janela._set_appearance_mode("system")


btn = s.CTkButton(master = janela, text = "")


# Executando a nossa janela
janela.mainloop()