import customtkinter as ctk


class RadiobuttonsEframes(ctk.CTkFrame):
    def __init__(self, app, valores, titulo):
        super().__init__(app)
        self.grid_columnconfigure(0, weight=1)
        self.valores = valores
        self.radiobuttons = []
        self.titulo = titulo
        self.variavel = ctk.StringVar(value="")

        self.titulo = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6).grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        for i, valor in enumerate(self.valores):
            radiobutton = ctk.CTkRadioButton(self, text=f'Valor: {valor}', variable=self.variavel)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 10), sticky="ew")
            self.radiobuttons.append(radiobutton)

    def valores_dosBotoes(self):
        radiobuttons_assinaladas = []
        for buttons in self.radiobuttons:
            if buttons.get() == 1:
                radiobuttons_assinaladas.append(radiobuttons.cget("text")) # Armazena 'text=' de cada checkbox
        return radiobuttons_assinaladas # Retorna a lista de caixas que foram assinaladas



class CheckboxesEframes(ctk.CTkFrame):
    def __init__(self, app, valores, titulo):
        super().__init__(app)
        self.grid_columnconfigure(0, weight=1)
        self.valores = valores
        self.checkboxes = []
        self.titulo = titulo

        self.titulo = ctk.CTkLabel(self, text=self.titulo, fg_color="gray30", corner_radius=6).grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        for i, valor in enumerate(self.valores):
            checkbox = ctk.CTkCheckBox(self, text=f'Valor: {valor}')
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 10), sticky="ew")
            self.checkboxes.append(checkbox)

    def valores_dasCaixas(self):
        checkboxes_assinaladas = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checkboxes_assinaladas.append(checkbox.cget("text")) # Armazena 'text=' de cada checkbox
        return checkboxes_assinaladas # Retorna a lista de caixas que foram assinaladas



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Uso dos Frames')
        self.geometry('400x350')
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Agora é possível criar vários frames
        self.checkboxFrame1 = CheckboxesEframes(self, valores=[1,2,3,4,5], titulo='Valores numéricos')
        self.checkboxFrame2 = CheckboxesEframes(self, valores=["Um", "Dois", 'Três'], titulo='Valores por extenso')

        self.radiobuttonFrame = RadiobuttonsEframes(self, valores=["A", "B", 'C'], titulo='Valores alfabéticos')
        self.radiobuttonFrame.grid(row=0, column=2, padx=10, pady=(10, 20), sticky="nsew")

        # Podemos configurar da maneira que quisermos nosso frame
        self.checkboxFrame2.configure(fg_color='transparent')

        self.checkboxFrame1.grid(row=0, column=0, padx=10, pady=(10, 20), sticky="nsew")
        self.checkboxFrame2.grid(row=0, column=1, padx=10, pady=(10, 20), sticky="nsew")

        ctk.CTkButton(self, text='Botão chato', command=self.botao_Pressionado).grid(column=0, row=1, sticky='ew', columnspan=3, pady=(10,20), padx=10)

    def botao_Pressionado(self):
        print('Para de me cutucar!!')
        print(self.checkboxFrame1.valores_dasCaixas())
        print(self.checkboxFrame2.valores_dasCaixas())
        print(self.radiobuttonFrame.valores_dosBotoes())
        self.destroy()
        pass


# main
app = App()
app.mainloop()