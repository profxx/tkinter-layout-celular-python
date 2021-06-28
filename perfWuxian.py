from tkinter import *

class PerfilWu(Toplevel):
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
        self.title('Perfil Wuxian')
        self.configure(bg='#dbe2ec')
        self.iconbitmap('cloud.ico')

#**********  configuração do botão de voltar do perfil *********************
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

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Frames ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        self.frame = Frame(self, bg=self.cor_azul)
        self.frame.place(relx=0.05, rely=0.03, relwidth=0.36, relheight=0.19)

        self.frame2 = Frame(self, bg=self.cor_azul_clar)
        self.frame2.place(relx=0.43, rely=0.03, relwidth=0.52, relheight=0.19)

        self.frame3 = Frame(self, bg=self.cor_azul)
        self.frame3.place(relx=0.05, rely=0.23, relwidth=0.90, relheight=0.44)

        self.frame4 = Frame(self, bg=self.cor_azul_esc)
        self.frame4.place(relx=0.05, rely=0.70, relwidth=0.90, relheight=0.23)

#$$$$$$$$$$$$$$$$$$$$$$$$$$ Imagens $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.modelo = PhotoImage(file='wuxian.png')
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

#&&&&&&&&&&&&&&&&& Informações da imagem do wangji &&&&&&&&&&&&&&&&&

        self.nomeirm = Label(
            self.frame4,
            text='Namorado: Lan Wangji',
            font=('Consolas', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nomeirm.place(relx=0.04, rely=0.86)

#¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ Informações do Wei Wuxian que fica do lado da foto ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
        self.nome = Label(
            self.frame2,
            text='Nome de nascimento:\nWei Ying\nN. de cortesia:\nWei Wuxian\nTítulo: Patriarca Yiling\nClã:Wei\nSeita:YunmengJiang\nAniversário: 31/10',
            font=('Consolas', 10),
            bg=self.cor_azul_clar,
            fg='#000000',
        )
        self.nome.place(relx=0.03, rely=0.0)

#------------------------ texto abaixo da foto -------------------------------------------------------------------------
        self.nome = Label(
            self.frame3,
            text='Espada: Suibian (significa "tanto faz").\nOutras ferramentas: Uma flauta chamada\n"Chenqing"; Selo do Tigre Estígio.\nInfo. adicional: Filho de Wei ChangZe',
            font=('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.1, rely=0.0)

        self.nome = Label(
            self.frame3,
            text ='(ex-servo da seita Yunmengjiang) e CangSe San\n Ren (cultivadora desgarrada); perdeu os\n pais quando ainda era criança e foi adotado\n porJiang FengMian. Classificado em quarto\nlugar na lista dos cinco',
            font=('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.2)
        self.nome = Label(
            self.frame3,
            text ='melhores cultivadores de sua geração,\n ele eraoriginalmente amigo da infância\n dos irmãos Jiang e colega de classe de\n Lan Wangji, até que a tragédia atingiu\no clã jiang. ',
            font = ('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.1, rely=0.5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def onClose(self):
        self.destroy()