import pygame,sys
from graficos import *

from practicas import Practicas
from opciones import Opciones
from examen import Examen
from pygame.locals import *
from xs import *
import xs

class Menu:
    
    def Cargar(self):
        if xs.IDIOMA == 0:
            self.texto11 = "Aumente su puntuación practicando."
            self.texto22 = "Examen con 5 pruebas al azar."
            self.texto33 = "Configure las opciones del juego."
            self.texto44 = "¿ Quiere salir del juego ?."
        else :
            self.texto11 = "Increase your score practicing."
            self.texto22 = "Exam whit 5 randoms tests."
            self.texto33 = "Set the game options."
            self.texto44 = "Do you wanna leave the game?."
            
        
        
        
        self.bpracticas0 = Graficos("img/menu/%s/bpracticas1.png"%xs.IDIOMA)
        self.bpracticas0.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2)         
        self.bexamen0 = Graficos("img/menu/%s/bexamen1.png"%xs.IDIOMA)  
        self.bexamen0.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2+50)      
        self.bopciones0 = Graficos("img/menu/%s/bopciones1.png"%xs.IDIOMA)
        self.bopciones0.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2+100)
        self.bsalir0 = Graficos("img/menu/%s/bsalir1.png"%xs.IDIOMA) 
        self.bsalir0.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2+150)

        self.bpracticas1 = Graficos("img/menu/%s/bpracticas2.png"%xs.IDIOMA)
        self.bpracticas1.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2)         
        self.bexamen1 = Graficos("img/menu/%s/bexamen2.png"%xs.IDIOMA)  
        self.bexamen1.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2+50)      
        self.bopciones1 = Graficos("img/menu/%s/bopciones2.png"%xs.IDIOMA)
        self.bopciones1.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2+100)
        self.bsalir1 = Graficos("img/menu/%s/bsalir2.png"%xs.IDIOMA) 
        self.bsalir1.Posicion(pantalla.Ancho()/2-125,pantalla.Alto()/2+150)
        self.texto1actual = 0
        self.texto1max = len(self.texto11)
        self.texto2actual = 0
        self.texto2max = len(self.texto22)
        self.texto3actual = 0
        self.texto3max = len(self.texto33)
        self.texto4actual = 0
        self.texto4max = len(self.texto44)
        self.tiza.Color((255,255,255))
        self.texto1 = ""
        self.texto2 = ""
        self.texto3 = ""
        self.texto4 = ""
        self.idioma = xs.IDIOMA
        
    def __init__(self):
        menumus.play(-1)
        
        self.blogo = Graficos("img/menu/logo.png")
        self.blogo.Posicion(pantalla.Ancho()/2,100)
        
        
        self.tiza = Fuentes("fonts/fuente.ttf",12)
        self.Cargar()
        
        
        
           
        
        self.sonar3 = 1
        self.sonar2 = 1
        self.sonar1 = 1
        self.sonar = 1
        
        self.animar = 0
        
        self.savance = clack
        self.sretorno = click
        pantalla.Color((200,200,200))
        
        
        
        done = False
        
        while not done :
            for event in pygame.event.get():
              
                if event.type == MOUSEMOTION:
                    raton.Posicionar()                    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE :
                        done = 1                    
                    
                if event.type == MOUSEBUTTONDOWN: 
                      
                    mousebutton = pygame.mouse.get_pressed()
                    if mousebutton[0] == 1:
                        if self.bpracticas0.Colisiona(raton):
                            
                            self.sretorno.play()
                            practicas = Practicas()
                            del practicas
                            self.sretorno.play()
                            
                        elif self.bexamen0.Colisiona(raton):
                                                        
                            self.sretorno.play() 
                            examen = Examen()
                            del examen                           
                            self.sretorno.play()
                        elif self.bopciones0.Colisiona(raton):
                            self.sretorno.play()
                            opciones = Opciones()  
                            del opciones
                            if xs.IDIOMA != self.idioma :
                                self.Cargar()
                        elif self.bsalir0.Colisiona(raton):                            
                            done = 1
                 
            
            
            
            
            pizarra.Dibujar(1)
            self.blogo.Dibujar(1)  
            comentario.Dibujar() 
            if self.animar == 0:                
                    caracol.Animar(200)
            else :
                
                caracolhabla.Animar(200)
                
            self.animar = 0
                
            if self.bpracticas0.Colisiona(raton):                
                if self.sonar == 1:
                        self.savance.play()
                        self.sonar = 0 
                                    
                self.bpracticas1.Dibujar(1)
                
                self.tiza.Dibujar(self.texto1,315,190,1)
                if self.texto1actual != self.texto1max:
                    self.texto1 += self.texto11[self.texto1actual]
                    self.texto1actual +=1
                self.animar = 1  
            else : 
                self.bpracticas0.Dibujar(1)
                self.texto1actual = 0
                self.texto1 = ""
                self.sonar = 1
            
            if self.bexamen0.Colisiona(raton):
                if self.sonar1 == 1:
                        self.savance.play()
                        self.sonar1 = 0  
                self.bexamen1.Dibujar(1)
                self.tiza.Dibujar(self.texto2,315,190,1)
                if self.texto2actual != self.texto2max:
                    self.texto2 += self.texto22[self.texto2actual]
                    self.texto2actual +=1
                self.animar = 1  
                
            else : 
                self.bexamen0.Dibujar(1) 
                self.sonar1 = 1
                self.texto2actual = 0
                self.texto2 = ""
                        
            if self.bopciones0.Colisiona(raton):
                if self.sonar2 == 1:
                        self.savance.play()
                        self.sonar2 = 0  
                self.bopciones1.Dibujar(1)
                self.tiza.Dibujar(self.texto3,315,190,1)
                if self.texto3actual != self.texto3max:
                    self.texto3 += self.texto33[self.texto3actual]
                    self.texto3actual +=1
                self.animar = 1  
            else :
                self.texto3actual = 0
                self.texto3 = ""
                self.bopciones0.Dibujar(1)
                self.sonar2 = 1
             
            if self.bsalir0.Colisiona(raton):
                if self.sonar3 == 1:
                        self.savance.play()
                        self.sonar3 = 0  
                self.bsalir1.Dibujar(1)
                self.tiza.Dibujar(self.texto4,315,190,1)
                if self.texto4actual != self.texto4max:
                    self.texto4 += self.texto44[self.texto4actual]
                    self.texto4actual +=1
                self.animar = 1  
            else :
                self.bsalir0.Dibujar(1)      
                self.sonar3 = 1
                self.texto4actual = 0
                self.texto4 = ""
            
             
                  
            raton.Dibujar()
            Update()
            

          
