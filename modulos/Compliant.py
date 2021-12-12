import PySimpleGUI as sg
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
class NotCompliant:
    def __UnDep__(self):
        layout = [
            #NÃO CONFORMIDADE #add botão de acrescentar mais ud
            [sg.Text("UD"), sg.Input(key='ud')],
            [sg.Text("Defeito"), sg.Input(key='defeito')],
            [sg.Text("Destinação"), sg.Input(key='destino')], #acrescentar uma lista de seleção
            [sg.Button('Exit')]
        ]
                #Gerar Janela
        janela = sg.Window("Relatório do Turno").layout(layout)
        self.button, self.values = janela.Read()

        #analisar meio que fechar aplicação
    while sg.Button() == ('Exit'):
            break
    def Iniciar(self):
        pass