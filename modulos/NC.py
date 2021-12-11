class NoConf:
    def __init__(self, Vnc, volume):
        self.volume = volume
        self.Vnc = Vnc
    def cal_nc(self):
        pnc = self.volume #calcular percentual de não conforme