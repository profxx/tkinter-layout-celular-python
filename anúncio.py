from tkinter import *

class Anuncios(Toplevel):
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
        self.title('3 mil regras')
        self.configure(bg=self.cor_fundo)
        self.iconbitmap('cloud.ico')

#**************configuração do botão de voltar************************************
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
            relx=0.80,
            rely=0.95,
            relwidth=0.20,
            relheight=0.05)

#--------------- Frames -----------------------------------------------------------

        self.frame = Frame(self, bg=self.cor_fundo) #Frame do enunciado
        self.frame.place(relx=0.05, rely=0, relwidth=0.90, relheight=0.07)

        self.frame1 = Frame(self, bg=self.cor_azul_esc) #Frames de cada regra
        self.frame1.place(relx=0.0, rely=0.06, relwidth=1, relheight=0.87)

        self.frame2 = Frame(self, bg=self.cor_azul_esc)
        self.frame2.place(relx=0.05, rely=0.14, relwidth=0.90, relheight=0.05)

        self.frame3 = Frame(self, bg=self.cor_azul_esc)
        self.frame3.place(relx=0.05, rely=0.21, relwidth=0.90, relheight=0.05)

        self.frame4 = Frame(self, bg=self.cor_azul_esc)
        self.frame4.place(relx=0.05, rely=0.28, relwidth=0.90, relheight=0.05)

        self.frame5 = Frame(self, bg=self.cor_azul_esc)
        self.frame5.place(relx=0.05, rely=0.35, relwidth=0.90, relheight=0.05)

        self.frame6 = Frame(self, bg=self.cor_azul_esc)
        self.frame6.place(relx=0.05, rely=0.42, relwidth=0.90, relheight=0.05)

        self.frame7 = Frame(self, bg=self.cor_azul_esc)
        self.frame7.place(relx=0.05, rely=0.49, relwidth=0.90, relheight=0.05)

        self.frame8 = Frame(self, bg=self.cor_azul_esc)
        self.frame8.place(relx=0.05, rely=0.56, relwidth=0.90, relheight=0.05)

        self.frame9 = Frame(self, bg=self.cor_azul_esc)
        self.frame9.place(relx=0.05, rely=0.63, relwidth=0.90, relheight=0.05)

        self.frame10 = Frame(self, bg=self.cor_azul_esc)
        self.frame10.place(relx=0.05, rely=0.70, relwidth=0.90, relheight=0.05)

        self.frame11 = Frame(self, bg=self.cor_azul_esc)
        self.frame11.place(relx=0.05, rely=0.77, relwidth=0.90, relheight=0.05)

        self.frame12 = Frame(self, bg=self.cor_azul_esc)
        self.frame12.place(relx=0.05, rely=0.84, relwidth=0.90, relheight=0.05)

        self.frame13 = Frame(self, bg=self.cor_azul_esc)
        self.frame13.place(relx=0.05, rely=0.91, relwidth=0.90, relheight=0.03)

# $$$$$$$$$$$$$$$$$$$$$$$$$$ Imagem $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.modelo = PhotoImage(file='fundo.png')
        self.img1 = Label(
            self.frame1,
            image=self.modelo,
            bd=0
        )
        self.img1.place(
            relx=0.0,
            rely=0.0)

#+++++++++++++++++++ texto do enunciado +++++++++++++++++++++++++++++++++++++++++++++++

        self.nome = Label(
            self.frame,
            text='     As 3 mil regras do paredão de pedra\n      da seita Gusulan',
            font=('Cooper Black', 12,),
            bg=self.cor_fundo,
            fg='#000000'
        )
        self.nome.place(relx=0.0, rely=0.0)

#++++++++++++++++++++ texto do enunciado e das regras em cada frame ++++++++++++++++++++

        self.nome = Label(
            self.frame2,
            text='Não mate no recanto das nuvens',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame3,
            text='Não lute sem permissão',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame4,
            text='Não mate no recanto das nuvens',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame5,
            text='Não cometa atos promíscuos',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame6,
            text='Não saia apos o toque de recolher',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame7,
            text='Não faça barulho',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame8,
            text='Não ande rápido',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame9,
            text='Não ria sem motivo',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame10,
            text='Não sente de forma desajeitada ',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame11,
            text='Não coma mais de 3 tigelas de comida',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame12,
            text='Seja um filho devoto',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

        self.nome = Label(
            self.frame13,
            text='Seja poderoso, e eles irão morrer por você',
            font=('KG Miss Kindy Marker', 10),
            bg=self.cor_azul_esc,
            fg=self.cor_white
        )
        self.nome.place(relx=0.0, rely=0.0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def onClose(self):
        self.destroy()
        self.frame_original.show()
