class Televisao():
    def __init__(self):

        self.volume = 10
        self.canal = 5
        self.ligada= False
        self.digitado = self.canal

    def power (self):
        if self.ligada:
            self.ligada
        else:
            self.ligada = True

    def aumenta_volume(self):
        if self.ligada:
            self.volume += 1
    def diminui_volume(self):
        if self.ligada:
            self.volume -= 1

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
            self.digitado= self.canal
        

    def diminui_canal (self):
        if self.ligada:
            self.canal -= 1
            self.digitado= self.canal
    def canal_digitado(self):
        if self.ligada:
            self.digitado = input (str ('Digite o canal: ') ) 
            self.canal = self.digitado

if __name__ == '__main__':            

    televisao = Televisao()

    print ('A televisão está: {} '.format(televisao.ligada))
    televisao.power()
    print ('A televisão está: {}' .format(televisao.ligada))

    print ('Canal: {}' .format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print ('Canal: {}'.format(televisao.canal))

    print('Volume: {}' .format(televisao.volume))
    televisao.diminui_volume()
    televisao.diminui_volume()
    televisao.diminui_volume()
    print ('Volume: {}' .format(televisao.volume))

    print ('Canal: {}' .format (televisao.digitado))
    televisao.canal_digitado()
    print ('Canal: {}' .format(televisao.digitado))

    print('Canal: {}' .format(televisao.canal))

    televisao.diminui_canal()
    print ('Canal: {}' .format(televisao.canal))

    