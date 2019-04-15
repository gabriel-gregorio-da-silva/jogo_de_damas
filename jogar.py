from Tkinter import *
tela = Tk()

# Geometria da tela
tela.geometry("650x650+20+20")

x = 1 # Andante pela coluna
y = 1 # Andando pelas linhas

global bt_posicao
bt_posicao = []

while True:
    # Esticar os objetos nas colunas
    tela.grid_columnconfigure(x,weight=1)
    # Esticar os objetos nas linhas
    tela.rowconfigure(y,weight=1)

    # Configurações do botão
    bt = Button(text="O", font=('',50),bg = "white",fg = "white",activeforeground="white",activebackground="white")
    # Passar botão para a definição
    bt['command'] = lambda bt=bt: clique(bt)
    bt.grid(row=y, column=x,sticky=NSEW)

    bt_posicao.append(bt)

    # Marcar os fundos em black do jogo
    if ((x%2 == 0 and y%2== 1) or (x%2 == 1 and y%2== 0)):
        bt.configure(bg="black" , fg = "black",activeforeground="black",activebackground = "black")
    
    # Marcar as posições da cor laranja
    if (((x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1)) and y<4):
        bt.configure(fg='orange')

    # Marcar as posições da cor azul
    if (((x%2 == 1 and y%2 == 0) or (x%2 == 0 and y%2 == 1)) and y>5):
        bt.configure(fg='blue')

    # Andar pelas colunas
    x = x+1   

    # Quando chegar a posição da coluna 9
    if x == 15:
        y=y+1 # Ande uma linha.
        x=1   # Resete p x para 1

    # Quando chegaros a linha 9, interrompa tudo!
    if y == 15:
        break

def clique(bt):
    # Andante para todas as posições
    w = 0
    # Andar por todas as posições registradas na variável global
    while len(bt_posicao) > w: 
        # Se a posição registrada for igual ao botão que chamou o evento
        if bt_posicao[w] == bt:
            bt_posicao[w]['bg'] = 'red'
            print('posição ' + str(w))

            # Se a posição estiver vazia
            if bt_posicao[w-7]['fg'] != 'orange' and  bt_posicao[w-7]['fg'] != 'blue': 
                bt_posicao[w-7]['bg'] = 'red'

            # Se a posição estiver vazia
            if bt_posicao[w-9]['fg'] != 'orange' and  bt_posicao[w-9]['fg'] != 'blue': 
                bt_posicao[w-9]['bg'] = 'red'

            # Se a posição estiver vazia
            if bt_posicao[w+9]['fg'] != 'orange' and  bt_posicao[w+9]['fg'] != 'blue': 
                bt_posicao[w+9]['bg'] = 'red'

            # Se a posição estiver vazia
            if bt_posicao[w+7]['fg'] != 'orange' and  bt_posicao[w+7]['fg'] != 'blue': 
                bt_posicao[w+7]['bg'] = 'red'

        w=w+1

tela.mainloop()
