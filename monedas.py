import sys,xs
from xs import *
from random import *
import puntuacion
import graficos

from comienzo import Comienzo
import record


class Monedas(Comienzo):
    
    def __init__(self):
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))
        self.segund = Timer(1000)
        self.salire = 0
        self.pizarra = Graficos("img/menu/bpizarra.png",pantalla.Ancho()/2,pantalla.Alto()/2)
        
        
        self.sclick = graficos.click
        self.sover = graficos.clack
        
        self.cuadrado1 = Graficos("img/monedas/cuadrado.png")
        self.cuadrado1.Posicion(pantalla.Ancho()/3.5,pantalla.Alto()/2+23) 
        self.cuadrado2 = Graficos("img/monedas/cuadrado.png")
        self.cuadrado2.Posicion((pantalla.Ancho()/3.5)*2.5,pantalla.Alto()/2+23)   
        
        self.tiza = Fuentes("fonts/tiza.ttf",30)
        self.tiza.SetColor(255, 255, 255)
        self.fuente = Fuentes("fonts/fuente.ttf",40)
        self.fuente.SetColor(255,0,0)
        self.segundos = 60
        
        self.columnas = 2

        
        self.puntuacion = 0
        
        self.monedas = {}           
        self.sonar = 1
        self.sonar2 = 1
        
        pantalla.Color((200,200,200))
        self.comienzo = Comienzo()
        
        self.NuevaPregunta()
        while self.comienzo.segundo >= 1: 
            self.comienzo.Dibujar()
            self.Dibujar()
        self.salir = False
        Musica.play()
        while not self.salir : 
            self.Dibujar()
            
            
            
            
            
        
        
 
    def DibujarResultado(self):
        if xs.modo == 0:
          record.Cargar(2,self.puntuacion) 
        else:
          if self.puntuacion >= 50 : self.resex = 2.0
          else : self.resex = float(self.puntuacion*2)/50 
          puntuacion.examen += self.resex
                   
        self.salir = 1
    
    def AsignarDificultad(self):
        if self.puntuacion <= 2 :
            self.columnas = 2
        elif self.puntuacion == 3 :
            self.columnas = 3
        elif self.puntuacion == 7 :
            self.columnas = 4
        elif self.puntuacion == 10 :
            self.columnas = 5
        
      
    def NuevaPregunta(self):
        
        self.resultado1 = 0
        self.resultado2 = 0
        
        posx = 89
        posy = 109
        self.AsignarDificultad()
        for c in range(self.columnas):
            self.monedas[c] = {}   
            for f in range(3):
                num = choice((1,5,10,50))
                grafico = "img/monedas/%d.gif" % num
                self.resultado1 += num
                    
                    
                self.monedas[c][f] = Graficos(grafico) 
                self.monedas[c][f].Transparencia((255,255,255))
                                            
                self.monedas[c][f].Posicion(posx,posy)                        
                posx += 61   
            posx = 89 
            posy+=61
        self.monedas2 = {} 
        posx = 640 -92-61*3
        posy = 109
        for c in range(self.columnas):
            self.monedas2[c] = {}   
            for f in range(3):    
                num = choice((1,5,10,50))
                grafico = "img/monedas/%d.gif" % num
                self.resultado2 += num
                            
                self.monedas2[c][f] = Graficos(grafico)   
                self.monedas2[c][f].Transparencia((255,255,255))                            
                self.monedas2[c][f].Posicion(posx,posy)                        
                posx += 61  
            posx = 640 -92-61*3
            posy+=61
        
   
    def Dibujar(self): 
            if self.comienzo.segundo == 0:
                raton.Dibujar()
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
                    if event.type == MOUSEBUTTONDOWN:
                        mousebutton = pygame.mouse.get_pressed()
                        if mousebutton[0] :
                            if self.cuadrado1.Colisiona(raton) :
                                self.sclick.play()
                                if self.resultado1 > self.resultado2 :                            
                                    self.puntuacion += 1                                
                                elif self.puntuacion > 0 : self.puntuacion -= 1                           
                                
                                self.NuevaPregunta()
                                
                            elif self.cuadrado2.Colisiona(raton) :
                                self.sclick.play()
                                if self.resultado2 > self.resultado1 :                            
                                    self.puntuacion += 1
                                elif self.puntuacion > 0 : self.puntuacion -= 1                            
                               
                                self.NuevaPregunta()                                                      
                                                   
                                             
            self.pizarra.Dibujar(1)
            self.cuadrado1.Dibujar(1)
            self.cuadrado2.Dibujar(1)
            if xs.IDIOMA == 0:
                self.tiza.Dibujar("Puntuacion:",85, 40,1,0)
                self.tiza.Dibujar("TiEmpo:",383, 40,1,0)
            else :
                self.tiza.Dibujar("     ScorE:",85, 40,1,0)
                self.tiza.Dibujar("  TimE:",383, 40,1,0)
            
            self.fuente.Dibujar(self.puntuacion,263,66,1,1)        
            
            
            self.fuente.Dibujar(self.segundos,520,66,1,1) 
            if self.comienzo.segundo == 0:
                
                for c in range(self.columnas):    
                    for f in range(3):
                     
                        self.monedas[c][f].Dibujar(0)
                        self.monedas2[c][f].Dibujar(0)    
            
            
            
            
                if self.segund.EndLoop():
                    self.segundos-=1
                    if self.segundos == -1:
                        self.DibujarResultado() 
                if self.cuadrado1.Colisiona(raton) or  self.cuadrado2.Colisiona(raton):
                    if self.sonar == 1:
                        self.sover.play()
                        self.sonar = 0
                else : self.sonar = 1
                
       
