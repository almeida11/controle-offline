import PySimpleGUI as sg
from modulos import Header
from modulos import DiceReport
##-------------------------------------------#-------------------------------------------------##
##-------------------------------RELATÓRIO INSPEÇÃO OFFLINE------------------------------------##
##-------------------------------------------#-------------------------------------------------##
Tela_Inicial = Header.WindowHeader()
Tela_Dados = DiceReport.DiReport()
Tela_Dados.Iniciar()
Tela_Inicial.Iniciar()
while True:
    window, event, values = sg.read_all_windows()
    if window == Tela_Inicial and event == sg.WIN_CLOSED:
        break
    if window == Tela_Inicial and event == 'Salvar':
        Tela_Dados = Report() #chamar a def não a class
        Tela_Inicial.hide()