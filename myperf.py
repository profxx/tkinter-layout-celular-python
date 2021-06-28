from tkinter import *
from myperf2 import Perfilusuario

class MyPerf(Toplevel):
    #cores
    cor_azul_esc = '#1d3557'
    cor_azul = '#00b4d8'
    cor_azul2 = '#48cae4'
    cor_azul_clar = '#caf0f8'
    cor_white = '#edf6f9'
    cor_fundo = '#b6e0f8'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self)
        self.title('Entrar em sua conta ou cadastrar')
        self.geometry('375x680+979+15')
        self.iconbitmap('cloud.ico')

#^^^^^^^^^^^^^^^^^^^^ frames ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        self.frame1 = Frame(self, bg='#f1f5f8')
        self.frame1.place(x=0, y=0, relwidth=1.0, relheight=136)
        self.frame2 = Frame(self, bg='#FFC8DD')
        self.frame2.place(x=0, rely=0.2, relwidth=1.0, relheight=0.9)


#44444444444444444444  imagem de fundo  444444444444444444444444444444


        self.modelo = PhotoImage(file='fundo2.png')
        self.img1 = Label(
            self.frame2,
            image=self.modelo,
            bd=0
        )
        self.img1.place(
            relx=0.0,
            rely=0.0)

#5555555555555555555555 Botão 555555555555555555555555555555

        self.btn = Button(
            self,
            text='Voltar',# botão do canto esquerdo da tela
            bg='#878063',
            activebackground=self.cor_azul,
            font=('Please write me a song', 14, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul,
            command=self.onClose)

        self.btn.pack()
        self.btn.place(
            relx=0.0,
            rely=0.95,
            relwidth=0.20,
            relheight=0.05)

        self.btn = Button(
            self,
            text='Pronto',
            bg="#dbe2ec",
            activebackground=self.cor_azul,
            font=('Please write me a song', 12, 'bold'),
            fg='#1c5f75',
            activeforeground=self.cor_azul,
            command=self.chama_entrar6)

        self.btn.pack()
        self.btn.place(
            relx=0.80,
            rely=0.43,
            relwidth=0.15,
            relheight=0.03)

        self.btn = Button(
            self,
            text='Pronto',#texto do botão
            bg="#dbe2ec",#cor do fundo
            activebackground=self.cor_azul,
            font=('Please write me a song', 12, 'bold'),#fonte, tamanho, negrito
            fg='#1c5f75',#cor da fonte
            activeforeground=self.cor_azul,
            command=self.chama_entrar6)#comando do botão

        self.btn.pack()
        self.btn.place(
            relx=0.80,
            rely=0.74,
            relwidth=0.15,
            relheight=0.03)


                            #Widget
#333333333333333333333333333333333333333333333333333333333333333333333333333333333
        self.welcome = Label(
            self.frame1,#onde está localizado
            text= 'Faça Login ou Cadastra-se',#texto de info
            font=('Muthiara -Demo Version-', 20),
            bg= '#f1f5f8',
            fg= '#000000')
        self.welcome.pack(padx=0, pady=40)#desloca o texto para o lugar desejado
#333333333333333333333333333333333333333333333333333333333333333333333333333333333

        self.text_log1 = Label(#login
            self.frame2,# onde está localizado
            text= 'Email',
            font=('MV Boli', 13),
            bg='#f1f5f8',
            fg='#000000')
        self.text_log1.place(relx=0.15, rely=0.05)

        self.ent_log1 = Entry(#entrada para usuario escrever para login
            self.frame2,
            font=('Arial', 11),
            fg='#000000')
        self.ent_log1.place(relx=0.15, rely=0.10, width=250, height=25)

        self.text_senha = Label(
            self.frame2,
            text= 'Senha',
            font=('MV Boli', 13),
            bg='#f1f5f8',
            fg='#000000')
        self.text_senha.place(relx=0.15, rely=0.15)

#2222222222222222222222222222222222222222222222222222222222222222222222222222222
        self.ent_senha = Entry(#entrada para usuario escrever para login
            self.frame2,
            font=('Arial',11),
            fg='#000000')
        self.ent_senha.place(relx=0.15, rely=0.20, width=250, height=25)
#2222222222222222222222222222222222222222222222222222222222222222222222222222222

        self.text_log1 = Label( #2° opção para o usuário
            self.frame2,
            text='ou cadastrar',
            font=('MV Boli', 13),
            bg='#dbe2ec',
            fg='#000000')
        self.text_log1.place(relx=0.15, rely=0.25)

        self.text_log1 = Label(#cadastrar
            self.frame2,
            text= 'Email',
            font=('MV Boli', 13),
            bg='#dbe2ec',
            fg='#000000')
        self.text_log1.place(relx=0.15, rely=0.30)

        self.ent_log1 = Entry(#entrada para usuario escrever para cadastro
            self.frame2,
            font=('Arial', 11),
            fg='#000000')
        self.ent_log1.place(relx=0.15, rely=0.35, width=250, height=25)

        self.text_senha = Label(
            self.frame2,
            text= 'Senha',
            font=('MV Boli', 13),
            bg='#dbe2ec',
            fg='#000000')
        self.text_senha.place(relx=0.15, rely=0.40)

        self.ent_senha = Entry(#entrada para usuario escrever para cadastro
            self.frame2,
            font=('Arial',11),
            fg='#000000')
        self.ent_senha.place(relx=0.15, rely=0.45, width=250, height=25)

        self.text_idade = Label(
            self.frame2,
            text='Idade',
            font=('MV Boli', 13),
            bg='#dbe2ec',
            fg='#000000')
        self.text_idade.place(relx=0.15, rely=0.50)

        self.ent_idade = Entry(#entrada para usuario escrever para cadastro
            self.frame2,
            font=('Arial', 11),
            fg='#000000')
        self.ent_idade.place(relx=0.15, rely=0.55, width=250, height=25)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def onClose(self):
        self.destroy()
        self.frame_original.show()
    def chama_entrar6(self):
        self.subFrame = Perfilusuario(self)