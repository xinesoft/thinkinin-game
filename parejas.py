import sys
from xs import *
import xs
from random import *
from comienzo import Comienzo
import record
import puntuacion
import graficos
class Casilla:
    
    def __init__(self,file,id):
        self.image = Graficos(file)
        self.id = id

    def Dibujar(self):
        self.image.Dibujar()

class Parejas:
    def __init__(self):
        pantalla.Color((200,200,200))
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))
        self.salire = 0
        self.pizarra = Graficos("img/menu/bpizarra.png")
        self.pizarra.Posicion(pantalla.Ancho()/2,pantalla.Alto()/2)
        self.tiza = Fuentes("fonts/tiza.ttf",30)
        self.tiza.SetColor(255, 255, 255)
        self.fuente = Fuentes("fonts/fuente.ttf",40)
        self.fuente.SetColor(255,0,0)
        self.segund = Timer(1000)
        
        
        self.sover = graficos.clack
        self.sclick = graficos.click

        self.puntuacion = 0
        self.segundos = 60
        self.comienzo = 1
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
                
                if self.comienzo.segundo == 0:
                    if event.type == MOUSEMOTION:
                        raton.Posicionar()
                    if event.type == KEYDOWN :
                            if event.key == K_ESCAPE:
                                        Musica.fadeout(1000)
                                        self.salir = 1
                                        if xs.modo == 1:
                                            self.salire = 1
                    if event.type == MOUSEBUTTONDOWN:
                        mousebutton = pygame.mouse.get_pressed()
                        if mousebutton[0] :
                            for n in self.casilla :
                                if self.casilla[n].image.Colisiona(raton):
                                    self.sclick.play()
                                    if self.pulsado <= 1:
                                        self.pulsado += 1
                                    self.click[self.pulsado] = self.casilla[n].id
                                    if self.pulsado == 1:
    
                                            del self.casilla[n]
    
    
                                            break
                                    if self.pulsado == 2:
    
                                            del self.casilla[n]
    
                                            self.pulsado += 1
                                            self.timer = Timer(200)
                                            break
            if self.comienzo.segundo == 0:
                if self.pulsado >= 2:
                    if self.timer.End():
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
            else:
                self.tiza.Dibujar("  ScorE:",140,35,1,0)            
                self.tiza.Dibujar(" TimE:",410,35,1,0)
            self.fuente.Dibujar(self.puntuacion,210,95,1,1)
            self.fuente.Dibujar(self.segundos,455,95,1,1)
            if self.comienzo.segundo == 0:
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
        if self.click[1] == 0 and  self.click[2] ==0:
            self.puntuacion+=1
        elif self.puntuacion > 0 : self.puntuacion-=1
        self.NuevaPregunta()

    def DibujarResultado(self):
        
        if xs.modo == 0:
              record.Cargar(5,self.puntuacion) 
        else:
              if self.puntuacion >= 20: self.resex = 2.0
              else : self.resex = float(self.puntuacion*2)/20 
              puntuacion.examen += self.resex
          
        self.salir = 1

    def NuevaPregunta(self):
        self.click = {}
        self.pulsado = 0
        self.dificultad = 12
        self.sonar = list(range(self.dificultad))
        for x in range(self.dificultad): self.sonar[x] = 1
        self.preposiciones =sample(range(20), self.dificultad )
        self.pareja = self.preposiciones[0]
        self.casilla = {}
        tipo = randint(0,2)
        self.casilla[0] = Casilla("img/cartas/%d/%s.png"%(tipo,self.pareja),0)
        self.casilla[1] = Casilla("img/cartas/%d/%s.png"%(tipo,self.pareja),0)
        for n in range(2,self.dificultad):
            self.casilla[n] = Casilla("img/cartas/%d/%s.png"%(tipo,self.preposiciones[n-1]),n)

        shuffle(self.casilla)
        posx = pantalla.Ancho()/2 - 100
        posy = pantalla.Alto()/2 -150



        for n in self.casilla :
            if n % 4 == 0:
                posy +=66
                posx = pantalla.Ancho()/2 - 100
            self.casilla[n].image.Posicion(posx,posy)

            posx += 50






