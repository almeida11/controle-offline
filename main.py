import PySimpleGUI as sg

while True:
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
        #seleção de turma
        [sg.Checkbox('Turma A',key = 'var_A'),sg.Checkbox('Turma B',key = 'var_B')],  
        [sg.Checkbox('Turma C',key = 'var_C'),sg.Checkbox('Turma D',key = 'var_D')],
        #inspetor
        [sg.Text("Inspetor"), sg.Input(key='inspetor')],
        #produto
        [sg.Text("Produto"), sg.Input(key='prodTi')],
        #bitola
        [sg.Text("Bitola"), sg.Input(key='bitola')],
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
        #RELATÓRIO
        [sg.Text("Corrida"), sg.Input(key='corrida', size=(15))],
        [sg.Text("Produto"), sg.Input(key='produto')], #acrescentar uma lista de seleção
        [sg.Text("Volumes"), sg.Input(key='volumes', size=(10))],
        [sg.Text("Volumes NC"), sg.Input(key='volumesnc', size=(10))],
        #calcular percentual não conforme
        [sg.Text("Comprimento Máx"), sg.Input(key='cmax', size=(12))],
        [sg.Text("Comprimento Mín"), sg.Input(key='cmin', size=(12))],
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
        #NÃO CONFORMIDADE #add botão de acrescentar mais ud
        [sg.Text("UD"), sg.Input(key='ud')],
        [sg.Text("Defeito"), sg.Input(key='defeito')],
        [sg.Text("Destinação"), sg.Input(key='destino')], #acrescentar uma lista de seleção
        
        
        [sg.Button('Incrementar'),sg.Button('Fechar')],
    ]
    #Gerar Janela
    janela = sg.Window("Relatório do Turno").layout(layout)

    #Extrair os dados da tela
    button, values = janela.Read()
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
##-------------------------------------------#-------------------------------------------------##
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
        sg.popup('Sem Informações!')
        break

#*Relatório do Turno*
#*Turno:* 
#*Data:* 
#*Turma:* "{}"
#*Inspetor:* "{}"
#*Produto:* 
#*Bitola:* 