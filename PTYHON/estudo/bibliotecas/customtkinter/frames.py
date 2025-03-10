import customtkinter as ctk

class CheckboxesEframes(ctk.CTkFrame):
    def __init__(self, app, valores):
        super().__init__(app)
        self.valores = valores
        self.checkboxes = []

        for i, value in enumerate(self.valores):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def valores_dasCaixas(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Uso dos Frames')
        self.geometry('400x400')
        self.grid_columnconfigure((0, 1), weight=1)

        self.checkboxFrame = CheckboxesEframes(self, valores=[1,2,3,4,5])
        self.checkboxFrame.grid(row=0, column=0, padx=10, pady=(10, 20), sticky="nsw")

        ctk.CTkButton(self, text='Botão chato', command=self.botao_Pressionado).grid(column=0, row=1, sticky='NEW', columnspan=2)


    def botao_Pressionado(self):
        print('Para de me cutucar!!')
        print(self.checkboxFrame.valores_dasCaixas())
        self.destroy()
        pass


# main
app = App()
app.mainloop()