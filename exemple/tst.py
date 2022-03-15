import PySimpleGUI as sg

##-------------------------------------------#-------------------------------------------------##
##-------------------------------RELATÓRIO INSPEÇÃO OFFLINE------------------------------------##
##-------------------------------------------#-------------------------------------------------##
def TelaInicial():
    #Tema da Tela
    sg.theme("Dark")
    #LAYOUT DA TELA
    layout = [
        #CABEÇALHO
        #seleção de turno
        [sg.Text("Informações do Turno")],
        [sg.Checkbox("00:00 às 08:00",key = '00')],
        [sg.Checkbox("08:00 às 16:00",key = '01')],
        [sg.Checkbox("16:00 às 00:00",key = '02')],
        #data
        [sg.Text('Data'), sg.Input(key='data')],
        #seleção de turma
        [sg.Checkbox('Turma A',key = 'var_A'),sg.Checkbox('Turma B',key = 'var_B')],  
        [sg.Checkbox('Turma C',key = 'var_C'),sg.Checkbox('Turma D',key = 'var_D')],
        #inspetor
        [sg.Text('Inspetor')],
        [sg.Combo(["Rayson", "Gabriel", "Vinnicius", "Alan"], key="inspetor")],
        #produto
        [sg.Text("Produto"), sg.Input(key='produto')],
        #bitola
        [sg.Text("Bitola"), sg.Input(key='bitola')],
        #gerar cabeçalho
        [sg.Button('Salvar'), sg.Button('Fechar')],
    ]
    #envio de layout para tela
    janela01 = sg.Window('Tela 01').layout(layout)
    #envio de dados para memoria
    button, values = janela01.read()
##-------------------------------------------#-------------------------------------------------##
    turno0 = values['00']
    turno1 = values['01']
    turno2 = values['02']
    turno_real = ''
    #PUXANDO DADOS DATA
    data = values['data']
    #PUXANDO DADOS DE TURMA
    var_1 = values['var_A']
    var_2 = values['var_B']
    var_3 = values['var_C']
    var_4 = values['var_D']
    turma_real = ''
    #PUXANDO DADOS INSPETOR
    inspetor = values['inspetor']
    #PUXANDO DADOS PRODUTO
    produto = values['produto']
    #PUXANDO DADOS BITOLA
    bitola = values['bitola']
    if turno0 == 1:
        turno_real = '00:00 as 08:00'
    elif turno1 == 1:
        turno_real = '08:00 as 16:00'
    elif turno2 == 1:
        turno_real = "16:00 as 00:00"
    else:
        turno_real = "Turno nao selecionado!"
##-------------------------------------------#-------------------------------------------------##
    if var_1 == 1:
        turma_real = "A"
    elif var_2 == 1:
        turma_real = "B"
    elif var_3 == 1:
        turma_real = "C"
    elif var_4 == 1:
        turma_real = "D"
    else:
        turma_real = "Turma nao selecionada!"
##-------------------------------------FUNCIONAMENTO-------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
#funções dos botões da janela 01
    if button == 'Salvar':
        janela01.close()
    if button == 'Fechar':
        exit()
##-------------------------------------------#-------------------------------------------------##
##----------------------------------CABEÇALHO RELATÓRIO----------------------------------------##
##-------------------------------------------#-------------------------------------------------##
#escrevendo as informações no arquivo txt
    relatorio = open("RelatórioTurno.txt", "a")
    relatorio.write("*RELATORIO DO TURNO*""\n"
    "*Turno:* {}""\n"
    "*Data:* {}""\n"
    "*Turma:* {}""\n"
    "*Inspetor:* {}""\n"
    "*Produto:* {}""\n"
    "*Bitola:* {}""\n"
    "*Rendimento Metalico Total do Turno:* ""\n".format(turno_real, data, turma_real, inspetor, produto, bitola))
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##

def TelaDados():
    layout2 = [
        [sg.Button('Prosseguir'),sg.Button('Fechar')],
    ]
    janela02 = sg.Window('Tela 02').layout(layout2)
    button, values = janela02.read()
    if button == "Prosseguir":
        while button == "Prosseguir" or button == "Incrementar":

                layout3 = [
                    [sg.Text("Corrida"), sg.Input(key='corrida', size=(15))],
                    [sg.Text("Produto"), sg.Input(key='produtoc')], #acrescentar uma lista de seleção
                    [sg.Text("Volumes"), sg.Input(key='volumes', size=(10))],
                    [sg.Text("Volumes NC"), sg.Input(key='volumesnc', size=(10))],
                    #calcular percentual não conforme
                    [sg.Text("Comprimento Máx"), sg.Input(key='cmax', size=(12))],
                    [sg.Text("Comprimento Mín"), sg.Input(key='cmin', size=(12))], 
                    [sg.Button('Incrementar'),sg.Button('Fechar')],
                ]
                janela03 = sg.Window('Tela 03').layout(layout3)
                button, values = janela03.read()
        ##-------------------------------------------#-------------------------------------------------##
        #condição para escrever dados de corridas/fechar aplicação
                if button == "Incrementar":
                    corrida = values['corrida']
                    produto = values['produtoc']
                    volumes = values['volumes']
                    volnc = values['volumesnc']
                    cmax = values['cmax']
                    cmin = values['cmin']
                    ##-------------------------------------------#-------------------------------------------------##
                    ##-----------------------------------CORPO DO RELATÓRIO----------------------------------------##
                    ##-------------------------------------------#-------------------------------------------------##
                    relatorio = open("RelatórioTurno.txt", "a")
                    relatorio.write("*-----------------------------------------*""\n"
                    "*Corrida:* {}""\n"
                    "*Produto:* {}""\n"
                    "*Volumes:* {}""\n"
                    "*Volumes nao conforme:* {}""\n"
                    "*Comprimento Max:* {}""\n"
                    "*Comprimento Min:* {}""\n".format(corrida, produto, volumes, volnc, cmax, cmin))
                    
                else:
                    exit()
    else:
        exit()
##-------------------------------------------#-------------------------------------------------##
Tela01 = TelaInicial()
Tela02 = TelaDados()