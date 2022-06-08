import sys,xs
import panel
from xs import *
from random import randint
from comienzo import Comienzo
import record
import puntuacion
import graficos


class Calculo2:
    def __init__(self):
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))
        self.puntuacion = 0
        self.salire = 0
        self.signos = ["+","-","*","/"]   
        self.signoc = "_"     
        self.RMAX = 2
        self.segundos = 60
        self.dificultad = 0
        self.sonar = 1
        self.activado = 0
        self.resultadomac = 0
        salir = 0
        
        self.sclick = graficos.click
        pantalla.Color((200,200,200))
        
        self.panel = panel.Panel2()
        
        self.tiza = Fuentes("fonts/tiza.ttf",50)
        self.tiza.SetColor(255, 255, 255)
        self.tiza2 = Fuentes("fonts/tiza.ttf",30)
        self.tiza2.SetColor(255, 255, 255)
        self.fuente3 = Fuentes("fonts/fuente.ttf",40)
        self.fuente3.SetColor(255,0,0)
        self.timeresul = Timer(0)
                
        self.pizarra = Graficos("img/menu/bpizarra.png",pantalla.Ancho()/2,240)
       
        
        self.segund = Timer(1000)
        self.timer4 = Timer(4000)
        
        self.comienzo = Comienzo()
        
        self.NuevaPregunta()
        while self.comienzo.segundo >= 1: 
            self.comienzo.Dibujar()
            self.Dibujar()
        self.panel.comienzo = 1        
        self.salir = False
        Musica.play(-1)
        while not self.salir : 
            
                self.Dibujar()
        
    
    def DibujarTiza(self):
        if self.comienzo.segundo == 0:           
           if (self.dificultad == 0):
                self.tiza.Dibujar(self.num1,pantalla.Ancho()/2-100,210,1,1)
                self.tiza.Dibujar(self.signoc,pantalla.Ancho()/2-50,210,1,1)
                self.tiza.Dibujar(self.num2,pantalla.Ancho()/2,210,1,1)
                self.tiza.Dibujar("=",pantalla.Ancho()/2+50,210,1,1)
                self.tiza.Dibujar(self.resultadomac,pantalla.Ancho()/2+105,210,1,1)







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
                                if xs.modo == 1:
                                            self.salire = 1
                                self.salir = 1
                        if event.type == MOUSEBUTTONDOWN:
                            
                            mousebutton = pygame.mouse.get_pressed()
                            if mousebutton[0] :
                                self.ActualizarMBoton()
                        if event.type == MOUSEBUTTONUP or event.type == KEYUP:
                            self.sonar = 1
            
            
            
            self.pizarra.Dibujar(1)
            self.panel.Dibujar()
            self.DibujarTiza()
            
            
            if self.timeresul.End():   
                  if self.activado == 1:
                    self.Resultado()
                    self.NuevaPregunta()
                    
                    self.activado = 0
                   
            
                
                    
                    
                                
            if xs.IDIOMA == 0:          
                self.tiza2.Dibujar("Puntuacion:",140,40,1,0)            
                self.tiza2.Dibujar("TiEmpo:",410,40,1,0)
            else :
                self.tiza2.Dibujar("  ScorE:",140,40,1,0)
                self.tiza2.Dibujar(" TimE:",410,40,1,0)
            
            self.fuente3.Dibujar(self.puntuacion,210,100,1,1)
            self.fuente3.Dibujar(self.segundos,455,100,1,1)
            
            if self.comienzo.segundo == 0:
                
                if self.segund.EndLoop():
                    self.segundos-=1
                    if self.segundos == -1:
                        self.DibujarResultado()

    def NuevaPregunta(self):
        
           
            self.signoc = "_"
            self.num1 = randint(3,10)
            self.num2 = randint(2,10)
            self.num3 = randint(3,10)
            self.resultadomac = 0
            self.signo = randint(0,3)            
            
            if self.dificultad == 0:
                if self.signo == 0:
                    self.resultadomac = self.num1 + self.num2
                    
                    
                if self.signo == 1 :
                    self.resultadomac = self.num1 - self.num2
                    
                if self.signo == 2 :
                    self.resultadomac = self.num1 * self.num2
                   
                if self.signo == 3 :                   
                    while self.num2 == 0:
                            self.num2 = randint(1,10)
                    while self.num1 % self.num2 != 0 :
                            
                             self.num1 = randint(1,10)
                             self.num2 = randint(1,10)
                    while self.num2 == 0:
                            self.num2 = randint(1,10)
                        
                    self.resultadomac = self.num1 / self.num2
                                                                        

            
            
            
    def ActualizarMBoton(self):
        for n in range(4):
            if self.panel.boton[n].Colisiona(raton):
                self.signor = n
                self.signoc = self.signos[n]
                self.activado = 1
                
                self.timeresul = Timer(300)
                
                
    def Resultado(self):
        if self.activado == 1:
            if self.signo  != self.signor :
                if self.puntuacion > 0: self.puntuacion-=1
    
            else :                
                    self.puntuacion+=1
           
        
    
        
    def DibujarResultado(self):
        if xs.modo == 0:
          record.Cargar(1,self.puntuacion) 
        else:
          if self.puntuacion >= 25 : self.resex = 2.0
          else : self.resex = float(self.puntuacion*2)/25 
          puntuacion.examen += self.resex
                   
        self.salir = 1
          


