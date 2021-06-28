from tkinter import *

class Perfilusuario(Toplevel):
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
        self.geometry('375x680+979+15')
        self.title('Seu Perfil')
        self.configure(bg=self.cor_fundo)
        self.iconbitmap('cloud.ico')

        #configuração do botão de voltar do perfil
        self.btn = Button(
            self,
            text='Voltar',
            bg=self.cor_azul_esc,
            activebackground=self.cor_azul,
            font=('Please write me a song', 12, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul,
            command=self.onClose)

        self.btn.pack()
        self.btn.place(
            relx=0.0,
            rely=0.95,
            relwidth=0.20,
            relheight=0.05)

#222222222222222222  Frames  22222222222222222222222222222222222222222222222222222

        self.frame = Frame(self, bg=self.cor_azul)
        self.frame.place(relx=0.30, rely=0.03, relwidth=0.36, relheight=0.19)

        self.frame3 = Frame(self, bg=self.cor_fundo)
        self.frame3.place(relx=0.05, rely=0.23, relwidth=0.90, relheight=0.53)

        self.frame4 = Frame(self, bg=self.cor_azul_esc)
        self.frame4.place(relx=0.05, rely=0.60, relwidth=0.90, relheight=0.34)

#3333333333333333333 imagem 3333333333333333333333333333333333333333333333333333

        self.modelo = PhotoImage(file='usuario.png') # foto do suposto usuário
        self.img1 = Label(
            self.frame,
            image=self.modelo,
            bd=0
        )
        self.img1.place(
            relx=0.0,
            rely=0.0)

        self.modelo2 = PhotoImage(file='wanxian.png') # foto em baixo da tela
        self.img2 = Label(
            self.frame4,
            image=self.modelo2,
            bd=0
        )
        self.img2.place(
            relx=0.0,
            rely=0.0)

#777777777777777777 texto 777777777777777777777777777777777777777777777777
        self.text_log1 = Label(
            self.frame3,
            text= 'Seu nome:',
            font=('MV Boli', 10),
            bg='#f1f5f8',
            fg='#000000')
        self.text_log1.place(relx=0.10, rely=0.03)

        self.ent_log1 = Entry(#entrada para usuario escrever o nome
            self.frame3,
            font=('Arial', 11),
            fg='#000000')
        self.ent_log1.place(relx=0.10, rely=0.10, width=260, height=20)

        self.text_titulo = Label(
            self.frame3,
            text= 'Seu título:',
            font=('MV Boli', 10),
            bg='#f1f5f8',
            fg='#000000')
        self.text_titulo.place(relx=0.10, rely=0.17)

        self.ent_titulo = Entry(#entrada para usuario escrever  o título
            self.frame3,
            font=('Arial',11),
            fg='#000000')
        self.ent_titulo.place(relx=0.10, rely=0.24, width=260, height=20)

        self.text_aniver = Label(
            self.frame3,
            text= 'Seu aniversário:',
            font=('MV Boli', 10),
            bg='#f1f5f8',
            fg='#000000')
        self.text_aniver.place(relx=0.10, rely=0.31)

        self.ent_aniver = Entry(#entrada para usuario escrever a data do aniversário
            self.frame3,
            font=('Arial',11),
            fg='#000000')
        self.ent_aniver.place(relx=0.10, rely=0.38, width=260, height=20)

        self.text_nomeesp = Label(
            self.frame3,
            text= 'O nome da sua espada:',
            font=('MV Boli', 10),
            bg='#f1f5f8',
            fg='#000000')
        self.text_nomeesp.place(relx=0.10, rely=0.45)

        self.ent_nomeesp = Entry(#entrada para usuario escrever o nome da sua espada
            self.frame3,
            font=('Arial',11),
            fg='#000000')
        self.ent_nomeesp.place(relx=0.10, rely=0.52, width=260, height=20)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def onClose(self):
        self.destroy()

    def chama_entrar6(self):
        self.subFrame = Perfilusuario(self)
