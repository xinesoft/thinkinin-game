from xs import *

class Comienzo:
    def __init__(self):
        
        self.numero = Fuentes("fonts/fuente.ttf",250)
        self.scomienzo = Sonido("musica/comienzo.ogg")
        self.fondo = Graficos("img/menu/fondon.png")
        self.graficos = [None,Graficos("img/comienzo/1.png"),\
                          Graficos("img/comienzo/2.png"),\
                          Graficos("img/comienzo/3.png")]
        for n in range(1,4) :
            self.graficos[n].Posicion(320,240)
        self.segundo = 3
        self.timer = Timer(1000)
        self.color = list(range(1,7))     
       
        
        
    
    def Dibujar(self):
        end = 0
        
       
        self.fondo.Dibujar()
        self.graficos[self.segundo].Dibujar(1)
        
        
        
        if self.timer.EndLoop():
                self.segundo-=1
                
        if self.segundo == 0:
            self.scomienzo.play()
            
        
                
                    
