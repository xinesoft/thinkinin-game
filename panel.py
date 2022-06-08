import xs
from xs import *
class Panel:
    
    def __init__(self):
        self.posi = pantalla.Ancho()/2-96
        self.boton = {}
        self.posx=30
        self.posy = 230
        self.sonar = list(range(12))
        self.comienzo = 0
        self.sover = Sonido("musica/clack.ogg")
        for n in range(12) :           
                                                                                 
            msg = str('img/panel/%d.png'%n)
            self.boton[n] = Graficos(msg)
            
            if(n % 3 == 0):
                self.posy+=48
                self.posx=self.posi
            
            self.boton[n].Posicion(self.posx,self.posy)
            self.posx+=69 

    def Dibujar(self):
              
        if self.comienzo == 1:
            for n in range(12):
                
                if self.boton[n].Colisiona(raton) :
                
                    if self.sonar[n] == 1:
                        self.sover.play()
                        self.sonar[n] = 0           
                else : self.sonar[n] = 1
            
                
                             
                 
               
        for n in range(12):
            if self.comienzo == 1:
                
                if(self.boton[n].Colisiona(raton)):
                    self.boton[n].PosicionY(self.boton[n].PosicionIY()-2)
                    
                else : 
                    self.boton[n].PosicionY(self.boton[n].PosicionIY())
                    
                    
                boton = pygame.mouse.get_pressed()
                if(self.boton[n].Colisiona(raton)):     
                    if boton[0]:
                        
                        self.boton[n].PosicionY(self.boton[n].PosicionIY())
                 
                tecla = pygame.key.get_pressed()
                
                if tecla[K_KP1]:
                    self.boton[0].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP2]:
                    self.boton[1].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP3]:
                    self.boton[2].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP4]:
                    self.boton[3].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP5]:
                    self.boton[4].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP6]:
                    self.boton[5].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP7]:
                    self.boton[6].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP8]:
                    self.boton[7].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP9]:
                    self.boton[8].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP0]:
                    self.boton[9].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP_PERIOD]:
                    self.boton[10].PosicionY(self.boton[n].PosicionIY()+2)
                elif tecla[K_KP_ENTER]:
                    self.boton[11].PosicionY(self.boton[n].PosicionIY()+2)
               

            self.boton[n].Dibujar()



class Panel2:
    
    def __init__(self):
        self.boton = list(range(4))
        posx = 320 - 160
        posy = 325
        self.comienzo = 0
        for n in self.boton:
            msg = str("img/panel/0%d.png"%n)
            self.boton[n] = Graficos(msg,posx,posy)
            posx += 80
    def Dibujar(self):
        for n in range(4):           
            if self.comienzo == 1:    
                if(self.boton[n].Colisiona(raton)):
                    self.boton[n].PosicionY(self.boton[n].PosicionIY()-2)
                        
                else : 
                    self.boton[n].PosicionY(self.boton[n].PosicionIY())
            
            self.boton[n].Dibujar()
        
        


    