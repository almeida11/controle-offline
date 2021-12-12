import PySimpleGUI as sg


class WindowHeader:
    def __init__(self):
        #Layout da Tela
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
            [sg.Text('Turma')],
            [sg.Combo(["A", "B", "C", "D"], key="turma")],
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
            [sg.Button('Adicionar Cabeçalho')],
        ]
        #Gerar Janela
        title = sg.Window("Relatório do Turno").layout(layout)
        #Extrair os dados da tela
        self.button, self.values = title.Read()
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
    def Iniciar(self):
        #PUXANDO DADOS DO TURNO
        turno0 = self.values['00']
        turno1 = self.values['01']
        turno2 = self.values['02']
        turno_real = ''
        #PUXANDO DADOS DATA
        data = self.values['data']
        #PUXANDO DADOS DE TURMA
        var_1 = self.values['var_A']
        var_2 = self.values['var_B']
        var_3 = self.values['var_C']
        var_4 = self.values['var_D']
        turma_real = ''
        #PUXANDO DADOS INSPETOR
        inspetor = self.values['inspetor']
        #PUXANDO DADOS PRODUTO
        produto = self.values['produto']
        #PUXANDO DADOS BITOLA
        bitola = self.values['bitola']
##-------------------------------------------#-------------------------------------------------##
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
##-------------------------------------------#-------------------------------------------------##
##----------------------------------CABEÇALHO RELATÓRIO----------------------------------------##
##-------------------------------------------#-------------------------------------------------##
        relatorio = open("RelatórioTurno.txt", "a")
        relatorio.write("*RELATORIO DO TURNO*""\n"+
        "*Turno:* {}""\n"
        "*Data:* {}""\n"
        "*Turma:* {}""\n"
        "*Inspetor:* {}""\n"
        "*Produto:* {}""\n"
        "*Bitola:* {}""\n"
        "*Rendimento Metalico Total do Turno:* ".format(turno_real, data, turma_real, inspetor, produto, bitola))
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
    def __Dices__(self):
        #RELATÓRIO
        layout = [
            [sg.Text("Corrida"), sg.Input(key='corrida', size=(15))],
            [sg.Text("Produto"), sg.Input(key='produtoc')], #acrescentar uma lista de seleção
            [sg.Text("Volumes"), sg.Input(key='volumes', size=(10))],
            [sg.Text("Volumes NC"), sg.Input(key='volumesnc', size=(10))],
            #calcular percentual não conforme
            [sg.Text("Comprimento Máx"), sg.Input(key='cmax', size=(12))],
            [sg.Text("Comprimento Mín"), sg.Input(key='cmin', size=(12))], 

            [sg.Button('Incrementar'),sg.Button('incrementar')],
        ]
        report = sg.Window("Relatório do Turno").layout(layout)
        self.button, self.values = report.Read()
    def Report(self):
        pass

    while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == 'Salvar':
        janela2 = __Dices__()
        janela1.hide()
