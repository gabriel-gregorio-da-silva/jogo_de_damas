/*
    autor: Gabriel Gregório da Silva
    data: 26 de outubro de 2019 a 27 de outubro de 2019
    ultima modificação: None
    site: https://github.com/gabrielogregorio/
    observação: Meus primeiros passos em Javascript. Não espere um código profissional!
*/

var lista_botoes = [];               // Todos os id's dos botões que ficarão disponíveis
var lista_estado_botoes = []         // Todos os estados dos botões que ficarão disponíveis
var objeto_clicado = false;          // Alguma peça foi clicada?
var vez = 'x';                       // De quem é a vez?
var inimigo = 'o';                   // Quem é o inimigo?
var objeto_lista_selecionado = -1;   // Quem tinha sido clicado anteriormente?
var posicao_dos_inimigos = [[]];     // Qual é a posição dos inimigos?
var qtd_de_pecas = {'x':15,'o':15};  // Peças do inimgo

/* Posiciona os botões na tela */
function posicionar_botoes(){

    /* número total de botões */
    var botoes = 136;

    /* Ande por todas as posições dos futuros botões */
    for(var i = 1; i < botoes; i++) {

        /* Id do futuro botão */ 
        var id = 'btn' + i;

        /* Adiciona o id na lista dos botões */
        lista_botoes.push(id);

        /* Acessa a div e coloca o código de um botão */
        document.getElementById('principal').innerHTML += "<button onclick=clique(this) class='btn_principal' id = 'btn"+ i +"'></button>";

        /* Se for divisível por zero, adicione uma quebra de linha*/
        if (i % 15 == 0){
            document.getElementById('principal').innerHTML += '<br>';
        }
    }    
    /* Posicione os botões peça lista recem criada*/
    posicionar_pecas_pela_lista();
}

function posicione_uma_peca(i,estado,fg){

    /* Acesse uma posição e sobrescreva o estado */
    document.getElementById(lista_botoes[i]).innerText = estado;

    if (i % 2 == 1) {
        estilizar_botoes(lista_botoes[i],'#d8c169','#d8c169');
    } else {
        estilizar_botoes(lista_botoes[i],fg,'#362018');
    }

    /* Adicione o estado na lista de estados da peça posicionada */
    lista_estado_botoes.push(estado);
}

/* Posiciona as peças 'x' e 'o' nas suas respectivas posições*/
function posicionar_pecas_pela_lista(){

    /* Busque pelas posições disponíveis */
    for (i=0; i < lista_botoes.length; i++){

        /* Se for par (Na lista) e for menor que o valor máximo */
        if ((i % 2 == 0) && (i < 30)) {

            /* Posicione o 'x' com o fundo branco*/
            posicione_uma_peca(i,'x','white');

        } else if ((i % 2 == 0) && (i > lista_botoes.length-30)){

            /* Posicione o 'o' com o fundo branco*/
            posicione_uma_peca(i,'o','white');

        } else {
            /* Posicione o 'n' para torna-lo disponível */
            posicione_uma_peca(i,'n','#362018');
        }
    }
}

/* Reposiciona o tabuleiro pelo estado das peças */
function posicionar_pecas_pelo_estado(){

    /* Busca pelos registros dispoíveis */
    for (i=0; i < lista_botoes.length; i++) {

        /* Se tiver um x */
        if (lista_estado_botoes[i] == 'x'){
            /* Marque um x */
            document.getElementById(lista_botoes[i]).innerText = 'x';
            var fg = 'white';

        } else if (lista_estado_botoes[i] == 'o') {
            /* Marque o o */
            document.getElementById(lista_botoes[i]).innerText = 'o';
            var fg = 'white';

        } else {
            /* Marque o n*/
            document.getElementById(lista_botoes[i]).innerText = 'n';
            var fg = '#362018';

            /* Pode ter um 'pos' aqui, então sobrescreva essa posição com um 'n' */
            lista_estado_botoes.push('n');
        }

        if (i % 2 == 1) {
            estilizar_botoes(lista_botoes[i],'#d8c169','#d8c169');
        } else {
            estilizar_botoes(lista_botoes[i],fg,'#362018');
        }

    }
}

function estilizar_botoes(id,fg,bg){
    document.getElementById(id).style.color           = fg;
    document.getElementById(id).style.backgroundColor = bg;
    document.getElementById(id).style.width           = "70px";
    document.getElementById(id).style.height          = "70px";
    document.getElementById(id).style.fontSize        = "1.2em";
}

function troca_vez() {
    if (vez == 'x') {
        vez = 'o';
        inimigo = 'x';
    } else {
        vez = 'x';
        inimigo = 'o';
    }
}

function analisar_clique_botao(posicao){

    /* Verifica se a posição existe */
    if (document.getElementById(lista_botoes[posicao]) != undefined ){

         /* Se ela estiver disponível para clique */
        if (document.getElementById(lista_botoes[posicao]).innerText == 'n'){

             /* Atualize o estilo */
            estilizar_botoes(lista_botoes[posicao], fg = "#00868a", bg = "#00868a")

            /* Marque como uma posição disponível para clique */
            document.getElementById(lista_botoes[posicao]).innerText = 'pos';
         }
    }
}

