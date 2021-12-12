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
