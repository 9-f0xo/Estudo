from customtkinter import *  # Biblioteca tkinter melhorada
import tkinter as tk
from tkinter import messagebox
from menu import App
from admin import AdminWindow, carregar_config

# Variáveis globais para verificar o login do usuário
logado = False 
usuario_logado = None  # Variável para armazenar o usuário logado

# Lista global para armazenar os usuários cadastrados
donos = [{'usuario': 'Yan', 'senha': 'Rem.py3'}, {'usuario': 'Micael Rei Delas 2014', 'senha': 'ReiDelas.Exquecii'},
            {'usuario': 'Luis_Antonella loves marry christmas', 'senha': 'Amor_Da_Antonella'}]

vips = [{'usuario': 'Mona China Maite', 'senha': 'La Cucaracha la cucaracha...'}, {'usuario': 'Jamilly Cullen', 'senha': 'gig cullen'},
        {'usuario': 'Raquel', 'senha': 'gig cullen'}]

usuarios = []  # Lista para armazenar os usuários registrados pelo sistema

lista_negra = [{'usuario': 'Ruan Perro delas', 'senha': 'vou roubar a mochila dela'}]  # Lista de usuários bloqueados

class Menu:
    def __init__(self):
        self.app_menu = CTk()  
        self.app_menu.geometry('500x400')
        self.tema_atual = StringVar(value="dark")
        set_appearance_mode(self.tema_atual.get())
        self.criar_interface()

    def criar_interface(self):
        """Função para criar todos os componentes da interface"""

        self.janelinha = CTkFrame(master=self.app_menu, width=500, height=300, border_width=1)
        self.janelinha.place(relx=0.5, rely=0.02, anchor='n')

        self.botao_tema = CTkSwitch(
            master=self.janelinha, 
            text="Modo Escuro", 
            command=self.alternar_tema,
            variable=self.tema_atual, 
            onvalue="dark", 
            offvalue="light",
            fg_color='#3E3E3E', 
            border_width=0
        )
        self.botao_tema.place(relx=0.01, rely=0.06, anchor='w')

        self.nome = CTkLabel(
            master=self.janelinha, 
            text='Mokele Mbembe\nPizzas', 
            font=('Baskerville', 20), 
            text_color='#FFFFFF'
        )
        self.nome.place(relx=0.5, rely=0.01, anchor='n')

        if not logado:
            self.botao_login = CTkButton(
                master=self.janelinha, 
                text="Login", 
                command=self.entrar, 
                width=15, 
                height=10, 
                corner_radius=75
            )
            self.botao_login.place(relx=0.9, rely=0.10)
        else:
            self.msg_logado = CTkLabel(master=self.janelinha, text=f'Logado como {usuario_logado}')
            self.msg_logado.place(relx=0.5, rely=0.10, anchor='n')

            # Verifica se o usuário logado é um dono e exibe o botão do admin
            if usuario_logado in [dono['usuario'] for dono in donos]:
                self.botao_admin = CTkButton(
                    master=self.janelinha, 
                    text="Painel do Admin", 
                    command=self.abrir_admin,  # Função que abre o painel de admin
                    width=30, 
                    height=20, 
                    corner_radius=75
                )
                self.botao_admin.place(relx=0.5, rely=0.7, anchor='n')

            self.botao_login = CTkButton(
                master=self.janelinha, 
                text="Ir para o Pedido",  
                command=self.ir_para_pedido, 
                width=30, 
                height=20, 
                corner_radius=75
            )
            self.botao_login.place(relx=0.5, rely=0.5, anchor='n')

    def alternar_tema(self):
        """Alterna entre o modo claro e escuro"""
        set_appearance_mode(self.tema_atual.get())
        
        if self.tema_atual.get() == 'dark':
            self.nome.configure(text_color='#FFFFFF')
        else:
            self.nome.configure(text_color="#000000")

    def entrar(self):
        """Função chamada ao clicar no botão de login"""
        login = Login()
        self.app_menu.destroy()  # Fecha o menu principal
        login.exibir_login()  # Exibe a janela de login

    def ir_para_pedido(self):
        """Função para ir para a tela de pedido após login"""
        pedido = App()  # Instancia o aplicativo de pedido
        self.app_menu.destroy()  # Fecha a tela do menu
        pedido.mainloop()  # Exibe a tela de pedido

    def abrir_admin(self):
        """Função para abrir o painel de administração"""
        config_data = carregar_config()  # Carrega a configuração do painel de admin
        admin_window = AdminWindow(self.app_menu, config_data)
        admin_window.grab_set()  # Garante que a janela de admin será modal (bloqueia o acesso à janela principal)
        
    def exibir_menu(self):
        """Exibe a janela principal"""
        self.app_menu.mainloop()

    def Sair(self):
        global logado, usuario_logado
        usuario_logado = ""
        logado = False
        self.app_menu.quit()
        self.app_menu.destroy()
        login = Login()
        login.exibir_login()



