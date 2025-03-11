import customtkinter as ctk
from tkinter import messagebox


class FrameDeTamanhos(ctk.CTkFrame):
    def __init__(self, app, titulo, valores):
        super().__init__(app)
        self.titulo = titulo
        self.valores = valores
        tamanhos = ['Broto', 'Pequena', 'Média', 'Grande', 'Avestruz']
        self.tamanho = ctk.IntVar()

        self.titulo_frame = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="sew")
        
        for i, valor in enumerate(self.valores):
            radiobutton = ctk.CTkRadioButton(self, text=f'{tamanhos[i]}: {(i+1)*4} fatias, até {valor} sabores', variable=self.tamanho, value=i, command=self.acessar_Tamanho)

            radiobutton.grid(row=i+1, column=0, columnspan=2, padx=10, pady=5, sticky="sew")

    def acessar_Tamanho(self):
        print('Funfando')

    def confirmarEscolha(self):
        if self.tamanho.get() == 0:
            messagebox.showerror('ERRO', 'É obrigatório escolher algum tamanho de pizza.')
            return False
        else: return True


class FrameDeSabores(ctk.CTkFrame):
    def __init__(self, app, titulo):
        super().__init__(app)
        self.titulo = titulo
        self.vars = {}
        self.totalVal = ctk.DoubleVar(value=0.0)  # Inicializa o total como 0
        self.qtd_sabores_escolhidos = 0
        
        self.titulo_frame = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="sew")
        
        self.sabores = {
            'Perro Roni': 15, 'Mozzarella': 12, 'Lucas': 20, 'Calabreso (Lá ele)': 18, 'Luís': 17, 
            'Yan': 16, '4 Queijos': 22, 'Terracota Pie': 14, 'Mokele Mbembe': 25, 'Roblox': 30
        }
        
        for i, (sabor, valor) in enumerate(self.sabores.items(), start=1):
            self.vars[sabor] = ctk.IntVar(value=0)
            ctk.CTkCheckBox(self, text=f"{sabor} - R${valor}", variable=self.vars[sabor],
                onvalue=1, offvalue=0, command=self.acessar_valDosSabores).grid(row=i, column=0, padx=10, pady=5, sticky="we")
            
    def acessar_valDosSabores(self):
        # Obtém o tamanho escolhido
        tamanho_escolhido = app.frame_de_tamanhos.tamanho.get()
        if tamanho_escolhido < 0:
            return  # Nenhum tamanho foi selecionado ainda

        limite_sabores = app.frame_de_tamanhos.valores[tamanho_escolhido]  # Obtém o limite de sabores
        self.qtd_sabores_escolhidos = sum(var.get() for var in self.vars.values())

        if self.qtd_sabores_escolhidos > limite_sabores:
            messagebox.showwarning("Limite atingido", f"Você pode escolher no máximo {limite_sabores} sabores.")
            for sabor, var in self.vars.items():
                if var.get() == 1:
                    var.set(0)  # Desmarca o último selecionado'

class FrameDeAdicionais(ctk.CTkFrame):
    def __init__(self, app, titulo):
        super().__init__(app)
        
        self.titulo = titulo
        self.titulo_frame = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="sew")

        self.quantidade = [str(i) for i in range(11)]
        self.comboboxes = {}
        self.adicionais = {
            'Coca-Cola 2L': 10, 'Pepsi 2L': 9, 'Sprite 2L': 9, 'Fanta Laranja 2L': 8,
            'Coca-Cola 1,5L': 9, 'Pepsi 1,5L': 7.50, 'Sprite 1,5L': 7.50, 'Fanta Laranja 1,5L': 6.70,
        }
        
        for i, (adicional, valor) in enumerate(self.adicionais.items(), start=1):
            ctk.CTkLabel(self, text=f"{adicional} - R${valor}").grid(row=i, column=0, padx=10, pady=5, sticky="we")
            combobox = ctk.CTkComboBox(self, values=self.quantidade, state="readonly", command=self.acessar_valDosAdicionais)
            combobox.set("0")
            combobox.grid(row=i, column=1, padx=10, pady=5, sticky='we')
            self.comboboxes[adicional] = combobox

    def acessar_valDosAdicionais(self):
        print('Funfando')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Menu')
        self.geometry('800x550')
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(0, weight=1)

        label1 = ctk.CTkLabel(self, text='Escolha como deseja que seu pedido seja realizado!', font=("Arial", 16))
        label2 = ctk.CTkLabel(self, text='Após escolher o tamanho, sabores e adicionais, clique no botão abaixo para confirmar seu pedido.', font=("Arial", 14))
        
        label1.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="sew")
        label2.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="sew")
        
        self.frame_de_tamanhos = FrameDeTamanhos(self, valores=[2, 3, 4, 5, 6], titulo='Escolha o tamanho da pizza:')
        self.frame_de_tamanhos.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.frame_de_sabores = FrameDeSabores(self, titulo='Escolha seus sabores')
        self.frame_de_sabores.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        self.frame_de_adicionais = FrameDeAdicionais(self, titulo='Escolha seus adicionais')
        self.frame_de_adicionais.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        
        self.botao_confirmar = ctk.CTkButton(self, text='Confirmar', command=self.confirmar_escolhas)
        self.botao_confirmar.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="sew")

    def atualizarPreco_total(self):
        preco_total = 0

        label_total = ctk.CTkLabel(self, text=f'Total: R${preco_total:.2f}', font=("Arial", 14))
        label_total.grid(row=1, column=2, columnspan=4, padx=10, pady=5, sticky="sew")
    
    def confirmar_escolhas(self):
        if not self.frame_de_tamanhos.confirmarEscolha():
            return
        else:
            self.destroy()


ctk.set_appearance_mode('dark')
app = App()
app.mainloop()
