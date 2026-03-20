import tkinter
from tkinter import *
from tkinter import ttk

# cores
cor0 = "#FFFFFF"  # branco
cor1 = "#1C1C1C"  # cinza escuro
cor2 = "#836FFF"  # Slate Blue
cor3 = "#38576b"  # valor / value
cor4 = "#3297a8"  # azul / blue
cor5 = "#B0C4DE"  # Azul Ferro
cor6 = "#20B2AA"  # Azul Marinho Claro
cor7 = "#fff873"  # amarela / yellow
cor8 = "#DDA0DD"  # Rosinha
cor9 = "#FF1493"  # Dark Pink
cor10 = "#fcfbf7" # branco
cor11 = "#4B0082" # Indigo
fundo = "#8A2BE2" # BlueViolet

# Criando janela principal
janela = Tk()
janela.title('Jogo Da Velha')
janela.geometry('260x370')
janela.configure(bg=fundo)

# dividindo a janela em 2 frames
frame_cima = Frame(janela, width=240, height=100, bg=cor11, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

# Configurando Frame Superior

# Jogador 1
app_x = Label(
    frame_cima,
    text='X',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 40 italic bold'),
    bg=cor11, fg=cor4)
app_x.place(x=25, y=10)

app_x_nome = Label(
    frame_cima,
    text='Jogador 1',
    height=1, relief='flat',
    anchor='center',
    font=('Ivy 8 italic'),
    bg=cor11, fg=cor0)
app_x_nome.place(x=22, y=63)

app_x_pontos = Label(
    frame_cima,
    text='0',
    height=1, relief='flat',
    anchor='center',
    font=('Ivy 27 italic bold'),
    bg=cor11, fg=cor0)
app_x_pontos.place(x=80, y=20)

# separador
app_separador = Label(
    frame_cima,
    text=':',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 27 italic bold'),
    bg=cor11, fg=cor0)
app_separador.place(x=115, y=18)

# Jogador 2
app_o = Label(
    frame_cima,
    text='O',
    height=1,
    relief='flat',
    anchor='center',
    font=('Ivy 40 italic bold'),
    bg=cor11, fg=cor9)
app_o.place(x=170, y=10)

app_o_nome = Label(
    frame_cima,
    text='Jogador 2',
    height=1, relief='flat',
    anchor='center',
    font=('Ivy 8 italic'),
    bg=cor11, fg=cor0)
app_o_nome.place(x=165, y=63)

app_o_pontos = Label(
    frame_cima,
    text='0',
    height=1, relief='flat',
    anchor='center',
    font=('Ivy 27 italic bold'),
    bg=cor11, fg=cor0)
app_o_pontos.place(x=140, y=20)

# Lógica
jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

jogando = 'X'
joga = ''
contador = 0
contador_de_rodada = 0


def iniciar_jogo():
    global tabela, contador, jogando

    tabela = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    contador = 0
    jogando = 'X'

    # impedir criar botão/tabuleiro duplicado
    try:
        b_jogar.destroy()
    except:
        pass

    # Controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global joga
        global cor

        jogador_atual = jogando

        if i == str(1):
            if b_0['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_0['fg'] = cor
                b_0['text'] = jogador_atual
                tabela[0][0] = jogador_atual
                contador += 1

        if i == str(2):
            if b_1['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_1['fg'] = cor
                b_1['text'] = jogador_atual
                tabela[0][1] = jogador_atual
                contador += 1

        if i == str(3):
            if b_2['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_2['fg'] = cor
                b_2['text'] = jogador_atual
                tabela[0][2] = jogador_atual
                contador += 1

        if i == str(4):
            if b_3['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_3['fg'] = cor
                b_3['text'] = jogador_atual
                tabela[1][0] = jogador_atual
                contador += 1

        if i == str(5):
            if b_4['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_4['fg'] = cor
                b_4['text'] = jogador_atual
                tabela[1][1] = jogador_atual
                contador += 1

        if i == str(6):
            if b_5['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_5['fg'] = cor
                b_5['text'] = jogador_atual
                tabela[1][2] = jogador_atual
                contador += 1

        if i == str(7):
            if b_6['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_6['fg'] = cor
                b_6['text'] = jogador_atual
                tabela[2][0] = jogador_atual
                contador += 1

        if i == str(8):
            if b_7['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_7['fg'] = cor
                b_7['text'] = jogador_atual
                tabela[2][1] = jogador_atual
                contador += 1

        if i == str(9):
            if b_8['text'] == '':
                cor = cor4 if jogador_atual == 'X' else cor9
                b_8['fg'] = cor
                b_8['text'] = jogador_atual
                tabela[2][2] = jogador_atual
                contador += 1

        # verifica vitória
        if contador >= 5:
            # linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2] != '':
                vencedor(jogador_atual)
                return
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != '':
                vencedor(jogador_atual)
                return
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != '':
                vencedor(jogador_atual)
                return

            # colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0] != '':
                vencedor(jogador_atual)
                return
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != '':
                vencedor(jogador_atual)
                return
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != '':
                vencedor(jogador_atual)
                return

            # diagonais
            if tabela[0][0] == tabela[1][1] == tabela[2][2] != '':
                vencedor(jogador_atual)
                return
            elif tabela[0][2] == tabela[1][1] == tabela[2][0] != '':
                vencedor(jogador_atual)
                return

        # empate
        if contador >= 9:
            vencedor('EMPATE!')
            return

        # troca o turno só depois de tudo
        if jogador_atual == 'X':
            jogando = 'O'
            joga = 'Jogador 2'
        else:
            jogando = 'X'
            joga = 'Jogador 1'

    # definir o ganhador
    def vencedor(i):
        global score_1
        global score_2
        global tabela
        global contador_de_rodada
        global contador
        global jogando

        # desabilitando os botões
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_vencedor = Label(
            frame_baixo, text='', width=18,
            relief='flat',
            anchor='center',
            font=('Ivy 13 italic bold'),
            bg=cor7, fg=cor9)
        app_vencedor.place(x=35, y=194)

        if i == 'X':
            score_1 += 1
            app_vencedor['text'] = 'Jogador 1 VENCEU!'
            app_x_pontos['text'] = score_1

        if i == 'O':
            score_2 += 1
            app_vencedor['text'] = 'Jogador 2 VENCEU!'
            app_o_pontos['text'] = score_2

        if i == 'EMPATE!':
            app_vencedor['text'] = 'EMPATE!'

        def start():
            global tabela, contador, jogando

            # limpando os botões
            b_0['text'] = ''
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''

            b_0['state'] = 'normal'
            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'

            tabela = [
                ['', '', ''],
                ['', '', ''],
                ['', '', '']
            ]
            contador = 0
            jogando = 'X'

            app_vencedor.destroy()
            b_jogar_proxima.destroy()

        # botão próxima rodada
        b_jogar_proxima = Button(
            frame_baixo,
            command=start,
            text='PRÓXIMA',
            width=10,
            font=('Ivy 10 bold italic'),
            overrelief=RIDGE,
            relief='raise',
            bg=fundo, fg=cor0)
        b_jogar_proxima.place(x=84, y=220)

        def GameOver():
            b_jogar_proxima.destroy()
            app_vencedor.destroy()
            encerrar()

        if contador_de_rodada >= 5:
            GameOver()
        else:
            contador_de_rodada += 1
            tabela = [
                ['', '', ''],
                ['', '', ''],
                ['', '', '']
            ]
            contador = 0

    # encerrar o jogo
    def encerrar():
        global tabela
        global contador
        global contador_de_rodada
        global score_1
        global score_2
        global jogando

        tabela = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        contador = 0
        contador_de_rodada = 0
        score_1 = 0
        score_2 = 0
        jogando = 'X'

        # desabilitando os botões
        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_GameOver = Label(
            frame_baixo, text='FIM DE JOGO', width=18,
            relief='flat',
            anchor='center',
            font=('Ivy 13 italic bold'),
            bg=cor7, fg=cor9)
        app_GameOver.place(x=35, y=50)

        # jogar novamente
        def jogar_novamente():
            app_x_pontos['text'] = 0
            app_o_pontos['text'] = 0
            app_GameOver.destroy()
            b_jogar_fim.destroy()

            # limpa tabuleiro
            b_0['text'] = ''
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''

            b_0['state'] = 'normal'
            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'

        # botão jogar novamente
        b_jogar_fim = Button(
            frame_baixo,
            command=jogar_novamente,
            text='JOGAR',
            width=10,
            font=('Ivy 10 bold italic'),
            overrelief=RIDGE,
            relief='raise',
            bg=fundo, fg=cor0)
        b_jogar_fim.place(x=84, y=220)

    # linhas verticais
    app_linha1 = Label(
        frame_baixo,
        text='',
        height=24, relief='flat',
        pady=5,
        anchor='center',
        font=('Ivy 5 italic bold'),
        bg=cor0, fg=cor0)
    app_linha1.place(x=95, y=10)

    app_linha2 = Label(
        frame_baixo,
        text='',
        height=24, relief='flat',
        pady=5,
        anchor='center',
        font=('Ivy 5 italic bold'),
        bg=cor0, fg=cor0)
    app_linha2.place(x=158, y=10)

    # linhas horizontais
    app_linha3 = Label(
        frame_baixo,
        text='',
        width=177, relief='flat',
        padx=2,
        anchor='center',
        font=('Ivy 1'),
        bg=cor0, fg=cor0)
    app_linha3.place(x=37, y=63)

    app_linha4 = Label(
        frame_baixo,
        text='',
        width=177, relief='flat',
        padx=2,
        anchor='center',
        font=('Ivy 1'),
        bg=cor0, fg=cor0)
    app_linha4.place(x=37, y=127)

    # linha 0
    global b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8

    b_0 = Button(
        frame_baixo,
        command=lambda: controlar('1'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_0.place(x=37, y=8)

    b_1 = Button(
        frame_baixo,
        command=lambda: controlar('2'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_1.place(x=100, y=8)

    b_2 = Button(
        frame_baixo,
        command=lambda: controlar('3'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_2.place(x=163, y=8)

    # linha 1
    b_3 = Button(
        frame_baixo,
        command=lambda: controlar('4'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_3.place(x=37, y=71)

    b_4 = Button(
        frame_baixo,
        command=lambda: controlar('5'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_4.place(x=100, y=71)

    b_5 = Button(
        frame_baixo,
        command=lambda: controlar('6'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_5.place(x=163, y=71)

    # linha 2
    b_6 = Button(
        frame_baixo,
        command=lambda: controlar('7'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_6.place(x=37, y=136)

    b_7 = Button(
        frame_baixo,
        command=lambda: controlar('8'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_7.place(x=100, y=136)

    b_8 = Button(
        frame_baixo,
        command=lambda: controlar('9'),
        text='',
        width=3,
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_8.place(x=163, y=136)

# Botão Jogar
b_jogar = Button(
    frame_baixo,
    command=iniciar_jogo,
    text='JOGAR',
    width=10,
    font=('Ivy 10 bold italic'),
    overrelief=RIDGE,
    relief='raise',
    bg=fundo, fg=cor0)
b_jogar.place(x=84, y=220)

janela.mainloop()