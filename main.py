import tkinter
from tkinter import*
from tkinter import ttk

#cores
cor0 = "#FFFFFF" #branco
cor1 = "#1C1C1C" #cinza escuro
cor2 = "#836FFF" #Slate Blue
cor3 = "#38576b" # valor / value
cor4 = "#3297a8" # azul / blue
cor5 = "#B0C4DE" #Azul Ferro
cor6 = "#20B2AA" #Azul Marinho Claro
cor7 = "#fff873" #amarela / yellow
cor8 = "#DDA0DD" #Plum?
cor9 = "#FF1493" #Dark Pink
cor10 = "#fcfbf7" #branco
cor11 = "#4B0082" #Indigo
fundo = "#8A2BE2" #BlueVioliet



#Criando janela principal

janela = Tk()
janela.title('Jogo Da Velha')
janela.geometry('260x370')
janela.configure(bg=fundo)

#dividindo a janela em 2 frames -------------------------------------------------------------

frame_cima = Frame(janela, width=240, height=100, bg=cor11, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

#Configurando Frame Superior-----------------------------------------------------------------------------

#Jogador 1-------------------------------------------------------------------------------------------
app_x = Label(
    frame_cima, 
    text='X', 
    height=1, 
    relief='flat', 
    anchor='center', 
    font=('Ivy 40 italic bold'), 
    bg=cor11, fg=cor4)
app_x.place(x=25, y=10)


app_x = Label(
    frame_cima, 
    text='Jogador 1', 
    height=1, relief='flat', 
    anchor='center', 
    font=('Ivy 8 italic'), 
    bg=cor11, fg=cor0)
app_x.place(x=22, y=63)

app_x_pontos = Label(
    frame_cima, 
    text='0', 
    height=1, relief='flat', 
    anchor='center', 
    font=('Ivy 27 italic bold'), 
    bg=cor11, fg=cor0)
app_x_pontos.place(x=80, y=20)

#separador---------------------------------------------------------------------------------------
app_separador = Label(
    frame_cima, 
    text=':', 
    height=1, 
    relief='flat', 
    anchor='center', 
    font=('Ivy 27 italic bold'), 
    bg=cor11, fg=cor0)
app_separador.place(x=115, y=18)


#Jogador 2---------------------------------------------------------------------------------------
app_0 = Label(
    frame_cima, 
    text='O', 
    height=1, 
    relief='flat', 
    anchor='center', 
    font=('Ivy 40 italic bold'), 
    bg=cor11, fg=cor9)
app_0.place(x=170, y=10)


app_0 = Label(
    frame_cima, 
    text='Jogador 2', 
    height=1, relief='flat', 
    anchor='center', 
    font=('Ivy 8 italic'), 
    bg=cor11, fg=cor0)
app_0.place(x=165, y=63)

app_0_pontos = Label(
    frame_cima, 
    text='0', 
    height=1, relief='flat', 
    anchor='center', 
    font=('Ivy 27 italic bold'), 
    bg=cor11, fg=cor0)
app_0_pontos.place(x=140, y=20)



#configurando o frame de inferior-------------------------------------------------------------------


#Lógica -------------------------------------------------------------------------------------

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [   
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

jogando = 'X'
joga = ''
contador = 0
contador_de_rodada = 0


def iniciar_jogo():
    #Controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global joga
        global cor
        #comparando o valor recebido


        if i==str(1):
            #verificar se a posição está vazia ou não
            if b_0['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(2):
            #verificar se a posição está vazia ou não
            if b_1['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(3):
            #verificar se a posição está vazia ou não
            if b_2['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(4):
            #verificar se a posição está vazia ou não
            if b_3['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(5):
            #verificar se a posição está vazia ou não
            if b_4['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(6):
            #verificar se a posição está vazia ou não
            if b_5['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(7):
            #verificar se a posição está vazia ou não
            if b_6['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(8):
            #verificar se a posição está vazia ou não
            if b_7['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1

        if i==str(9):
            #verificar se a posição está vazia ou não
            if b_8['text']=='':
                
                #verificar quem está jogando e apóis isso definir a cor do símbolo
                if jogando == 'X':
                    cor = cor4
                if jogando== 'O':
                    cor = cor9
                
                #definindo a cor do texto do botão 
                #e marcar a posição com o valor do jogador atual
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando

                #verificar quem está jogando, e trocar o jogador
                if jogando == 'X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                #incrementa o contador pra próxima rodada
                contador +=1
            
        if contador>=5:
            
            #linhas
            if tabela[0][0] == tabela[0][1]== tabela[0][2]!='':
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1]== tabela[1][2]!='':
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1]== tabela[2][2]!='':
                vencedor(jogando)

            #colunas
            if tabela[0][0] == tabela[1][0]== tabela[2][0]!='':
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1]== tabela[2][1]!='':
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2]== tabela[2][2]!='':
                vencedor(jogando)

            #diagonais
            if tabela[0][0] == tabela[1][1]== tabela[2][2]!='':
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1]== tabela[2][0]!='':
                vencedor(jogando)
            
            #empate
            if contador >= 9:
                vencedor('EMPATE!')
        
#---------------------------------------------------------------------------------------------
    #definir o ganhador
    def vencedor(i):
        global score_1
        global score_2
        global tabela
        global contador_de_rodada
        global contador


        #desabilitando os botões
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
            score_2+=1
            app_vencedor['text']= 'Jogador 2 VENCEU!'
            app_0_pontos['text'] = score_2
        
        if i == 'O':
            score_1=+1
            app_vencedor['text'] = 'Jogador 1 VENCEU!'
            app_x_pontos['text'] = score_1

        if i == 'EMPATE!':
            app_vencedor['text'] = 'EMPATE!'

        def start():
            #limpando os botões
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

            app_vencedor.destroy()
            b_jogar.destroy()

    
        #botao proxima rodada
        b_jogar = Button(
        frame_baixo,
        command=start,
        text='PRÓXIMA', 
        width=10,  
        font=('Ivy 10 bold italic'),
        overrelief=RIDGE,
        relief='raise',
        bg=fundo, fg=cor0)
        b_jogar.place(x=84, y=220)

        def GameOver():
            b_jogar.destroy()
            app_vencedor.destroy()

            encerrar()
        
        if contador_de_rodada >= 5:
            GameOver()
        else:
            contador_de_rodada += 1
           
            #reinicia a tabela
            tabela = [   
                ['1','2','3'],
                ['4','5','6'],
                ['7','8','9']
            ]
            contador = 0

    
    #encerrar o jogo
    def encerrar():
        global tabela
        global contador
        global contador_de_rodada
        global score_1
        global score_2

        tabela = [   
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
        ]
        contador_de_rodada = 0
        score_1 = 0
        score_2 = 0

        #desabilitando os botões
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

        #Jogar novamente
        def jogar_novamente():
            app_x_pontos['text'] = 0
            app_0_pontos['text'] = 0
            app_GameOver.destroy()
            b_jogar.destroy()

            #Chamando a funcão iniciar o jogo
            iniciar_jogo()
        
        #botao jogar novamente
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
        

    #linhas verticais-----------------------------------------------------------------------------------
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

    #linhas horizontais---------------------------------------------------------------------------------

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
    
    #linha 0--------------------------------------------------------------------------------------------
    b_0 = Button(
        frame_baixo,
        command=lambda:controlar('1'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_0.place(x=37, y=8)

    b_1 = Button(
        frame_baixo,
        command=lambda:controlar('2'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_1.place(x=100, y=8)

    b_2 = Button(
        frame_baixo,
        command=lambda:controlar('3'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_2.place(x=163, y=8)

    #linha 1--------------------------------------------------------------------------------------

    b_3 = Button(
        frame_baixo,
        command=lambda:controlar('4'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_3.place(x=37, y=71)

    b_4 = Button(
        frame_baixo,
        command=lambda:controlar('5'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_4.place(x=100, y=71)

    b_5 = Button(
        frame_baixo,
        command=lambda:controlar('6'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_5.place(x=163, y=71)

    #linha 2--------------------------------------------------------------------------------------

    b_6 = Button(
        frame_baixo,
        command=lambda:controlar('7'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_6.place(x=37, y=136)

    b_7 = Button(
        frame_baixo,
        command=lambda:controlar('8'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_7.place(x=100, y=136)

    b_8 = Button(
        frame_baixo,
        command=lambda:controlar('9'), 
        text='', 
        width=3,  
        font=('Ivy 20'),
        overrelief=RIDGE,
        relief='flat',
        bg=fundo, fg=fundo)
    b_8.place(x=163, y=136)

#Botao Jogar--------------------------------------------------------------------------------------
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
