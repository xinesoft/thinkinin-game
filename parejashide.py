import sys,xs
from xs import *
from random import *
from comienzo import Comienzo
import record
import puntuacion


class Casilla:
    def __init__(self,file,id):
        self.image = Graficos(file)
        self.id = id
        self.dibujar = 1
    def Dibujar(self):
       if self.dibujar == 1:
           self.image.Dibujar()

class ParejasHide:
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
        self.fuentea = Fuentes("fonts/fuente.ttf",100)
        self.fuentea.SetColor(0,0,255)
        self.segund = Timer(1000)
        self.segundoso = 3
        self.segundi = {}
        for n in range(3):
            self.segundi[n+1] =Graficos("img/cartas/%s.png"%str(n+1))
            self.segundi[n+1].Posicion(pantalla.Ancho()/2,120)
        


        self.puntuacion = 0
        self.segundos = 60
        self.activado = 0
        self.tiempo = 0
       
        self.comienzo = Comienzo()
        
        self.NuevaPregunta()    
        
        while self.comienzo.segundo >= 1: 
            self.comienzo.Dibujar()
            self.Dibujar()
        
        
        self.tiempo = 0
        self.tmarcador = Timer(109)    
        
        self.NuevaPregunta()  
        self.salir = False
        Musica.play(-1)
       
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
                                            self.salir = 1
                                            if xs.modo == 1:
                                                self.salire = 1
                        if event.type == MOUSEBUTTONDOWN:
                            if self.activado == 1:
                                mousebutton = pygame.mouse.get_pressed()
                                if mousebutton[0] :
                                    for n in self.casilla :
                                        if self.casilla[n].image.Colisiona(raton):
                                            if self.pulsado <= 2:
                                                self.pulsado += 1
                                            self.click[self.pulsado] = self.casilla[n].id
                                            if self.pulsado == 1:
                                                    self.id1 = self.casilla[n].id
        
        
                                                    self.casillao[n].dibujar = 0
        
        
                                            if self.pulsado == 2:
                                                    self.id2 = self.casilla[n].id
                                                    self.casillao[n].dibujar = 0
        
                                                    self.timer = Timer(500)
                                                
            if self.comienzo.segundo == 0:
                if len(self.casilla) == 0:
                    self.puntuacion += 1
                    self.activado = 1
                    self.tiempo = 0
                    self.NuevaPregunta()

            self.pizarra.Dibujar(1)
            if xs.IDIOMA == 0:
                self.tiza.Dibujar("Puntuacion:",140,35,1,0)
                self.tiza.Dibujar("TiEmpo:",410,35,1,0)
            else :
                self.tiza.Dibujar("  ScorE:",140,35,1,0)
                self.tiza.Dibujar(" TimE:",410,35,1,0)
            self.fuente.Dibujar(self.puntuacion,210,95,1,1)

            
            self.fuente.Dibujar(self.segundos,455,95,1,1)
           
            if self.comienzo.segundo == 0:    
                for n in self.casilla :
                        if self.activado == 1:
                            if self.casilla[n].image.Colisiona(raton):
                                self.casillao[n].image.PosicionY(self.casilla[n].image.PosicionIY()-2)
                                self.casilla[n].image.PosicionY(self.casilla[n].image.PosicionIY()-2)
                            else :
                                self.casilla[n].image.PosicionY(self.casilla[n].image.PosicionIY())
                                self.casillao[n].image.PosicionY(self.casilla[n].image.PosicionIY())
                        self.casilla[n].Dibujar()
            if self.comienzo.segundo == 0:
                if self.timer10.End():
                    for n in self.casillao :
                        self.casillao[n].Dibujar()
                        self.tiempo = 1
                    self.activado = 1
    
            if self.comienzo.segundo == 0:
                if self.pulsado >= 2 :
                    if self.timer.End():
                      if self.id1-100 == self.id2 or self.id1 == self.id2-100:
                          for n in self.casilla:
                                       if self.casilla[n].id == self.id2:
                                           del self.casilla[n]
                                           del self.casillao[n]
                                           break
                          for n in self.casilla:
                                       if self.casilla[n].id == self.id1:
                                           del self.casilla[n]
                                           del self.casillao[n]
                                           break
    
                          self.pulsado = 0
    
    
                      else:
                           for n in self.casillao:
                               self.casillao[n].dibujar = 1
                           self.pulsado = 0
                    activado = 0
    
    
    
    
    
    
    
            if self.comienzo.segundo == 0:
                if self.segund.EndLoop():
                    if self.tiempo == 0 :
                        self.segundoso-=1
                        if self.segundoso == 0:
                            self.segundos-=1
                            self.activado = 1
    
    
    
                    else:
                        self.segundos-=1
                        if self.segundoso > 0:
                            self.segundoso-=1
                        if self.segundos == -1:
                            self.DibujarResultado()
    
            if self.comienzo.segundo == 0:
                if self.segundoso > 0 :
                    self.segundi[self.segundoso].Dibujar(1)
                raton.Dibujar()


    def DibujarResultado(self):   
        if xs.modo == 0:
              record.Cargar(8,self.puntuacion) 
        else:
              if self.puntuacion >= 10 : self.resex = 2.0
              else : self.resex = float(self.puntuacion*2)/10 
              puntuacion.examen += self.resex
          
        self.salir = 1

    def NuevaPregunta(self):
        self.click = {}
        
        self.pulsado = 0
        self.segundoso = 3

        self.dificultad = 12
        self.preposiciones =sample(range(20), self.dificultad )

        self.pareja = self.preposiciones[0]
        self.casilla = {}
        self.casillao = {}
        self.posiciones = self.preposiciones[:int(self.dificultad/2)]
        tipo = str(randint(0,2))
        for n in range(int(self.dificultad/2)):
            self.casilla[n] = Casilla("img/cartas/%s/%s.png"%(tipo,self.posiciones[n]),n)
            self.casilla[n+int(self.dificultad/2)] = Casilla("img/cartas/%s/%s.png"%(tipo,self.posiciones[n]),n+100)
            self.casillao[n] = Casilla("img/cartas/back.png",n)
            self.casillao[n+int(self.dificultad/2)] = Casilla("img/cartas/back.png",n+100)

        shuffle(self.casilla)



        posx = pantalla.Ancho()/2 - 100
        posy = pantalla.Alto()/2 - 125



        for n in  self.casilla:

            if n % 4 == 0:
                    posy +=66
                    posx = pantalla.Ancho()/2 - 100
            self.casilla[n].image.Posicion(posx,posy)
            self.casillao[n].image.Posicion(posx,posy)
            posx += 50

        self.timer10 = Timer(3000)
        self.segund = Timer(1000)




