import PySimpleGUI as sg

def make_WindowTurn():
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
        return sg.Window('WindowTurn', layout, finalize=True).Finalize()

def make_WindowDices():
    layout = [
            [sg.Text("Corrida"), sg.Input(key='corrida', size=(15))],
            [sg.Text("Produto"), sg.Input(key='produtoc')], #acrescentar uma lista de seleção
            [sg.Text("Volumes"), sg.Input(key='volumes', size=(10))],
            [sg.Text("Volumes NC"), sg.Input(key='volumesnc', size=(10))],
            #calcular percentual não conforme
            [sg.Text("Comprimento Máx"), sg.Input(key='cmax', size=(12))],
            [sg.Text("Comprimento Mín"), sg.Input(key='cmin', size=(12))], 
            [sg.Button('Salvar'),sg.Button('Incrementar'),sg.Button('Fechar')],
        ]
    return sg.Window('WindowDices', layout, finalize=True).Finalize()

WindowTurn, WindowDices = make_WindowTurn(), None

while True:
    window, event, values = sg.read_all_windows()
    window.Maximize()
    if window == WindowTurn and event in (sg.WIN_CLOSED, 'Fechar'):
        break
    if window == WindowTurn:
#salvando informações e escrevendo no txt
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
        if event == 'Salvar':
            WindowTurn.hide()
            WindowDices = make_WindowDices()
            relatorio = open("RelatórioTurno.txt", "a")
            relatorio.write("*RELATORIO DO TURNO*""\n"
            "*Turno:* {}""\n"
            "*Data:* {}""\n"
            "*Turma:* {}""\n"
            "*Inspetor:* {}""\n"
            "*Produto:* {}""\n"
            "*Bitola:* {}""\n"
            "*Rendimento Metalico Total do Turno:* ""\n".format(turno_real, data, turma_real, inspetor, produto, bitola))
    if window == WindowDices and event in (sg.WIN_CLOSED, 'Fechar'):
        break
    if window == WindowDices:
        if event == 'Incrementar':
            #escrevendo dados
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
            WindowDices.hide()
            WindowDices = make_WindowDices()        
window.close()
