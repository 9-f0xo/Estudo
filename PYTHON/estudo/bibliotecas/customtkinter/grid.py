import customtkinter as ctk

def botao_Pressionado():
    print('Para de me cutucar!!')
    app.destroy()

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Aplicação')
app.geometry('400x300')

# Isso faz com que toda a coluna 0 fique centralizada
# app.grid_columnconfigure(0, weight=1)

# Aqui foi adiciondo a coluna 0,1 para que as checkboxes ficassem igualmente espaçadas
app.grid_columnconfigure((0, 1), weight=1)

# Usando sticky nesse caso fará com que o botão se adapte a largura da tela
ctk.CTkButton(app, text='Botão chato', command=botao_Pressionado).grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

# pady recebe uma tupla, o que quer dizer 0 deslocamento para cima e 20px para baixo
checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1").grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = ctk.CTkCheckBox(app, text="checkbox 2").grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

app.mainloop()