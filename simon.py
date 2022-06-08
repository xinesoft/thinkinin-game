from random import randint,choice
from graficos import *
from comienzo import Comienzo
from xs import *
import sys,record,xs
import puntuacion

class Simon:    
    
    def __init__(self):
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))

        self.tiza = Fuentes("fonts/tiza.ttf",30)
        self.tiza.SetColor(255, 255, 255)     
        self.fuente = Fuentes("fonts/fuente.ttf",40)
        self.fuente.SetColor(255,0,0)
        self.base = Graficos("img/simon/simon.png",pantalla.Ancho()/2,pantalla.Alto()/2)
        self.pulsar = {}
        self.actu = 0
        self.pulsar[0] = Graficos("img/simon/rojo.png",187,108)
        self.pulsar[1] = Graficos("img/simon/verde.png",322,108)
        self.pulsar[2] = Graficos("img/simon/azul.png",187,242)
        self.pulsar[3] = Graficos("img/simon/amarillo.png",322,242)
        self.resulmac = []
        self.principio = 1
        self.salire = 0
        self.puls = 1
        self.sonar= 1
        self.sonarm = 1
        self.segundos = 60
        self.pierde = 0
        self.puntuacion = 0        
        self.dificultad = 3     
        
        self.sonidos = Sonido("musica/simon/0.wav") ,Sonido("musica/simon/1.wav"),\
                       Sonido("musica/simon/2.wav") ,Sonido("musica/simon/3.wav")   
         
         
        
        self.segund = Timer(1000)
        
        self.comienzo = Comienzo()
        
        self.NuevaPregunta()
        self.segundo = Timer(1000)
        self.activ = 0
        while self.comienzo.segundo >= 1: 
            self.comienzo.Dibujar()
            self.Dibujar()
        
        self.salir = False
        Musica.play()     
        self.NuevaPregunta()
        self.activ = 1
        self.segundo = Timer(1000)
        while not self.salir : 
            self.Dibujar()
    def DibujarResultado(self):
           
          if xs.modo == 0:
              record.Cargar(9,self.puntuacion) 
          else:
              if self.puntuacion >= 15 : self.resex = 2.0
              else : self.resex = float(self.puntuacion*2)/15 
              puntuacion.examen += self.resex
          self.salir = 1
         
    def NuevaPregunta(self):
       
        if self.principio == 2:                
                self.resulmac.append(choice(range(4)))
                                
        if self.principio == 2:
           self.principio ==3
            
        if self.principio == 1:
            for x in range(self.dificultad):
                self.resulmac.append(choice(range(4)))
                
            self.principio = 2
         
            
        self.resuljug = []
        self.pos = 0
        self.timer = Timer(700)
        self.timer2 = Timer(400)
        self.timer3 = Timer(400)
        
        
            
        
        self.inicio = 1
        self.nact = 0
       
    def Resultado(self):
        if self.resuljug[:self.dificultad-1] == self.resulmac[:self.dificultad-1]:
            self.puntuacion += 1
            self.dificultad += 1
        elif self.puntuacion > 0:
            self.puntuacion -= 1
            self.dificultad -= 1
            self.pierde = 1
     
        
    def Dibujar(self):   
        if self.segundo.End():
            if self.activ == 1:
                self.NuevaPregunta()
                self.activ = 0     
        
        Update()       
                            
        for event in pygame.event.get():           
            
            if event.type == MOUSEMOTION:
                raton.Posicionar()
            if self.comienzo.segundo == 0:
                if event.type == KEYDOWN :
                                        if event.key == K_ESCAPE:
                                                self.salir = 1
                                                if xs.modo == 1:
                                                    self.salire = 1
                if event.type == MOUSEBUTTONUP:
                    self.sonar = 1
                    
                if event.type == MOUSEBUTTONDOWN:
                        mousebutton = pygame.mouse.get_pressed()
                        if mousebutton[0] :
                            if self.inicio == 2:
                                if self.puls == 1:
                                    for n in range(4):
                                        if self.pulsar[n].Colisiona(raton):
                                            self.nact =  n
                                            self.resuljug.append(n)
                                            if self.sonar == 1:
             
                                                self.sonidos[self.nact].play()
                                                self.sonar = 0
                
                                            self.pos += 1
                                            self.timer3 = Timer(400)
                                    self.puls = 0
                            
        pizarra.Dibujar(1)
        self.base.Dibujar(1)
        
        if self.timer3.End(): self.puls = 1
        
        if self.comienzo.segundo == 0 and self.segundo.End():
            
                if self.inicio == 1:
                    
                    if self.timer.EndLoop():             
                        self.sonarm = 1
                        self.timer2.ResetTimeBase()
                       
                       
                        if self.nact == self.dificultad -1 :
                            self.inicio = 2                
                            self.pos = 0     
                                           
                        else : self.nact += 1 
                    elif not self.timer2.End():
                            if self.nact != self.dificultad :   
                                if self.sonarm == 1:
                                    self.sonidos[self.resulmac[self.nact]].play()
                                    self.sonarm = 0  
                                self.pulsar[self.resulmac[self.nact]].Dibujar()
                    
                        
                    
                    
                if self.inicio == 2:
                
                    if not self.timer3.End():        
                                             
                                   
                        self.pulsar[self.nact].Dibujar()
                        
                    elif self.pos == self.dificultad:
                        self.Resultado() 
                        self.timer2.ResetTimeBase()
                        self.inicio = 3                   
                if self.inicio == 3:
                    if self.timer2.End():
                        self.NuevaPregunta()
             
                    
            
        
        if xs.IDIOMA == 0:          
                self.tiza.Dibujar("Puntuacion:",140,40,1,0)            
                self.tiza.Dibujar("TiEmpo:",410,40,1,0)
        else :
                self.tiza.Dibujar("  ScorE:",140,40,1,0)
                self.tiza.Dibujar(" TimE:",410,40,1,0)
            
        self.fuente.Dibujar(self.puntuacion,210,100,1,1)
        self.fuente.Dibujar(self.segundos,455,100,1,1)
        
        if self.comienzo.segundo == 0 :
            
                if self.inicio != 1:    
                    if self.segund.EndLoop() and self.segundo.End():
                        self.segundos-=1
                        if self.segundos == -1:                    
                            self.DibujarResultado()
                raton.Dibujar()
             