class Login:
    def __init__(self):
        self.login_janela = CTk()  # Janela de login
        self.login_janela.geometry('400x300')  # Tamanho da janela
        self.criar_interface()  # Criação da interface

    def criar_interface(self):
        """Função para criar a interface do login"""

        # Texto de boas-vindas
        frase_login = CTkLabel(master=self.login_janela, text='Logue e compre as\nmelhores pizzas!!', font=('arial', 30))
        frase_login.place(relx=0.5, rely=0.2, anchor='n')

        # Campo de texto para o nome de usuário
        self.usuario_entry = CTkEntry(master=self.login_janela, placeholder_text="Usuário")
        self.usuario_entry.place(relx=0.5, rely=0.5, anchor='n')

        # Campo de texto para a senha
        self.senha_entry = CTkEntry(master=self.login_janela, placeholder_text="Senha", show="*")
        self.senha_entry.place(relx=0.5, rely=0.6, anchor='n')

        # Botão de login que chama a função realizar_login
        self.botao_entrar = CTkButton(master=self.login_janela,
            text="Entrar",
            command=self.retornar_menu
        )
        self.botao_entrar.place(relx=0.5, rely=0.7, anchor='n')

        # Botão para registrar-se, que chama a função abrir_registro
        self.botao_registrar = CTkButton(
            master=self.login_janela,
            text="Registrar-se",
            command=self.abrir_registro,
            width=15,
            height=10,
            corner_radius=75
        )
        self.botao_registrar.place(relx=0.9, rely=0.02, anchor='n')

        self.botao_voltar = CTkButton(
            master=self.login_janela,
            text='Voltar',
            command=self.Voltar,
            width=10,
            height=7,
            corner_radius=75
        )
        self.botao_voltar.place(relx=0.05, rely=0.02, anchor='n')

    def realizar_login(self):
        """Função para realizar o login"""
        
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        # Agora usamos `global` para modificar as variáveis globais
        global logado, usuario_logado

        # Verifica se o login é bem-sucedido
        for dono in donos:
            if usuario == dono['usuario'] and dono['senha'] == senha:
                messagebox.showinfo('Bem-Vindo de volta', f'Olá, Bem vindo novamente {usuario}')
                logado = True
                usuario_logado = usuario
                return True
        for vip in vips:
            if usuario == vip['usuario'] and vip['senha'] == senha:
                messagebox.showinfo("Bem-Vinda Parceira", f'Bem-Vinda novamente {usuario}')
                logado = True
                usuario_logado = usuario
                return True
        for u in usuarios:
            if usuario == u['usuario'] and u['senha'] == senha:
                messagebox.showinfo('Olá', f'Seja Bem-vindo a pizzaria Mokele Y Bmembe {usuario}')
                logado = True
                usuario_logado = usuario
                return True
        messagebox.showerror('Login Incorreto','O Login que esta tentando digitar esta incorreto, Tente novamente!')
        return False

    def exibir_login(self): 
        """Exibe a janela de login"""
        self.login_janela.mainloop()

    def abrir_registro(self):
        """Abre a tela de registro"""
        registrar = Registro()
        self.login_janela.destroy()  # Fecha a janela de login
        registrar.exibir_registro()  # Exibe a janela de registro

    def retornar_menu(self):
        if self.realizar_login():
            self.login_janela.destroy()
            menu = Menu()
            menu.exibir_menu()

    def Voltar(self):
        self.login_janela.destroy()
        menu = Menu()
        menu.exibir_menu()


class Registro:
    def __init__(self):
        self.janela_registro = CTk()
        self.janela_registro.geometry('400x300')  # Tamanho da janela
        self.criar_interface()

    def criar_interface(self):
        """Função para criar a interface de registro"""
        
        frase_registro = CTkLabel(master=self.janela_registro, text='Torne-se um Mokele\nMbembe agora!', font=('arial', 30))
        frase_registro.place(relx=0.5, rely=0.2, anchor='n')

        self.usuario = CTkEntry(master=self.janela_registro, placeholder_text='Usuário')
        self.usuario.place(relx=0.5, rely=0.5, anchor='n')

        self.senha = CTkEntry(master=self.janela_registro, placeholder_text='Senha', show='*')
        self.senha.place(relx=0.5, rely=0.6, anchor='n')

        self.Botao_registro = CTkButton(master=self.janela_registro, text='Registrar-se', command=self.retornar_login)
        self.Botao_registro.place(relx=0.5, rely=0.7, anchor='n')

        self.botao_voltar = CTkButton(
            master=self.janela_registro,
            text='Voltar',
            command=self.Voltar,
            width=10,
            height=7,
            corner_radius=75
        )
        self.botao_voltar.place(relx=0.05, rely=0.02, anchor='n')


    def exibir_registro(self):
        """Exibe a janela de registro"""
        self.janela_registro.mainloop()

    def verificar_registro(self):
        """Verifica as condições para o registro"""

        for dono in donos:
            if self.usuario.get() == dono['usuario']:
                messagebox.showerror('Erro', 'Usuário já registrado, por favor utilize outro')
                return False
        for vip in vips:
            if self.usuario.get() == vip['usuario']:
                messagebox.showerror('Erro', 'Usuário já registrado, por favor utilize outro')
                return False
        for n in lista_negra:
            if self.usuario.get() == n['usuario']:
                messagebox.showerror('Erro', 'Usuário está na lista negra')
                return False
        for u in usuarios:
            if self.usuario.get() == u['usuario']:
                messagebox.showerror('Erro', 'Usuário já registrado, por favor utilize outro')
                return False
            
        if len(self.senha.get()) < 6:
            messagebox.showerror('Erro', 'Sua senha deve conter 6 ou mais caracteres!')
            return False

        messagebox.showinfo('Cadastrado', 'Obrigado por se tornar um Mokele Mbembe')
        usuarios.append({'usuario': self.usuario.get(), 'senha': self.senha.get()})
        return True

    def retornar_login(self):
        """Retorna para a tela de login se o registro for bem-sucedido"""
        if self.verificar_registro():
            self.janela_registro.destroy()  # Fecha a janela de registro
            login = Login()  # Cria a janela de login
            login.exibir_login()  # Exibe a janela de login

    def Voltar(self):
        self.janela_registro.destroy()
        login = Login()
        login.exibir_login()

class Frame_saborzito(App):
    
    def __init__(self):
        super().__init__()



# Instancia e inicia o programa
menu = Menu()  # Cria a janela do menu principal
menu.exibir_menu()  # Exibe a janela do menu