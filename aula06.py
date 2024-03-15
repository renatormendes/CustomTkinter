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

# Customizando tema da nossa aplicação = Aula-03
# light
# dark
# system
#janela._set_appearance_mode("light")

# Aula 06 - Tabview (Abas no CustomTkinter)
tabview = ctk.CTkTabview(
							janela, 
							width = 400,                                    # tamanho da janela
							corner_radius = 20,                             # Tamanho do raio do corner
							bg_color = "transparent",                       # Cor de fundo do tabview
							border_width = 3,                               # Tamanho da borda
							border_color = "red",                           # Cor da borda
							fg_color = "teal",                              # Cor de fundo da borda
							segmented_button_fg_color="red",                # Cor de fundo das abas do tabview
							segmented_button_selected_color="green",        # Cor do botão selecionado
							segmented_button_unselected_hover_color="blue", # Cor de fundo do botão não selecionado ao passar o mouse
							segmented_button_unselected_color="yellow"      # Cor de fundo do botão não selecionado
						)
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Genero")

tabview.tab("Nomes").grid_columnconfigure(0, weight = 1)
tabview.tab("Idades").grid_columnconfigure(0, weight = 1)
tabview.tab("Genero").grid_columnconfigure(0, weight = 1)

text = ctk.CTkLabel(tabview.tab("Nomes"), text = "Salvador Eduardo\nEugenio Eduardo\nAntonia Tomocema\n")
text.place(x = 10, y = 10)

idd = ctk.CTkLabel(tabview.tab("Idades"), text = "23\n31\n42\n")
idd.place(x = 10, y = 10)

text = ctk.CTkLabel(tabview.tab("Genero"), text = "Masculino\nMasculino\nFeminino\n")
text.place(x = 10, y = 10)

# Executando a nossa janela
janela.mainloop()