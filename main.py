import PySimpleGUI as pag
import time
title = "*RELATÓRIO DO TURNO*"

while True:
    #Layout da Tela
    pag.theme("DarkAmber")
    #LAYOUT DA TELA
    layout = [
        #CABEÇALHO
        #seleção de turno
        [pag.Text("Turno")],
        [pag.Checkbox("00:00 às 08:00",key = '00')],
        [pag.Checkbox("08:00 às 16:00",key = '01')],
        [pag.Checkbox("16:00 às 00:00",key = '02')],
        #data
        #seleção de turma
        [pag.Checkbox('Turma A',key = 'var_A'),pag.Checkbox('Turma B',key = 'var_B')],  
        [pag.Checkbox('Turma C',key = 'var_C'),pag.Checkbox('Turma D',key = 'var_D')],
        #inspetor
        #produto
        #bitola
        #RELATÓRIO
        [pag.Text("Corrida"), pag.Input(key='corrida', size=(15))],
        [pag.Text("Produto"), pag.Input(key='produto')],
        [pag.Text("Volumes"), pag.Input(key='volumes', size=(10))],
        [pag.Text("Volumes NC"), pag.Input(key='volumesnc', size=(10))],
        #percentual de não conforme
        [pag.Text("Comprimento Máx"), pag.Input(key='cmax', size=(12))],
        [pag.Text("Comprimento Mín"), pag.Input(key='cmin', size=(12))],
        #NÃO CONFORMIDADE
        [pag.Text("UD"), pag.Input(key='ud')],
        [pag.Text("Defeito"), pag.Input(key='defeito')],
        [pag.Text("Destinação"), pag.Input(key='destino')],
        
        
        

        [pag.Button('Incrementar')],
        [pag.Button('Fechar', key = 'fechar')],
    ]
    #Gerar Janela
    janela = pag.Window("Relatório do Turno").layout(layout)

    #Extrair os dados da tela
    button, values = janela.Read()

    #PUXANDO DADOS DE TURMA
    var_1 = values['var_A']
    var_2 = values['var_B']
    var_3 = values['var_C']
    var_4 = values['var_D']
    #TURMA SELECIONADA
    if var_1 == 1:
        var_1 = "Turma A"
        print(var_1)
    elif var_2 == 1:
        var_2 = "Turma B"
        print(var_2)
    elif var_3 == 1:
        var_3 = "Turma C"
        print(var_3)
    elif var_4 == 1:
        var_4 = "Turma D"
        print(var_4)
    else:
        print('fecha aplicação')
        break

#*Relatório do Turno*
#*Turno:* 
#*Data:* 
#*Turma:* "{}"
#*Inspetor:* "{}"
#*Produto:* 
#*Bitola:* 