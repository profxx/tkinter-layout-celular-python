from tkinter import *

class Perfilxi(Toplevel):
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
        self.title('Perfil Xichen')
        self.configure(bg='#dbe2ec')
        self.iconbitmap('cloud.ico')

# **********  configuração do botão de voltar do perfil *********************
        self.btn = Button(
            self,
            text='Voltar',
            bg=self.cor_azul_esc,
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

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Frames ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        self.frame = Frame(self, bg=self.cor_azul)
        self.frame.place(relx=0.05, rely=0.03, relwidth=0.36, relheight=0.19)

        self.frame2 = Frame(self, bg=self.cor_azul_clar)
        self.frame2.place(relx=0.43, rely=0.03, relwidth=0.52, relheight=0.19)

        self.frame3 = Frame(self, bg=self.cor_azul)
        self.frame3.place(relx=0.05, rely=0.23, relwidth=0.90, relheight=0.44)

        self.frame4 = Frame(self, bg=self.cor_azul_esc)
        self.frame4.place(relx=0.05, rely=0.70, relwidth=0.90, relheight=0.23)

# $$$$$$$$$$$$$$$$$$$$$$$$$$ Imagens $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.modelo = PhotoImage(file='xichen.png')
        self.img1 = Label(
            self.frame,
            image=self.modelo,
            bd=0
        )
        self.img1.place(
            relx=0.0,
            rely=0.0)

        self.modelo2 = PhotoImage(file='wangji.png')
        self.img2 = Label(
            self.frame4,
            image=self.modelo2,
            bd=0
        )
        self.img2.place(
            relx=0.05,
            rely=0.0)

# &&&&&&&&&&&&&&&&& Informações da imagem do wangji &&&&&&&&&&&&&&&&&

        self.nomeirm = Label(
            self.frame4,
            text='Irmão: Lan Wangji',
            font=('Consolas', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nomeirm.place(relx=0.08, rely=0.86)

# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ Informações do Lan Xiche que fica do lado da foto ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

        self.nome = Label(
            self.frame2,
            text='Nome de nascimento:\nLan Huan\nN. de cortesia:\nLan Xichen\nTítulo: ZeWu-Jun\nClã:Lan\nSeita:Gusulan\nAniversário: 08/10',
            font=('Consolas', 10),
            bg=self.cor_azul_clar,
            fg='#000000',
        )
        self.nome.place(relx=0.1, rely=0.0)

# ------------------------ texto abaixo da foto -------------------------------------------------------------------------

        self.nome = Label(
            self.frame3,
            text='Espada: Shuoyue.\n•Outras ferramentas: Uma xiao (flauta) de\njade branca chamada "Liebing".\nAtual líder da seita Gusulan,\n é um homem caloroso e refinado,\n sincero e gentil.',
            font=('Consolas', 11),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame3,
            text ='Fez um juramento de irmandade com Nie MingJue\n e Jin GuangYao.\nCuriosidades:\n• Foi classificado em primeiro lugar na lista\ndoscinco melhores cultivadores de sua geração,\nsendo também considerado o mais bonito.',
            font=('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.4)
        self.nome = Label(
            self.frame3,
            text ='• É a pessoa que melhor conhece Wangi, sendo o\núnico capaz de ler/interpretar seu irmão e o\nprimeiro a notar os sentimentos dele por WuXian.',
            font = ('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0, rely=0.7)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def onClose(self):
        self.destroy()