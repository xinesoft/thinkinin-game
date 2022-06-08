from xs import *
import sys,record,xs
from comienzo import Comienzo
from panel import Panel
from graficos import pizarra,click
import puntuacion
class Monedas2:
    def __init__(self):  
        pantalla.Color((200,200,200))   
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))   
        self.puntuacion = 0
        self.monedas = {}
        self.pizarra = Graficos("img/menu/pizarra.png",pantalla.Ancho()/2,142)
        self.cuadrado = Graficos("img/monedas/cuadrado2.png",pantalla.Ancho()/2,180)
        self.salire = 0
        self.tiza = Fuentes("fonts/tiza.ttf",30)
        self.tiza.SetColor(255, 255, 255)
        self.fuente = Fuentes("fonts/fuente.ttf",40)
        self.fuente.SetColor(255,0,0)
        self.segundos = 60
        self.segund = Timer(1000)
        
        self.sclick = click
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
        pass
    def DibujarResultado(self):
           
          if xs.modo == 0:
              record.Cargar(3,self.puntuacion) 
          else:
              if self.puntuacion >= 15 : self.resex = 2.0
              else : self.resex = float(self.puntuacion*2)/15 
              puntuacion.examen += self.resex
          self.salir = 1
    def AsignarDificultad(self):
        if self.puntuacion <= 2 :
            self.columnas = 1
        elif self.puntuacion == 3 :
            self.columnas = 2
        elif self.puntuacion == 5 :
            self.columnas = 3
        elif self.puntuacion == 8 :
            self.columnas = 4
        elif self.puntuacion == 11 :
            self.columnas = 5
        elif self.puntuacion == 14 :
            self.columnas = 6
    def Resultado(self):

        if self.resultadomac != self.resuljug:
            if self.puntuacion > 0: self.puntuacion-=1

        else : self.puntuacion+=1
    def ActualizarMBoton(self):
        
        
       
        if self.sonar == 1:
            for n in range(12):
                if self.panel.boton[n].Colisiona(raton):
                    self.sclick.play()
                    self.sonar = 0
        
        if len(str(self.resuljug)) <= len(str(self.resultadomac)):
            if self.panel.boton[9].Colisiona(raton):
                
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-0"

                    else  : self.resuljug = "0"
                    self.primer = 0   
                else : self.resuljug+="0"
            elif self.panel.boton[0].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-1"

                    else  : self.resuljug = "1"
                    self.primer = 0   
                else : self.resuljug+="1"
            elif self.panel.boton[1].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-2"

                    else  : self.resuljug = "2"
                    self.primer = 0   
                else : self.resuljug+="2"
            elif self.panel.boton[2].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-3"

                    else  : self.resuljug = "3"
                    self.primer = 0   
                else : self.resuljug+="3"
            elif self.panel.boton[3].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-4"

                    else  : self.resuljug = "4"
                    self.primer = 0   
                else : self.resuljug+="4"
            elif self.panel.boton[4].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-5"

                    else  : self.resuljug = "5"
                    self.primer = 0   
                else : self.resuljug+="5"
            elif self.panel.boton[5].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-6"

                    else  : self.resuljug = "6"
                    self.primer = 0   
                else : self.resuljug+="6"
            elif self.panel.boton[6].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-7"

                    else  : self.resuljug = "7"
                    self.primer = 0   
                else : self.resuljug+="7"
            elif self.panel.boton[7].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-8"

                    else  : self.resuljug = "8"
                    self.primer = 0   
                else : self.resuljug+="8"
            elif self.panel.boton[8].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < str(0):
                        self.resuljug = "-9"

                    else  : self.resuljug = "9"
                    self.primer = 0   
                else : self.resuljug+="9"           
           

        if self.panel.boton[10].Colisiona(raton):
            self.resuljug = "?"
            self.primer = 1
            
        if self.panel.boton[11].Colisiona(raton):
            self.Resultado()
            self.NuevaPregunta()        
    def Dibujar(self):
        
            if self.comienzo.segundo == 0:
                raton.Dibujar()
            Update()       
                            
            for event in pygame.event.get():             
               
                if event.type == MOUSEMOTION:
                    raton.Posicionar()
                if self.comienzo.segundo == 0:
                    if event.type == MOUSEBUTTONDOWN:
                        mousebutton = pygame.mouse.get_pressed()
                        if mousebutton[0] :
                           self.ActualizarMBoton()                        
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            if xs.modo == 1:
                                            self.salire = 1
                            self.salir = 1
                        self.ActualizarKBoton()
            self.pizarra.Dibujar(1)
            self.cuadrado.Dibujar(1)
            self.panel.Dibujar()
            if self.comienzo.segundo == 0:
                for c in range(2):    
                    for f in range(self.columnas):                     
                        self.monedas[c][f].Dibujar(0)
            if xs.IDIOMA == 0:
                self.tiza.Dibujar("Puntuacion:",100,25,1,0)
                self.tiza.Dibujar("Resultado:",270,25,1,0)
                self.tiza.Dibujar("TiEmpo:",450,25,1,0)
            else :
                self.tiza.Dibujar("  ScorE:",100,25,1,0)
                self.tiza.Dibujar("  REsult:",270,25,1,0)
                self.tiza.Dibujar(" TimE:",450,25,1,0)
            
            self.fuente.Dibujar(self.puntuacion,170,85,1,1)
            
            
            self.fuente.Dibujar(self.resuljug,pantalla.Ancho()/2+15,85,1,1)
            
            
            self.fuente.Dibujar(self.segundos,495,85,1,1)
            if self.comienzo.segundo == 0:
                if self.segund.EndLoop():
                    self.segundos-=1
                    if self.segundos == -1:
                        self.DibujarResultado() 
            
            
        
    def NuevaPregunta(self):
        
        self.resultadomac = 0
        
        self.primer = 1
       
        posx = 140
        posy = 118
        self.AsignarDificultad()
        for c in range(2):
            self.monedas[c] = {}   
            for f in range(self.columnas):
                num = choice((1,5,10,50))
                grafico = "img/monedas/%d.gif" % num
                self.resultadomac += num                   
                    
                self.monedas[c][f] = Graficos(grafico) 
                self.monedas[c][f].Transparencia((255,255,255))
                                            
                self.monedas[c][f].Posicion(posx,posy)                        
                posx += 61 
            posx = 140 
            posy+=61
                
        self.resultadomac = str(self.resultadomac)
        self.resuljug = "?"
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
                
        if len(str(self.resuljug)) <= len(str(self.resultadomac)):
            if  keydown[K_KP0]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-0"

                    else  : self.resuljug = "0"
                    self.primer = 0   
                else : self.resuljug+="0"
            elif keydown[K_KP1]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-1"

                    else  : self.resuljug = "1"
                    self.primer = 0   
                else : self.resuljug+="1"
            elif keydown[K_KP2]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-2"

                    else  : self.resuljug = "2"
                    self.primer = 0   
                else : self.resuljug+="2"
            elif keydown[K_KP3]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-3"

                    else  : self.resuljug = "3"
                    self.primer = 0   
                else : self.resuljug+="3"
            elif keydown[K_KP4]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-4"

                    else  : self.resuljug = "4"
                    self.primer = 0   
                else : self.resuljug+="4"
            elif keydown[K_KP5]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-5"

                    else  : self.resuljug = "5"
                    self.primer = 0   
                else : self.resuljug+="5"
            elif keydown[K_KP6]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-6"

                    else  : self.resuljug = "6"
                    self.primer = 0   
                else : self.resuljug+="6"
            elif  keydown[K_KP7]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-7"

                    else  : self.resuljug = "7"
                    self.primer = 0   
                else : self.resuljug+="7"
            elif  keydown[K_KP8]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-8"

                    else  : self.resuljug = "8"
                    self.primer = 0   
                else : self.resuljug+="8"
            elif  keydown[K_KP9]:
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-9"

                    else  : self.resuljug = "9"
                    self.primer = 0   
                else : self.resuljug+="9"           
           

        if  keydown[K_KP_PERIOD]:
            self.resuljug = "?"
            self.primer = 1
            
        if  keydown[K_KP_ENTER]:
            self.Resultado()
            self.NuevaPregunta()
