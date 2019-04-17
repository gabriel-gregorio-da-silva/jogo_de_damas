from tkinter import *
tela = Tk()

# Geometria da tela
tela.geometry("650x650+20+20")

# Lista com todos os botões criados
global bt_posicao

# Recebe a posição antiga de um botão para limpar as áreas possiveis!
global salvar_posicao

# Cor de fundo anterior selecionada
global padrao_cor

# Configurador de primeira vez
global primeira_vez

# Quantidade de casas na horizontal e na vertical
global bloco_quantidade

bt_posicao = []
bloco_quantidade = 9
primeira_vez = 0

x = 1 # Andante pela coluna
y = 1 # Andando pelas linhas

# Definições de um click
def clique(bt):
    # Lista com todos os botões criados
    global bt_posicao

    # Recebe a posição antiga de um botão para limpar as áreas possiveis!
    global salvar_posicao

    # Cor de fundo anterior selecionada
    global padrao_cor

    # Configurador de primeira vez
    global primeira_vez

    # Andar por todas as posições registradas na variável global
    w = 0
    while len(bt_posicao) > w: 


        # Se a posição salva for igual ao botão que chamou o evento
        if (bt_posicao[w] == bt and (bt['fg'] == 'orange' or  bt['fg'] == 'blue')):
            print('\n\nposição clicada ' + str(w))
            # bt_posicao[w]['text'] = str(w)

            # Caso da primeira vez de execução
            if primeira_vez == 0:
                print('primeira vez')

                # Salvar o background do botão que chamou o evento
                padrao_cor = bt_posicao[w]['bg']

                # Salvar a posição do botão que chamou o evento

                salvar_posicao = w

                # Impedir retrocessos
                primeira_vez = 1

            # Se o botão salvo for diferente do anterior
            if bt_posicao[salvar_posicao] != bt or primeira_vez == 1:
                primeira_vez = 2

                # Desmarcação de posição
                # Se a posição estiver vazia
                print(' -- Desmarcação dos objetos --')
    
                # Se a posição estiver vazia
                try:
                    print('Desmarcar posição antiga {} - 7'.format(salvar_posicao))
                    if (bt_posicao[salvar_posicao-7]['fg'] != 'orange' and  bt_posicao[salvar_posicao-7]['fg'] != 'blue') and analise(salvar_posicao,-7): 

                        bt_posicao[salvar_posicao-7].configure(bg = padrao_cor,fg = padrao_cor,  activebackground = padrao_cor, activeforeground = padrao_cor)
                except:
                    print(' ** ERRO')

                # Se a posição estiver vazia
                try:
                    print('Desmarcar posição antiga {} - 9'.format(salvar_posicao))
                    if (bt_posicao[salvar_posicao-9]['fg'] != 'orange' and  bt_posicao[salvar_posicao-9]['fg'] != 'blue') and analise(salvar_posicao,-9): 
                        bt_posicao[salvar_posicao-9].configure(bg = padrao_cor,fg = padrao_cor,  activebackground = padrao_cor, activeforeground = padrao_cor)
                except:
                    print(' ** ERRO')
    
                # Se a posição estiver vazia
                try:
                    print('Desmarcar posição antiga {} + 9'.format(salvar_posicao))
                    if (bt_posicao[salvar_posicao+9]['fg'] != 'orange' and  bt_posicao[salvar_posicao+9]['fg'] != 'blue') and analise(salvar_posicao,+9): 
                        bt_posicao[salvar_posicao+9].configure(bg = padrao_cor,fg = padrao_cor,  activebackground = padrao_cor, activeforeground = padrao_cor)
                except:
                    print(' ** ERRO')
    
                # Se a posição estiver vazia
                try:
                    print('Desmarcar posição antiga {} + 7'.format(salvar_posicao))
                    if (bt_posicao[salvar_posicao+7]['fg'] != 'orange' and  bt_posicao[salvar_posicao+7]['fg'] != 'blue') and analise(salvar_posicao,+7): 
                        bt_posicao[salvar_posicao+7].configure(bg = padrao_cor,fg = padrao_cor,  activebackground = padrao_cor, activeforeground = padrao_cor)
                except:
                    print(' ** ERRO')
    


                print(' ---------------------------------------')
                # Marcação de posição
                # Se a posição estiver vazia
    
                # Se a posição estiver vazia
                print(' Marcar posição atual {} - 7'.format(w))
                try:
                    if (bt_posicao[w-7]['fg'] != 'orange' and  bt_posicao[w-7]['fg'] != 'blue') and analise(w,-7): 
                        bt_posicao[w-7].configure(bg = 'red' ,fg = 'red',  activebackground = 'red', activeforeground = 'red')
                except:
                    print(' ** ERRO')
    
                # Se a posição estiver vazia
                print(' Marcar posição atual {} - 9'.format(w))
                try:
                    if (bt_posicao[w-9]['fg'] != 'orange' and  bt_posicao[w-9]['fg'] != 'blue')  and analise(w,-9): 
                        bt_posicao[w-9].configure(bg = 'red' ,fg = 'red',  activebackground = 'red', activeforeground = 'red')
                except:
                    print(' ** ERRO')
    
                # Se a posição estiver vazia
                print(' Marcar posição atual {} + 9'.format(w))
                try:
                    if (bt_posicao[w+9]['fg'] != 'orange' and  bt_posicao[w+9]['fg'] != 'blue') and analise(w,+9): 
                        bt_posicao[w+9].configure(bg = 'red' ,fg = 'red',  activebackground = 'red', activeforeground = 'red')
                except:
                    print(' ** ERRO')
    
                # Se a posição estiver vazia
                print(' Marcar posição atual {} + 7'.format(w))
                try:
                    if (bt_posicao[w+7]['fg'] != 'orange' and  bt_posicao[w+7]['fg'] != 'blue') and analise(w,+7): 
                        bt_posicao[w+7].configure(bg = 'red' ,fg = 'red',  activebackground = 'red', activeforeground = 'red')
                except:
                    print(' ** ERRO')
    
                salvar_posicao = w
                padrao_cor = bt_posicao[w]['bg']

                print('> Posição {} salva para a próxima execução, com a cor {}'.format(salvar_posicao,padrao_cor))
    
                # Interromper loop
                w = len(bt_posicao) 
    
        w=w+1






