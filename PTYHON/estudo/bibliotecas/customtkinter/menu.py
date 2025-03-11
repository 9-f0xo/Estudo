import customtkinter as ctk
from tkinter import messagebox


class FrameDeTamanhos(ctk.CTkFrame):
    def __init__(self, app, titulo, valores):
        super().__init__(app)
        self.app = app
        self.titulo = titulo
        self.valores = valores
        tamanhos = ['Broto', 'Pequena', 'Média', 'Grande', 'Avestruz']
        self.tamanho = ctk.IntVar(value=-1)

        self.titulo_frame = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="sew")
        
        for i, valor in enumerate(self.valores):
            radiobutton = ctk.CTkRadioButton(self, text=f'{tamanhos[i]}: {(i+1)*4} fatias, até {valor} sabores', 
                variable=self.tamanho, value=i, command=self.acessar_Tamanho)
            radiobutton.grid(row=i+1, column=0, columnspan=2, padx=10, pady=5, sticky="sew")

    def acessar_Tamanho(self):
        self.app.atualizarPreco_total()

    def confirmarEscolha(self):
        if self.tamanho.get() == -1:
            messagebox.showerror('ERRO', 'É obrigatório escolher algum tamanho de pizza.')
            return False
        return True


class FrameDeSabores(ctk.CTkFrame):
    def __init__(self, app, titulo):
        super().__init__(app)
        self.app = app
        self.vars = {}

        self.titulo_frame = ctk.CTkLabel(self, text=titulo, fg_color="gray30", corner_radius=6)
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
        tamanho_escolhido = self.app.frame_de_tamanhos.tamanho.get()
        if tamanho_escolhido < 0:
            return  # Nenhum tamanho foi selecionado ainda

        limite_sabores = self.app.frame_de_tamanhos.valores[tamanho_escolhido]
        qtd_sabores = sum(var.get() for var in self.vars.values())

        if qtd_sabores > limite_sabores:
            messagebox.showwarning("Limite atingido", f"Você pode escolher no máximo {limite_sabores} sabores.")
            for sabor, var in self.vars.items():
                if var.get() == 1:
                    var.set(0)  # Desmarca o último selecionado
        
        self.app.atualizarPreco_total()


class FrameDeAdicionais(ctk.CTkFrame):
    def __init__(self, app, titulo):
        super().__init__(app)
        self.app = app
        
        self.titulo_frame = ctk.CTkLabel(self, text=titulo, fg_color="gray30", corner_radius=6)
        self.titulo_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="sew")

        self.adicionais = {
            'Coca-Cola 2L': 10, 'Pepsi 2L': 9, 'Sprite 2L': 9, 'Fanta Laranja 2L': 8,
            'Coca-Cola 1,5L': 9, 'Pepsi 1,5L': 7.50, 'Sprite 1,5L': 7.50, 'Fanta Laranja 1,5L': 6.70,
        }
        
        self.comboboxes = {}
        
        for i, (adicional, valor) in enumerate(self.adicionais.items(), start=1):
            ctk.CTkLabel(self, text=f"{adicional} - R${valor}").grid(row=i, column=0, padx=10, pady=5, sticky="we")
            combobox = ctk.CTkComboBox(self, values=[str(i) for i in range(11)], state="readonly",
                command=self.acessar_valDosAdicionais)
            combobox.set("0")
            combobox.grid(row=i, column=1, padx=10, pady=5, sticky='we')
            self.comboboxes[adicional] = combobox

    def acessar_valDosAdicionais(self, event=None):
        '''O event=None é um parâmetro opcional da função acessar_valDosAdicionais. Ele permite que a função seja chamada tanto manualmente quanto automaticamente por eventos da interface gráfica (como mudanças em um ComboBox).'''
        self.app.atualizarPreco_total()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Menu')
        self.geometry('820x580')
        self.total_label = ctk.CTkLabel(self, text='Total: R$0.00', font=("Arial", 14))
        self.total_label.grid(row=4, column=0, columnspan=4, padx=10, pady=5, sticky="sew")

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
        total = sum(valor for sabor, valor in self.frame_de_sabores.sabores.items() if self.frame_de_sabores.vars[sabor].get())
        total += sum(int(self.frame_de_adicionais.comboboxes[adicional].get()) * valor for adicional, valor in self.frame_de_adicionais.adicionais.items())
        self.total_label.configure(text=f'Total: R${total:.2f}')
    
    def confirmar_escolhas(self):
        if not self.frame_de_tamanhos.confirmarEscolha():
            return
        self.destroy()

ctk.set_appearance_mode('dark')
app = App()
app.mainloop()
