from random import randint
from graficos import *
from comienzo import Comienzo
from panel import Panel
from xs import *
import sys,record,xs
import puntuacion

class Prueba5:
    def __init__(self):
        self.num = [None,None,None,None,None,None]
        self.puntuacion = 0
        self.salire = 0
        self.segundos = 60
        self.segund = Timer(1000)
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))   
        
        self.tiza = Fuentes("fonts/tiza.ttf",30)
        self.tiza.SetColor(255, 255, 255)
        self.tiza2 = Fuentes("fonts/tiza.ttf",40)
        self.tiza2.SetColor(255, 255, 255)
        self.fuente= Fuentes("fonts/fuente.ttf",40)
        self.fuente.SetColor(255,0,0)
        
        self.sclick = click
        
        self.pizarra = Graficos("img/menu/pizarra.png",pantalla.Ancho()/2,142)
        self.hexa = Graficos("img/practicas/hexa.png",pantalla.Ancho()/2,142)
        self.sonar = 1
        self.panel = Panel()
        
        self.comienzo = Comienzo()
        
        self.NuevaPregunta()
        while self.comienzo.segundo >= 1: 
            self.comienzo.Dibujar()
            self.Dibujar()
        self.panel.comienzo = 1 
        self.salir = False
        Musica.play()
        
        while not self.salir : 
            self.Dibujar()
    def Dibujar(self):
        
        Update()
        
        for event in pygame.event.get():
                
                if event.type == MOUSEMOTION:
                    raton.Posicionar()    
                if self.comienzo.segundo == 0:
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE :
                            self.salir = 1   
                            if xs.modo == 1:
                                            self.salire = 1
                        self.ActualizarKBoton()                 
                        
                    if event.type == MOUSEBUTTONDOWN: 
                          
                        mousebutton = pygame.mouse.get_pressed()
                        if mousebutton[0] == 1:
                            self.ActualizarMBoton()
        self.pizarra.Dibujar(1)
        self.hexa.Dibujar(1)
        self.panel.Dibujar()
        
        
        
        if xs.IDIOMA == 0:
            self.tiza.Dibujar("TiEmpo:",480,25,1,0)
            self.tiza.Dibujar("Puntuacion:",70,25,1,0)
        else :
            self.tiza.Dibujar(" TimE:",480,25,1,0)
            self.tiza.Dibujar("  ScorE:",70,25,1,0)
        self.fuente.Dibujar(self.puntuacion,140,85,1,1)
        
        self.fuente.Dibujar(self.segundos,525,85,1,1)
        if self.comienzo.segundo == 0:
            self.tiza2.Dibujar(self.num[0],250,83,1,1)
            self.tiza2.Dibujar(self.num[1],320,83,1,1)
            self.tiza2.Dibujar(self.num[2],390,83,1,1)
            self.tiza2.Dibujar(self.resuljug,320,205,1,1)
            if self.segund.EndLoop():
                        self.segundos-=1
                        if self.segundos == -1:
                            self.DibujarResultado() 
            raton.Dibujar()
        
    def DibujarResultado(self):
          
          if xs.modo == 0:
              record.Cargar(4,self.puntuacion) 
          else:
              if self.puntuacion >= 20 : self.resex = 2.0
              else : self.resex = float(self.puntuacion*2)/20 
              puntuacion.examen += self.resex
          self.salir = 1 
             
    def NuevaPregunta(self):
        self.primer = 1
        self.resuljug = "?"
        self.num[:3] = randint(0,9),randint(0,9),randint(0,9)
        self.num[3:5] = self.num[0] + self.num[1] ,self.num[1] + self.num[2]       
        self.num[5] = self.num[3] + self.num[4]     
        self.resulmac = self.num[5]
        
    
    def Resultado(self):
        if str(self.resulmac) != self.resuljug:
            if self.puntuacion > 0: self.puntuacion-=1

        else : self.puntuacion+=1
        
    def ActualizarKBoton(self):
        
        keydown = pygame.key.get_pressed()
                
        
        if self.sonar == 1:
            for n in range(256,267):
                if keydown[n]:
                    self.sclick.play()
                    self.sonar = 0
            if keydown[271]:
                self.sclick.play()
                self.sonar = 0
                
        if len(str(self.resuljug)) <= 1:
            if  keydown[K_KP0]:
                if self.primer :
                    self.resuljug = "0"
                    self.primer = 0   
                else : self.resuljug+="0"
            elif keydown[K_KP1]:
                if self.primer :
                    self.resuljug = "1"
                    self.primer = 0   
                else : self.resuljug+="1"
            elif keydown[K_KP2]:
                if self.primer :
                    self.resuljug = "2"
                    self.primer = 0   
                else : self.resuljug+="2"
            elif keydown[K_KP3]:
                if self.primer :
                    self.resuljug = "3"
                    self.primer = 0   
                else : self.resuljug+="3"
            elif keydown[K_KP4]:
                if self.primer :
                    self.resuljug = "4"
                    self.primer = 0   
                else : self.resuljug+="4"
            elif keydown[K_KP5]:
                if self.primer :
                    self.resuljug = "5"
                    self.primer = 0   
                else : self.resuljug+="5"
            elif keydown[K_KP6]:
                if self.primer :
                    self.resuljug = "6"
                    self.primer = 0   
                else : self.resuljug+="6"
            elif  keydown[K_KP7]:
                if self.primer :
                    self.resuljug = "7"
                    self.primer = 0   
                else : self.resuljug+="7"
            elif  keydown[K_KP8]:
                if self.primer :
                    self.resuljug = "8"
                    self.primer = 0   
                else : self.resuljug+="8"
            elif  keydown[K_KP9]:
                if self.primer :
                    self.resuljug = "9"
                    self.primer = 0   
                else : self.resuljug+="9"           
           

        if  keydown[K_KP_PERIOD]:
            self.resuljug = "?"
            self.primer = 1
            
        if  keydown[K_KP_ENTER]:
            self.Resultado()
            self.NuevaPregunta()
    def ActualizarMBoton(self):
        
        
                
        
        if self.sonar == 1:
            for n in range(12):
                if self.panel.boton[n].Colisiona(raton):
                    self.sclick.play()
                    self.sonar = 0
        
        if len(self.resuljug) <= 1:
            if self.panel.boton[9].Colisiona(raton):                
                if self.primer ==1:
                    self.resuljug = "0"                    
                    self.primer = 0   
                else : self.resuljug+="0"
            if self.panel.boton[0].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "1"
                    self.primer = 0   
                else : self.resuljug+="1"
            if self.panel.boton[1].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "2"
                    self.primer = 0   
                else : self.resuljug+="2"
            if self.panel.boton[2].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "3"
                    self.primer = 0   
                else : self.resuljug+="3"
            if self.panel.boton[3].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "4"
                    self.primer = 0   
                else : self.resuljug+="4"
            if self.panel.boton[4].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "5"
                    self.primer = 0   
                else : self.resuljug+="5"
            if self.panel.boton[5].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "6"
                    self.primer = 0   
                else : self.resuljug+="6"
            if self.panel.boton[6].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "7"
                    self.primer = 0   
                else : self.resuljug+="7"
            if self.panel.boton[7].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "8"
                    self.primer = 0   
                else : self.resuljug+="8"
            if self.panel.boton[8].Colisiona(raton):
                if self.primer ==1:
                    self.resuljug = "9"
                    self.primer = 0   
                else : self.resuljug+="9"           
           

        if self.panel.boton[10].Colisiona(raton):
            self.resuljug = "?"
            self.primer = 1
            
        if self.panel.boton[11].Colisiona(raton):
            self.Resultado()            
            self.NuevaPregunta()    
    

       