function analisar_clique_marca_inimigos(posicao_inimigo,posicao_para_ir){
    /* Verifica se as posições existem */
     if ((document.getElementById(lista_botoes[posicao_para_ir]) != undefined ) && (document.getElementById(lista_botoes[posicao_inimigo]) != undefined)){

        /* Se exitir inimigo e for possivel passar por cima dele */
        if ((document.getElementById(lista_botoes[posicao_para_ir]).innerText == 'n')  && (document.getElementById(lista_botoes[posicao_inimigo]).innerText == inimigo)){

            /* Adicionar a posição que o jogador pode ir e a posição que o inimigo está */
            posicao_dos_inimigos.push([posicao_para_ir, posicao_inimigo]);

            /* Atualiza o estilo da posição possivel para ir */
            estilizar_botoes(lista_botoes[posicao_para_ir], fg = "#00868a", bg = "#00868a")

            /* Marca como uma posição possível para ir */
            document.getElementById(lista_botoes[posicao_para_ir]).innerText = 'pos';
        }
    }
}

/* Realiza comandos se houver um clique em alguma peça */
function clique(btn){

    /* Se houver um clique em alguma posição com uma peça da vez */
    if ((document.getElementById(btn.id).innerText != 'n') && (document.getElementById(btn.id).innerText != 'pos')  && (document.getElementById(btn.id).innerText == vez)){

        /* Se o objeto já foi clicado anteriormente: Remover o destaque das peças clicadas anteriormente */        
        if (objeto_clicado == true){
            posicionar_pecas_pelo_estado();
        }

        /* Busca pelas posições registradas */ 
        for (i=0; i < lista_botoes.length; i++) {

            /* Botão que clicou foi localizado no registro */
            if (btn.id == lista_botoes[i] ){

                /* Altere a cor desse botão */
                estilizar_botoes(btn.id, fg = "white", bg = "#00868a")

                /* Posição do objeto que foi clicado */
                objeto_lista_selecionado = i;

                /* Colorir casas que é possivel mover */
                analisar_clique_botao(i-14);
                analisar_clique_botao(i-16);
                analisar_clique_botao(i+14);
                analisar_clique_botao(i+16);

                /* Salvar as possiveis posições que é possivel comer o adversário */
                posicao_dos_inimigos = [[999,999]];

                /* Colorir casas que é possivel comer */
                analisar_clique_marca_inimigos(i-14,i-28);
                analisar_clique_marca_inimigos(i-16,i-32);
                analisar_clique_marca_inimigos(i+14,i+28);
                analisar_clique_marca_inimigos(i+16,i+32);

                /* Objeto já foi selecionado! */
                objeto_clicado = true;
            }
        }
    /* Clique ocorreu em uma posição disponível mover */
    } else if (document.getElementById(btn.id).innerText == 'pos'){

        /* Busca pelas posições registradas */ 
        for (i=0; i < lista_botoes.length; i++) {

            /* Botão que clicou foi localizado no registro */
            if (btn.id == lista_botoes[i] ){
                /* Uma posição para mover foi encontrada. Talvez seja desnecessário isso. */
                if (document.getElementById(lista_botoes[i]).innerText = 'pos'){

                    /* Se alguma peça foi comida, remova ela. */
                    comeu(i);

                    /* Atualize a posição com o jogador da vez*/
                    document.getElementById(lista_botoes[i]).innerText = vez;

                    /* Atualize o estilo desse botão para torna-lo vísvel */
                    estilizar_botoes(lista_botoes[i],'white','#362018');

                    /* Atualize o estado da posição clicada */
                    lista_estado_botoes[i] = vez;

                    /* Atualize o estado da posição selecionada anteriormente */
                    lista_estado_botoes[objeto_lista_selecionado] = 'n';

                    /* Reposicione as peças pelo estado delas */ 
                    posicionar_pecas_pelo_estado();

                    /* Atualiza o jogador da vez */
                    troca_vez();

                    /* Tivemos um vencedor? */
                    alguem_ganhou();
                }
            }
        }
    }
}

/* Verifica se alguma peça foi comida */
function comeu(btn){

    /* Busca pelas posições registradas onde havia inimigos */ 
    for (o=0; o < posicao_dos_inimigos.length; o++){

        /* Se a posição clicada passou por um inimigo*/
        if ( posicao_dos_inimigos[o][0] == btn ) {

            /* Atualiza quantidade de peças do inimigo */
            if (lista_estado_botoes[posicao_dos_inimigos[o][1]] == 'x'){
                qtd_de_pecas['x'] = qtd_de_pecas['x'] -1;

            } else if (lista_estado_botoes[posicao_dos_inimigos[o][1]] == 'o') {
                qtd_de_pecas['o'] = qtd_de_pecas['o'] -1;
            }

            /*Remova o inimigo*/
            lista_estado_botoes[posicao_dos_inimigos[o][1]] = 'n';

        }
    }
}

function alguem_ganhou(){
    if (qtd_de_pecas['x'] == 0){
        alert("Jogador 'o' você ganhou! Confirme para resetar! ");
        reseta()

    } else if (qtd_de_pecas['o'] == 0) {
        alert("Jogador 'x' você ganhou! Confirme para resetar! ");
        reseta()
    }

}

function reseta(){
    window.location.reload(1);
}
