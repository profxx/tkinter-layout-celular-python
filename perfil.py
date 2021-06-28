from tkinter import *
from perfWuxian import PerfilWu
from perfXi import Perfilxi

class Perf(Toplevel):
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
        self.title('Perfil')
        self.configure(bg='#dbe2ec')
        self.iconbitmap('cloud.ico')

        #configuração do botão de voltar do perfil
        self.btn = Button(
            self,
            text='Voltar',
            bg=self.cor_azul_esc,
            activebackground=self.cor_azul,
            font=('Please write me a song', 14, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul,
            command=self.onClose)

#555555555555555555555 Botão 5555555555555555555555

        self.btn.pack()
        self.btn.place(
            relx=0.0,
            rely=0.95,
            relwidth=0.20,
            relheight=0.05)

        self.btn = Button(
            self,
            text='Wei Wuxian',
            bg=self.cor_azul,
            activebackground=self.cor_azul,
            font=('Please write me a song', 12, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul,
            command=self.clica_entrar4)

        self.btn.pack()
        self.btn.place(
            relx=0.80,
            rely=0.95,
            relwidth=0.20,
            relheight=0.05)

        self.btn = Button(
            self,
            text='Lan Xichen',
            bg=self.cor_azul,
            activebackground=self.cor_azul,
            font=('Please write me a song', 12, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul,
            command=self.clica_entrar5)

        self.btn.pack()
        self.btn.place(
            relx=0.60,
            rely=0.95,
            relwidth=0.20,
            relheight=0.05)

#88888888888888888888888 Frames 888888888888888888888888888888888888888888888888

        self.frame = Frame(self, bg=self.cor_azul)
        self.frame.place(relx=0.05, rely=0.03, relwidth=0.36, relheight=0.19)

        self.frame2 = Frame(self, bg=self.cor_azul_clar)
        self.frame2.place(relx=0.43, rely=0.03, relwidth=0.52, relheight=0.19)

        self.frame3 = Frame(self, bg=self.cor_azul)
        self.frame3.place(relx=0.05, rely=0.23, relwidth=0.90, relheight=0.46)

        self.frame4 = Frame(self, bg=self.cor_azul_esc)
        self.frame4.place(relx=0.05, rely=0.70, relwidth=0.90, relheight=0.23)

#999999999999999999999999999 Imagem 999999999999999999999999999999999999999999999

        self.modelo = PhotoImage(file='wangji.png')
        self.img1 = Label(
            self.frame,
            image=self.modelo,
            bd=0
        )
        self.img1.place(
            relx=0.0,
            rely=0.0)

        self.modelo2 = PhotoImage(file='xichen.png')
        self.img2 = Label(
            self.frame4,
            image=self.modelo2,
            bd=0
        )
        self.img2.place(
            relx=0.05,
            rely=0.0)

        self.modelo3 = PhotoImage(file='wuxian.png')
        self.img3 = Label(
            self.frame4,
            image=self.modelo3,
            bd=0
        )
        self.img3.place(
            relx=0.5,
            rely=0.0)

#6666666666666666666666666666666 informacões da imagem 66666666666666666666666666666666666666666666666666666666666666666

        self.nomeirm = Label(
            self.frame4,
            text='Irmão: Lan Xichen',
            font=('Consolas', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nomeirm.place(relx=0.08, rely=0.86)

        self.nomenam = Label(
            self.frame4,
            text='Namorado: Wei Wuxian',
            font=('Consolas', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nomenam.place(relx=0.50, rely=0.86)

#9999999999999999999999999999999 Informações do Lan Wangji que fica do lado da foto 999999999999999999999999999999999999

        self.nome = Label(
            self.frame2,
            text='Nome de nascimento:\nLan Zhan\nN. de cortesia:\nLan Wangji\nTítulo: HanGuang-Jun\nClã: Lan\nSeita: Gusulan\nAniversário: 23/01',
            font=('Consolas', 10),
            bg=self.cor_azul_clar,
            fg='#000000',
        )
        self.nome.place(relx=0.1, rely=0.0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~ texto abaixo da foto ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.nome = Label(
            self.frame3,
            text='Espada: Bichen (significa "evitar a poeira/\nassuntos mundanos").\nOutras ferramentas: Uma guqin chamada "Wangji".\n• Info. adicional: Como Segundo Jovem Mestre\n da familia Lan, possui a excelente \nreputação dheroico cultivador por "estar aonde\n quer que o caos esteja".',
            font=('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame3,
            text ='Classificado em segundo lugar na lista\n dos cinco melhores cultivadores de sua\n geração, nem mesmo os olhares complacentes\n poderiam evitar que sua amarga expressão\n facial o faça parecer',
            font=('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.4)
        self.nome = Label(
            self.frame3,
            text ='como se tivesse acabado de perder sua esposa.\nJuntamente com seu irmão mais velho, Lan Xichen,\nsão chamados de "As Duas Jades de Lan".',
            font = ('Consolas', 10),
            bg=self.cor_azul,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.7)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def onClose(self):
        self.destroy()
        self.frame_original.show()
    def clica_entrar4(self):
        self.subFrame = PerfilWu(self)
    def clica_entrar5(self):
        self.subFrame = Perfilxi(self)