# Verifica se a posição pode dar algum problema
def analise(posicao_w,elemento):
    print('Definição Análise')
    print(' Posição analisada: ' + str(posicao_w) + ' elemento em análse: ' + str(elemento))
    #[verificado]
    # Não pode permitir menores que 0!
    if posicao_w == 0:
        print('  Posição 0 detectada')
        if elemento == +9:
            print('   Elemento vale +9')
            return True
        else:
            print('   Elemento não vale +9')            
            return False
        
    lista_superior = [1,2,3,4,5,6,7]
    lista_lateral_esquerda = [8,16,24,32,40,48]
    lista_inferior = [56,57,58,59,60,61,62,63]
    lista_lateral_direita = [55,47,39,31,23,15]
    
    #[verificado]
    if posicao_w in lista_superior:
        print('  A posição está na lista superior')
        if posicao_w == 7:
            print('   A posição vale 7')
            if elemento == +7:
                print('    O elemento vale +7')
                return True
            else:
                print('    O elemento não vale +7')
                return False
        else:
            print('   A posição não vale 7')
            if elemento == +7 or elemento == +9:
                print('     A posição vale +7 ou +9')
                return True
            else:
                print('     A posição não vale +7 ou +9')
                return False
    
    #[verificado]
    elif posicao_w in lista_lateral_esquerda: 
        # Só pode permitir o -7 e o +9!.
        print('  A posição está na lista lateral esquerda')
        if elemento == -7 or elemento == +9:
            print('   O elemento vale -7 ou +9')
            return True
    
    #[verificado]
    elif posicao_w in lista_inferior:
        print('  A posição está na lista inferior')
        if posicao_w == 56:
            print('   A posição vale 56')
            if elemento == -7:
                print('    O elemento vale -7')
                return True
            else:
                print('    O elemento não vale -7')
                return False

        elif posicao_w == 63:
            print('  A posição vale 63')
            if elemento == -9:
                print('   O elemento vale -9')
                return True
            else:
                print('   O elemento não vale -9')
                return False
        else:
            print('  A posição não vale 63')
            if elemento == -7 or elemento == -9:
                print('   O elemento vale -7 ou -9')
                return True
            else:
                print('   O elemento não vale -7 ou -9')
                return False
    
    #[verificado]
    elif posicao_w in lista_lateral_direita:
        print('  A posição está na lista lateral direita')
        if elemento == -9 or elemento == +7:
            print('   O elemento vale -9 ou +7')
            return True
        else: 
            print('   O elemento não vale -9 ou +7')
            return False
    else:
        print('  Nenhuma coisa anormal aconteceu!')
        return True
#        print('Isso não deveria ter acontecido, você achou um bug!')
#        print('Tratamento na posição {} com o elemento {}, ou seja, a posição a ser analisada é a {}'.format(posicao_w,elemento,elemento+posicao_w))
    
#    [checked] Se for da lista lateral direita e não for o 63, permita o +7 e o -9. Se for o 7, permita apenas a +7



# Criar o tabuleiro
while True:
    # Esticar os objetos nas colunas
    tela.grid_columnconfigure(x,weight=1)

    # Esticar os objetos nas linhas
    tela.rowconfigure(y,weight=1)

    # Configurações do botão
    bt = Button(text="O", font=('',50))
    # Passar botão para a definição
    bt['command'] = lambda bt=bt: clique(bt)
    bt.grid(row=y, column=x,sticky=NSEW)

    # Salvar o botão em uma lista de acesso global
    bt_posicao.append(bt)

    # Marcar os fundos em black do jogo
    if ((x%2 == 0 and y%2== 1) or (x%2 == 1 and y%2== 0)):
        bt.configure(bg="black" , fg = "black",activeforeground="black",activebackground = "black")
    else:
        bt.configure(bg="white" , fg = "white",activeforeground="white",activebackground = "white")

    # Marcar as posições da cor laranja
    if (((x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1)) and y<4):
        bt.configure(fg='orange',activeforeground='orange')

    # Marcar as posições da cor azul
    if (((x%2 == 1 and y%2 == 0) or (x%2 == 0 and y%2 == 1)) and y>5):
        bt.configure(fg='blue',activeforeground='blue')

    # Andar pelas colunas
    x = x+1   

    # Quando chegar a posição da coluna 9
    if x == bloco_quantidade:
        y=y+1 # Ande uma linha.
        x=1 # Resete p x para 1

    # Quando chegaros a linha 9, interrompa tudo!
    if y == bloco_quantidade:
        break

tela.mainloop()
