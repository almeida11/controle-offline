#SALVANDO INFORMAÇÕES EM TXT
relatorio = open("RelatórioTurno{data}.txt", "a")
relatorio.write("*RELATÓRIO DO TURNO*\n"
    "*Turno:* {}""\n"
    "*Data:* {}""\n"
    "*Turma:* {}""\n"
    "*Inspetor:* {}""\n"
    "*Produto:* {}""\n"
    "*Bitola:* {}""\n"
    "*Rendimento Metálico Total do Turno:* {}".format())