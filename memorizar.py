import sys,xs
import panel
from xs import *
from random import randint
from comienzo import Comienzo
import record
import puntuacion

class Memorizar:
    def __init__(self):
        pantalla.Color((200,200,200))
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))

        self.pizarra = Graficos("img/menu/pizarra.png",pantalla.Ancho()/2,142)
        self.tiza = Fuentes("fonts/tiza.ttf",100)
        self.tiza.SetColor(255, 255, 255)
        self.tiza2 = Fuentes("fonts/tiza.ttf",30)
        self.tiza2.SetColor(255, 255, 255)
        self.fuente3 = Fuentes("fonts/fuente.ttf",40)
        self.fuente3.SetColor(255,0,0)
        self.salire = 0
        self.sclick = Sonido("musica/click.ogg")
        
        self.timers = Timer(1000)
       
        self.segund = Timer(1000)
        
        self.numero = {}
        self.resultadomac = ""
        self.dificultad = 3
        self.sonar = 1
       
        self.primer = 1
        self.introducir = 0
        self.resuljug = "_"
        self.puntuacion = 0
        self.segundos = 60
        self.panel = panel.Panel()
        self.comienzo = Comienzo()
        
        while self.comienzo.segundo >= 1: 
            self.comienzo.Dibujar()
            self.Dibujar()
        self.NuevaPregunta()
        self.panel.comienzo = 1
        self.salir = False
        while not self.salir : 
            
                self.Dibujar()
    
    def Resultado(self):
        if str(self.resuljug) == self.resultadomac:
            self.puntuacion += 1
        elif self.puntuacion > 0:
            self.puntuacion -= 1
        pass
    def AsignarDificultad(self):
        if self.puntuacion >= 1 :
            self.dificultad = 3
        if self.puntuacion >= 3 :
            self.dificultad = 4
        if self.puntuacion >= 6 :
            self.dificultad = 5
        if self.puntuacion >= 10 :
            self.dificultad = 6
          
    def Dibujar(self):
        if self.comienzo.segundo == 0:
            raton.Dibujar()
        Update()
        for event in pygame.event.get():
            
            if event.type == MOUSEMOTION:
                    raton.Posicionar()
            if self.comienzo.segundo == 0:    
                if event.type == KEYDOWN :
                    if self.timers.End():
                                    self.ActualizarKBoton()
                    if event.key == K_ESCAPE:
                        if xs.modo == 1:
                                            self.salire = 1
                        self.salir = 1
                if event.type == MOUSEBUTTONDOWN:
                                   
                                        mousebutton = pygame.mouse.get_pressed()
                                        if mousebutton[0] :
                                            if self.timers.End():
                                                self.ActualizarMBoton()
                if event.type == MOUSEBUTTONUP or event.type == KEYUP:
                                    self.sonar = 1
       
            
        self.panel.Dibujar()
        self.pizarra.Dibujar(1)
        
        if self.comienzo.segundo == 0:                          
                if not self.timers.End() :               
                     
                    self.tiza.Dibujar(self.resultadomac,pantalla.Ancho()/2,180,1,1)
                else :
                    self.tiza.Dibujar(self.resuljug,pantalla.Ancho()/2,180,1,1)
        if xs.IDIOMA == 0:
            self.tiza2.Dibujar("Puntuacion:",140,25,1,0)
            self.tiza2.Dibujar("TiEmpo:",410,25,1,0)
        else :
            self.tiza2.Dibujar("  ScorE:",140,25,1,0)
            self.tiza2.Dibujar(" TimE:",410,25,1,0)
        
        self.fuente3.Dibujar(self.puntuacion,210,85,1,1)        
        self.fuente3.Dibujar(self.segundos,455,85,1,1)
            
        if self.comienzo.segundo == 0:
                
            if self.segund.EndLoop():
                self.segundos-=1
                if self.segundos == -1:                    
                    self.DibujarResultado()     
            
    
    def NuevaPregunta(self):            
                         
        self.AsignarDificultad()
        self.resultadomac  = ""
        self.resuljug = "_"
        self.primer = 1
        for n in range(self.dificultad):
            self.numero[n] = randint(0,9)
            self.resultadomac += str(self.numero[n])
        
        self.timers.ResetTimeBase()
        
    
                
        
    def DibujarResultado(self):
           
          if xs.modo == 0:
              record.Cargar(7,self.puntuacion) 
          else:
              if self.puntuacion >= 20 : self.resex = 2.0
              else : self.resex = float(self.puntuacion*2)/20 
              puntuacion.examen += self.resex
          self.salir = 1
                   
             
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
                
        if len(self.resuljug) <= self.dificultad-1:
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
            self.resuljug = "_"
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
        
        if len(self.resuljug) <= self.dificultad-1:
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
            self.resuljug = "_"
            self.primer = 1
            
        if self.panel.boton[11].Colisiona(raton):
            self.Resultado()            
            self.NuevaPregunta()    
    

