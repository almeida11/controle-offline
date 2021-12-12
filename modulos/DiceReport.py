import PySimpleGUI as sg
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
class DiReport:   
    def Report(self):
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
    def Iniciar(self):
        print("namteo")
