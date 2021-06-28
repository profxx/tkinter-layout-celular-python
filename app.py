'''Esse app foi inspirado na serie Mo Dao Zu Shi, que também tem nome de The Untamed. Tem como foco umas das seitas desse mundo imáginario, e também o personagem principal: Lan Wangji,
tem muitas coisas que adicionei que giram em torno dele. É um app voltado para os fãs da série.

PyCharm 2018.3.7 (Community Edition)
Build #PC-183.6156.16, built on July 9, 2019
JRE: 1.8.0_152-release-1343-b28 x86
JVM: OpenJDK Server VM by JetBrains s.r.o
Windows 10 10.0'''
from tkinter import *
from anúncio import Anuncios
from perfil import Perf
from myperf import MyPerf
from perfWuxian import PerfilWu
from perfXi import Perfilxi
from myperf2 import Perfilusuario

class App:
    #cores
    cor_azul_esc = '#1d3557'
    cor_azul = '#00b4d8'
    cor_azul2 = '#48cae4'
    cor_azul_clar = '#caf0f8'
    cor_white = '#edf6f9'
    cor_fundo = '#b6e0f8'

    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        self.widgets_frame3()


        root.mainloop() # roda o class

    def tela(self):
        root.iconbitmap('cloud.ico')
        root.title('Gusulan')
        root.geometry('375x680+979+15')
        self.root.configure(bg=self.cor_fundo)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Frames ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def frames(self):
         self.frame1 = Frame(self.root, bg=self.cor_fundo)
         self.frame1.place(
             relx=0.0,
             rely=0.0,
             relwidth=1,
             relheight=0.99)

         self.frame2 = Frame(self.root, bg=self.cor_fundo)
         self.frame2.place(
             relx=0.0,
             rely=0.96,
             relwidth=1,
             relheight=0.99
         )
         self.frame3 = Frame(self.root, bg=self.cor_fundo)
         self.frame3.place(
             relx=0.0,
             rely=0.30,
             relwidth=1,
             relheight=0.20
         )

         self.frame4 = Frame(self.root, bg=self.cor_fundo)
         self.frame4.place(
             relx=0.0,
             rely=0.86,
             relwidth=1,
             relheight=0.10
        )

# 999999999999999999999999999 Imagem 999999999999999999999999999999999999999999999

    def widgets_frame1(self):
        self.modelo = PhotoImage(file='fundo.png')
        self.img1 = Label(
            self.frame1,
            image=self.modelo,
            bd=0
        )
        self.img1.place(
            relx=0.0,
            rely=0.0)
# -------------------- configuração dos botões ------------------------
    def widgets_frame2(self): # botam dos 3 mil regras
        self.btn_entrar = Button(
            self.frame2,#onde esta localizado
            text='3 mil regras', #texto do botão
            bg=self.cor_azul_esc,#cor do fundo
            activebackground=self.cor_azul_clar,#cor clicado
            font=('Please write me a song', 14, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul,
            command=self.clica_entrar
        )
        self.btn_entrar.place(
            relx=0,
            rely=0,
            relwidth=0.50,
            relheight=0.05
        )

        self.btn_perfil = Button( # botão do discípulos modelo
            self.frame2,
            text='Discípulo Modelo',
            bg=self.cor_azul_esc,
            activebackground=self.cor_azul_clar,
            font=('Please write me a song', 14, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul2,
            command=self.chama_entrar3
        )
        self.btn_perfil.place(
            relx=0.50,
            rely=0.0,
            relwidth=0.50,
            relheight=0.05
        )
        self.btn_myperfil = Button( # botão da sua conta
            self.frame4,#onde esta localizado
            text='Login do Cadastro', #texto do botão
            bg=self.cor_azul_esc,#cor do fundo
            activebackground=self.cor_azul_clar,#cor clicado
            font=('Please write me a song', 14, 'bold'),
            fg=self.cor_white,
            activeforeground=self.cor_azul,
            command=self.clica_entrar2
        )
        self.btn_myperfil.place(
            relx=0.25,
            rely=0.50,
            relwidth=0.50,
            relheight=0.50
        )

#+++++++++++++++++++ texto do centro da tela +++++++++++++++++++++++++++++
    def widgets_frame3(self):
        welcome = Label(
            self.frame3,
            text='Bem-vindo a Gusulan!',
            font=('Muthiara -Demo Version-', 23),
            bg=self.cor_fundo,
            fg='#000000')
        welcome.place(relx=0.0, rely=0.30, relwidth=1, relheight=0.50)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def clica_entrar(self): #comando btn
        self.hide()
        self.subFrame = Anuncios(self)
    def clica_entrar2(self):
        self.hide()
        self.subFrame = MyPerf(self)
    def chama_entrar3(self):
        self.hide()
        self.subFrame = Perf(self)
    def clica_entrar4(self):
        self.hide()
        self.subFrame = PerfilWu(self)
    def clica_entrar5(self):
        self.hide()
        self.subFrame = Perfilxi(self)
    def chama_entrar6(self):
        self.hide()
        self.subFrame = Perfilusuario(self)

    def hide(self): #esconde o root
        self.root.withdraw()
    def show(self):#Mostra o root novamente
        self.root.update()
        self.root.deiconify()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Programa Principal ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root = Tk()
App()
