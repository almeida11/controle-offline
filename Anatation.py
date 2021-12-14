corrida = 3
produto = 333
volumes = 3
volnc = 5
cmax = 5
cmin = 6
##-------------------------------------------#-------------------------------------------------##
##-----------------------------------CORPO DO RELATÓRIO----------------------------------------##
##-------------------------------------------#-------------------------------------------------##
report = open("RelatórioTurno.txt", "a")
report.write("*-----------------------------------------*""\n"
"*Corrida:* {}""\n"
"*Produto:* {}""\n"
"*Volumes:* {}""\n"
"*Volumes nao conforme:* {}""\n"
"*Comprimento Max:* {}""\n"
"*Comprimento Min:* {}""\n".format(corrida, produto, volumes, volnc, cmax, cmin))