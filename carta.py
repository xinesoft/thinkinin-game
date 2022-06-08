import sys,xs
from xs import *
from random import *
from parejas import Casilla
from comienzo import Comienzo
import graficos
import record
import puntuacion


class Carta:
    timer = Timer(300) 
    def __init__(self):
        pantalla.Color((200,200,200))
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))
        self.pizarra = Graficos("img/menu/bpizarra.png")
        self.pizarra.Posicion(pantalla.Ancho()/2,pantalla.Alto()/2)
        self.tiza = Fuentes("fonts/tiza.ttf",30)
        self.tiza.SetColor(255, 255, 255)
        self.fuente = Fuentes("fonts/fuente.ttf",40)
        self.fuente.SetColor(255,0,0)
        self.segund = Timer(1000)
        self.salire = 0        
        self.clicka  = 1
        self.puntuacion = 0
        self.segundos = 60
        self.sover = graficos.clack
        self.sclick = graficos.click
        
        self.difi = 0
        
        self.comienzo = Comienzo()
        self.NuevaPregunta()
        while self.comienzo.segundo >= 1: 
            self.comienzo.Dibujar()
            self.Dibujar()
        
       
        
        self.salir = False
        Musica.play()
        while not self.salir : 
            
                self.Dibujar()      
        
    
    def Dibujar(self):
        
           
            Update()
            for event in pygame.event.get():
                
                if self.comienzo.segundo == 0 :
                    if event.type == MOUSEMOTION:
                        raton.Posicionar()
                    if event.type == KEYDOWN :                   
                            if event.key == K_ESCAPE:
                                if xs.modo == 1:
                                            self.salire = 1
                                self.salir = 1
                    if event.type == MOUSEBUTTONDOWN:
                        mousebutton = pygame.mouse.get_pressed()
                        if mousebutton[0] :
                            if self.clicka == 1:                                      
                                for n in self.casilla:
                                    if self.casilla[n].image.Colisiona(raton):
                                       self.sclick.play() 
                                       self.click =  self.casilla[n].id 
                                       del self.casilla[n]               
                                       self.clicka = 0
                                       self.timer = Timer(300)                     
                                       break
                                   
            if self.comienzo.segundo == 0 :                    
                if self.clicka == 0:                        
                    if self.timer.End():
                        self.clicka = 1
                        self.ActualizarPuntos()
                for n in self.casilla:                    
                    if self.casilla[n].image.Colisiona(raton) :                    
                        if self.sonar[n] == 1:
                            self.sover.play()
                            self.sonar[n] = 0           
                    else : self.sonar[n] = 1                                                      
                                          
            
            
            self.pizarra.Dibujar(1)  
            if xs.IDIOMA == 0:
                self.tiza.Dibujar("Puntuacion:",140,35,1,0)
                self.tiza.Dibujar("TiEmpo:",410,35,1,0)
            else :
                self.tiza.Dibujar("  ScorE:",140,35,1,0)
                self.tiza.Dibujar(" TimE:",410,35,1,0)
            self.fuente.Dibujar(self.puntuacion,210,95,1,1)

            
            self.fuente.Dibujar(self.segundos,455,95,1,1)
            if self.comienzo.segundo == 0 :
                for n in self.casilla :
                        if self.casilla[n].image.Colisiona(raton):
                            self.casilla[n].image.PosicionY(self.casilla[n].image.PosicionIY()-2)                    
                        else : 
                            self.casilla[n].image.PosicionY(self.casilla[n].image.PosicionIY())
                        self.casilla[n].Dibujar()
              
             
                if self.segund.EndLoop():
                    self.segundos-=1
                    if self.segundos == -1:
                        self.DibujarResultado()
                raton.Dibujar()
            
    def ActualizarPuntos(self):
        if self.click == 0 :   
            self.puntuacion+=1
        elif self.puntuacion > 0 : self.puntuacion-=1
        self.asigdif()
        self.NuevaPregunta() 
    
    def asigdif(self):
        if self.puntuacion > 6:
            self.difi = 1
        else : self.difi = 0
    def DibujarResultado(self):
        if xs.modo == 0:
              record.Cargar(6,self.puntuacion) 
        else:
              if self.puntuacion >= 20 : self.resex = 2.0
              else : self.resex = float(self.puntuacion*2)/20 
              puntuacion.examen += self.resex
          
          
        self.salir = 1
    
    def NuevaPregunta(self):
        self.click = {}
        self.pulsado = 0
        self.sonar = list(range(20))
        if self.difi == 0:
            self.dificultad = 9
            self.preposiciones =sample(range(20), self.dificultad )
            
            self.pareja = self.preposiciones[0]  
            self.casilla = {}
            tipo = randint(0,2)
            self.casilla[0] = Casilla("img/cartas/%d/%s.png"%(tipo,self.pareja),0)     
              
            for n in range(2,self.dificultad,2):
                self.casilla[n-1] = Casilla("img/cartas/%d/%s.png"%(tipo,self.preposiciones[n]),n)
                self.casilla[n] = Casilla("img/cartas/%d/%s.png"%(tipo,self.preposiciones[n]),n)
               
            if self.dificultad % 2 == 0:    
                self.casilla[n+1] =  Casilla("img/cartas/%d/%s.png"%(tipo,self.preposiciones[n+1]),n+1)               
            shuffle(self.casilla)
            
                   
            
            posy = pantalla.Alto()/2 - 150
                   
           
            
            for n in self.casilla :
                if n % 3 == 0:
                    posy +=66 
                    posx = pantalla.Ancho()/2 - 75
                self.casilla[n].image.Posicion(posx,posy)
                          
                posx += 50
        elif self.difi == 1:
            self.dificultad = 15
            self.preposiciones =sample(range(20), self.dificultad )
            
            self.pareja = self.preposiciones[0]  
            self.casilla = {}
            tipo = randint(0,2)
            self.casilla[0] = Casilla("img/cartas/%d/%s.png"%(tipo,self.pareja),0)     
              
            for n in range(2,self.dificultad,2):
                self.casilla[n-1] = Casilla("img/cartas/%d/%s.png"%(tipo,self.preposiciones[n]),n)
                self.casilla[n] = Casilla("img/cartas/%d/%s.png"%(tipo,self.preposiciones[n]),n)
               
            if self.dificultad % 2 == 0:    
                self.casilla[n+1] =  Casilla("img/cartas/%d/%s.png"%(tipo,self.preposiciones[n+1]),n+1)               
            shuffle(self.casilla)
            
                   
            
            posy = pantalla.Alto()/2 - 150
                   
           
            
            for n in self.casilla :
                if n % 5 == 0:
                    posy +=66 
                    posx = pantalla.Ancho()/2 - 125
                self.casilla[n].image.Posicion(posx,posy)
                          
                posx += 50        
                          
        

        
