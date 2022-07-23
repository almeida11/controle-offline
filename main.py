import PySimpleGUI as sg

def make_WindowTurn():
        layout = [
        #CABEÇALHO
        #seleção de turno
        [sg.Text('Turno')],
        [sg.Combo(["00:00 as 08:00", "08:00 as 16:00", "16:00 as 00:00"], key="turno")],
        #data
        [sg.Text('Data')],
        [sg.Input(key='data')],
        #seleção de turma
        [sg.Text('Turma')],
        [sg.Combo(["Turma A", "Turma B", "Turma C", "Turma D"], key="turma")],
        #inspetor
        [sg.Text('Inspetor')],
        [sg.Combo(["Fernando", "Josiel Junior", "Marcos Vinicius", "Alex"], key="inspetor")],
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
        turno = values['turno']
        #PUXANDO DADOS DATA
        data = values['data']
        #PUXANDO DADOS DE TURMA
        turma = values['turma']
        #PUXANDO DADOS INSPETOR
        inspetor = values['inspetor']
        #PUXANDO DADOS PRODUTO
        if event == 'Salvar':
            WindowTurn.hide()
            WindowDices = make_WindowDices()
            relatorio = open("RelatórioTurno.txt", "a")
            relatorio.write("*RELATORIO DO TURNO*""\n"
            "*Turno:* {}""\n"
            "*Data:* {}""\n"
            "*Turma:* {}""\n"
            "*Inspetor:* {}""\n"
            "*Rendimento Metalico Total do Turno:* ""\n".format(turno, data, turma, inspetor))
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
