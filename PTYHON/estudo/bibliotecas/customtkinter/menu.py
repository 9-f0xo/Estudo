import customtkinter as ctk
import tkinter as tk

class FrameDeTamanhos(ctk.CTkFrame):
    def __init__(self, app, titulo, valores):
        super().__init__(app)
        self.titulo = titulo
        self.valores = valores
        tamanhos = [
            'Broto', 'Pequena', 'Média', 'Grande', 'Avestruz'
        ]

        # Salvar a referência do label para poder manipulá-lo depois
        self.titulo_widget = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6)
        self.titulo_widget.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.radiobuttons = []  # Inicializando a lista de radiobuttons

        # Variável que controla o valor selecionado
        self.selected_size = tk.IntVar(value=0)  # Inicializa com valor 0 (nenhum selecionado)

        for i, valor in enumerate(self.valores):
            # Passa a mesma 'IntVar' para todos os radiobuttons
            radiobutton = ctk.CTkRadioButton(self, text=f'{tamanhos[i]}: {i+4} fatias, até {valor} sabores', variable=self.selected_size, value=valor)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 10), sticky="ew")
            self.radiobuttons.append(radiobutton)

        # Adicionando um botão para exibir o valor selecionado
        self.show_button = ctk.CTkButton(self, text="Mostrar Seleção", command=self.acessar_valor)
        self.show_button.grid(row=len(self.valores) + 1, column=0, padx=10, pady=10)

    def acessar_valor(self):
        selected_value = self.selected_size.get()
        return selected_value


class FrameDeSabores(ctk.CTkFrame):
    def __init__(self, app, titulo):
        super().__init__(app)
        self.titulo = titulo
        self.sabores = {
            'Perro Roni': 15, 'Muitsarela': 12, 'Lucas': 20, 'Micael': 18, 'Luís': 17, 
            'Yan': 16, '4 Queijos': 22, 'Calabresa': 14, 'Mokele Mbembe': 25, 'Roblox': 30
        }

        # Salvar a referência do label para poder manipulá-lo depois
        self.titulo_widget = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6)
        self.titulo_widget.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.radiobuttons = []  # Inicializando a lista de radiobuttons

        # Variável que controla o valor selecionado
        self.selected_size = tk.IntVar(value=0)  # Inicializa com valor 0 (nenhum selecionado)

        for i, (sabor, valor) in enumerate(self.sabores.items(), start=1):
            self.vars[sabor] = tk.IntVar(value=0)  # Cada Checkbutton tem sua própria variável
            ctk.CTkCheckButton(
                self.janela, text=f"{sabor} - R${valor}", variable=self.vars[sabor],
                onvalue=1, offvalue=0, command=self.atualizar_total
            ).grid(row=i, column=0, sticky='W')

        # Adicionando um botão para exibir o valor selecionado
        self.show_button = ctk.CTkButton(self, text="Mostrar Seleção")
        self.show_button.grid(row=len(self.valores) + 1, column=0, padx=10, pady=10)




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Menu')
        self.geometry('1000x500')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Agora é possível criar vários frames
        self.frame_de_tamanhos = FrameDeTamanhos(self, valores=[2, 3, 4, 5, 6], titulo='Escolha o tamanho da pizza:')
        self.frame_de_tamanhos.grid(row=0, column=2, padx=10, pady=(10, 20), sticky="nw")
        self.frame_de_sabores = FrameDeSabores(self, titulo=f'Escolha o tamanho até')
        self.frame_de_sabores.grid(row=0, column=2, padx=10, pady=(10, 20), sticky="nw")
        


app = App()
app.mainloop()
