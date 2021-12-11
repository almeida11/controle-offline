import PySimpleGUI as sg


class WindowBody:
    def __init__(self):
        layout = [
                #RELATÓRIO
                [sg.Text("Corrida"), sg.Input(key='corrida', size=(15))],
                [sg.Text("Produto"), sg.Input(key='produto')],
                [sg.Text("Volumes"), sg.Input(key='volumes', size=(10))],
                [sg.Text("Volumes NC"), sg.Input(key='volumesnc', size=(10))],
                #calcular percentual não conforme
                [sg.Text("Comprimento Máx"), sg.Input(key='cmax', size=(12))],
                [sg.Text("Comprimento Mín"), sg.Input(key='cmin', size=(12))],
                [sg.Button('Fechar')],
        ]

        window = sg.Window("Corpo", layout)

        while True:
            event, values = window.read()
            if event == 'Fechar' or event == sg.WINDOW_CLOSED:
             break
