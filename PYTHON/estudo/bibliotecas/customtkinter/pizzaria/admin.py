import customtkinter as ctk
from tkinter import messagebox, simpledialog
import json
import os

CONFIG_FILE = "config.json"

def carregar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "tamanhos": ["Broto", "Pequena", "Média", "Grande", "Avestruz"],
        "valores_tamanhos": [2, 3, 4, 5, 6],
        "sabores": {
            "Perro Roni": 15, "Mozzarella": 12, "Lucas": 20,
            "Calabreso (Lá ele)": 18, "Luís": 17, "Yan": 16,
            "4 Queijos": 22, "Terracota Pie": 14, "Mokele Mbembe": 25, "Roblox": 30
        },
        "adicionais": {
            "Coca-Cola 2L": 10, "Pepsi 2L": 9, "Sprite 2L": 9, "Fanta Laranja 2L": 8,
            "Coca-Cola 1,5L": 9, "Pepsi 1,5L": 7.50, "Sprite 1,5L": 7.50, "Fanta Laranja 1,5L": 6.70
        }
    }

def salvar_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

class AdminWindow(ctk.CTkToplevel):
    def __init__(self, master, config):
        super().__init__(master)
        self.title("Administração")
        self.geometry("500x600")
        self.config_data = config

        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(fill="both", expand=True)

        self.tab_tamanhos = self.tabs.add("Tamanhos")
        self.tab_sabores = self.tabs.add("Sabores")
        self.tab_adicionais = self.tabs.add("Adicionais")

        self.setup_tamanhos()
        self.setup_sabores()
        self.setup_adicionais()

        self.btn_salvar = ctk.CTkButton(self, text="Salvar", command=self.salvar)
        self.btn_salvar.pack(pady=10)

    def setup_tamanhos(self):
        self.lista_tamanhos = ctk.CTkTextbox(self.tab_tamanhos, width=400, height=200)
        self.lista_tamanhos.pack(pady=10)
        self.atualizar_lista_tamanhos()
        
        btn_add = ctk.CTkButton(self.tab_tamanhos, text="Adicionar Tamanho", command=self.add_tamanho)
        btn_add.pack()

    def setup_sabores(self):
        self.lista_sabores = ctk.CTkTextbox(self.tab_sabores, width=400, height=200)
        self.lista_sabores.pack(pady=10)
        self.atualizar_lista_sabores()
        
        btn_add = ctk.CTkButton(self.tab_sabores, text="Adicionar Sabor", command=self.add_sabor)
        btn_add.pack()

    def setup_adicionais(self):
        self.lista_adicionais = ctk.CTkTextbox(self.tab_adicionais, width=400, height=200)
        self.lista_adicionais.pack(pady=10)
        self.atualizar_lista_adicionais()
        
        btn_add = ctk.CTkButton(self.tab_adicionais, text="Adicionar Adicional", command=self.add_adicional)
        btn_add.pack()

    def add_tamanho(self):
        novo = simpledialog.askstring("Novo Tamanho", "Digite o nome do novo tamanho:")
        if novo:
            limite_sabores = simpledialog.askinteger("Limite de Sabores", f"Digite o limite de sabores para {novo}:")
            if limite_sabores is not None:
                # Adiciona o novo tamanho ao dicionário de tamanhos
                self.config_data["tamanhos"][novo] = limite_sabores
                self.atualizar_lista_tamanhos()


    def add_sabor(self):
        novo = simpledialog.askstring("Novo Sabor", "Digite o nome do sabor:")
        preco = simpledialog.askfloat("Preço", f"Digite o preço do sabor {novo}:")
        if novo and preco:
            self.config_data["sabores"][novo] = preco
            self.atualizar_lista_sabores()

    def add_adicional(self):
        novo = simpledialog.askstring("Novo Adicional", "Digite o nome do adicional:")
        preco = simpledialog.askfloat("Preço", f"Digite o preço do adicional {novo}:")
        if novo and preco:
            self.config_data["adicionais"][novo] = preco
            self.atualizar_lista_adicionais()

    def atualizar_lista_tamanhos(self):
        self.lista_tamanhos.delete("1.0", "end")
        self.lista_tamanhos.insert("end", "\n".join(self.config_data["tamanhos"]))

    def atualizar_lista_sabores(self):
        self.lista_sabores.delete("1.0", "end")
        for sabor, preco in self.config_data["sabores"].items():
            self.lista_sabores.insert("end", f"{sabor}: R${preco}\n")

    def atualizar_lista_adicionais(self):
        self.lista_adicionais.delete("1.0", "end")
        for adicional, preco in self.config_data["adicionais"].items():
            self.lista_adicionais.insert("end", f"{adicional}: R${preco}\n")

    def salvar(self):
        global app
        salvar_config(self.config_data)
        messagebox.showinfo("Sucesso", "Configuração salva com sucesso!")
        self.destroy()
        app.destroy()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app.geometry("400x200")
    app.title("Painel Admin")

    config_data = carregar_config()
    
    def abrir_admin():
        app.withdraw()
        AdminWindow(app, config_data)
    
    btn_admin = ctk.CTkButton(app, text="Abrir Admin", command=abrir_admin)
    btn_admin.pack(pady=50)