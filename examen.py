from xs import *
import xs,record
from random import shuffle
from calculo  import Calculo
from monedas import Monedas

from memorizar import Memorizar
from parejas import Parejas
from carta import Carta
from parejashide import ParejasHide
from prueba4 import Monedas2
from prueba5 import Prueba5
from simon import Simon

from calculo2 import Calculo2
import puntuacion,sys
from graficos import *


puntuacion.cargarPuntos()


class Examen:
    
    def __init__(self):
        xs.modo = 1
        puntuacion.cExamen()
        self.blogo = Graficos("img/examen/%s/logo.png"%xs.IDIOMA)
        self.blogo.Posicion(pantalla.Ancho()/2,100)
        self.bentrar = Graficos("img/examen/%s/bentrar0.png"%xs.IDIOMA,pantalla.Ancho()/2-80,pantalla.Alto()-100),\
                       Graficos("img/examen/%s/bentrar1.png"%xs.IDIOMA,pantalla.Ancho()/2-80,pantalla.Alto()-100)
        self.bvolver = Graficos("img/practicas/%s/volver.png"%xs.IDIOMA,100,pantalla.Alto()-95),\
                       Graficos("img/practicas/%s/volver1.png"%xs.IDIOMA,100,pantalla.Alto()-95)
        self.comentario = Graficos("img/examen/comentario.png",320,235)
        
        self.fuente = Fuentes("fonts/fuente.ttf",12)
        
        self.fuente.Color((255,255,255))
        self.fuente2 = Fuentes("fonts/fuente.ttf",15)
        self.tiza = Fuentes("fonts/tiza.ttf",30)
        self.tiza.Color((255,0,0))
        self.fuente2.Color((255,255,255))
        self.sonar,self.sonar2=1,1
        self.fuente3 = Fuentes("fonts/fuente.ttf",15)        
        self.fuente3.Color((255,0,0))
        if xs.IDIOMA == 0:
            self.ctxt = "Demuestra los conocimientos que has adquirido."
        else : self.ctxt = "Demonstrates the knowledge that you have acquired."
        self.ictxt = ""
        self.actxt = 0
        self.mctxt = len(self.ctxt)
        self.pruebact = 1
        self.puntuacion = 0.0
        
        
        self.Dibujar()
        
    
    def Dibujar(self):
        self.done = 0
        
        while not self.done :
            for event in pygame.event.get():
                
                if event.type == MOUSEMOTION:
                    raton.Posicionar()                    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE :
                        self.done = 1 
                if event.type == MOUSEBUTTONDOWN:                       
                    mousebutton = pygame.mouse.get_pressed()
                    if mousebutton[0] == 1:
                        if self.bentrar[0].Colisiona(raton):
                            click.play()
                            self.ComenzarExamen()
                        if self.bvolver[0].Colisiona(raton):                            
                            self.done =1 
            
            pizarra.Dibujar(1)
            self.comentario.Dibujar(1)
            self.blogo.Dibujar(1)
            self.fuente.Dibujar(self.ictxt,185,180,1,0)
            if xs.IDIOMA == 0:
                self.fuente2.Dibujar("Mejor Alumno :                        Puntuación : ",185,220,1,0)
            else :  self.fuente2.Dibujar("Better Student :                           Score : ",185,220,1,0)
            self.tiza.Dibujar(puntuacion.cnombre,235,265,1,1)
            self.tiza.Dibujar(float(puntuacion.cexamen),425,265,1,1)
            
            
            if self.bentrar[0].Colisiona(raton):
                if self.sonar == 1:
                        clack.play()
                        self.sonar = 0 
                self.bentrar[1].Dibujar(1)
                if self.actxt <  self.mctxt:
                    self.ictxt += self.ctxt[self.actxt]
                    self.actxt +=1
                  
                caracolhabla.Animar(200)     
            else : 
                self.bentrar[0].Dibujar(1)
                self.actxt = 0 
                self.ictxt = ""
                self.sonar = 1
                caracol.Animar(200)
                
            if self.bvolver[0].Colisiona(raton):
                if self.sonar2 == 1:
                        clack.play()
                        self.sonar2 = 0 
                self.bvolver[1].Dibujar(1)
                
            else : self.bvolver[0].Dibujar(1);self.sonar2 = 1
            
            
            raton.Dibujar()
            Update()
    def ComenzarExamen(self):
        self.ftitulo = Fuentes("fonts/fuente.ttf",20)
        self.bcont = Graficos("img/examen/%s/bcont0.png"%xs.IDIOMA,pantalla.Ancho()/2-80,pantalla.Alto()-100),\
                       Graficos("img/examen/%s/bcont1.png"%xs.IDIOMA,pantalla.Ancho()/2-80,pantalla.Alto()-100)
        self.ftitulo.Color((255,150,0))
        self.CargarP()
        self.Pruebas = [Calculo,Calculo2,Monedas,Monedas2,Prueba5,Parejas,Carta,Memorizar,ParejasHide,Simon]
        
        self.buffer = list(range(10))
        shuffle(self.buffer)
        self.prueba = self.buffer[:5]
        self.pruebact = 1
                
        
        puntuacion.examen = 0.0
        while(self.pruebact <= 5 and not self.done):
           self.PruebaSiguiente()
           self.pruebact +=1
        if self.pruebact >= 5:               
               self.buffer = str("%.1f"%puntuacion.examen)
               self.puntuacion = float(self.buffer)
               record.CargarE(float(self.puntuacion))
        puntuacion.cExamen()
        self.Dibujar()
    def CargarP(self):       
        if xs.IDIOMA == 0:
            self.titulos = ["Algebra","Signo","Contar Dinero","Contar Monedas","Lógica","Buscar Pareja"]+\
                           ["Buscar Unica","Memorizar Numero","Memorizar Fichas","Simón"]
        else : self.titulos = ["Algebra","Sing","Count Money","Count Coins","Logic","Look for Pair"]+\
                              ["Look for Only","Memorize Number","Memorize Cards","Simon"]  
        self.txt = list(range(11))
        if xs.IDIOMA == 0:
            self.txt[0] = "Haz las siguientes operaciones."
            self.txt[1] = "Pulsa en el signo correspondiente."
            self.txt[2] = "Escoge el grupo con mas dinero."
            self.txt[3] = "¿ Cuánto dinero hay ?."
            self.txt[4] = "Acierta que numero va en la casilla."
            self.txt[5] = "Pulsa la única pareja de cartas."
            self.txt[6] = "Pulsa la carta que no tenga pareja."
            self.txt[7] = "Memoriza el numero en poco tiempo."
            self.txt[8] = "Memoriza cartas durante 5 segundos."
            self.txt[9] = "Memoriza la secuencia de colores."
            self.txt[10] = "Vuelve al menu principal."
        else :
            self.txt[0] = "Make the following operations."
            self.txt[1] = "Press in the corresponding sign."
            self.txt[2] = "Choose the group with more money."
            self.txt[3] = "How much money has?"
            self.txt[4] = "What number goes in the square?."
            self.txt[5] = "Press the only pair of cards."
            self.txt[6] = "Press the letter that does'n have pair."
            self.txt[7] = "Memorize the number in a short time."
            self.txt[8] = "Memorize the cards during 5 seconds. "
            self.txt[9] = "Memorize the colors sequence."
            self.txt[10] = "Returns to the main menu."
        self.txti = list(range(11))
        self.txta = list(range(11))
        self.txtm = list(range(11))
        for x in range(11):
            self.txti[x] = ""
            self.txta[x] = 0
            self.txtm[x] = len(self.txt[x])
            
    def DibujarP(self,indice):
        self.fuente.Dibujar(self.txti[indice],326,220,1)
        if self.txta[indice] <  self.txtm[indice]:
                self.txti[indice] += self.txt[indice][self.txta[indice]]
                self.txta[indice] +=1
    def DibujarPe(self,indice):
        self.fuente.Dibujar(self.txti[indice],220,240,1)
        if self.txta[indice] <  self.txtm[indice]:
                self.txti[indice] += self.txt[indice][self.txta[indice]]
                self.txta[indice] +=1
       
    def PruebaSiguiente(self):
        done = 0
        while not done:  
            Update()          
            for event in pygame.event.get():
                if event.type == QUIT :
                    sys.exit()
                if event.type == MOUSEMOTION:
                    raton.Posicionar()                    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE :
                        self.done = 1 
                        done = 1
                if event.type == MOUSEBUTTONDOWN:                       
                    mousebutton = pygame.mouse.get_pressed()
                    if mousebutton[0] == 1:
                         if self.bvolver[0].Colisiona(raton):
                             click.play()
                             self.done = 1
                             done = 1
                         if self.bcont[0].Colisiona(raton):
                             click.play()
                             menumus.fadeout(1000)
                             prueba = self.Pruebas[self.prueba[self.pruebact-1]]()
                             if prueba.salire == 1 : self.done = 1
                             del prueba  
                             xs.Musica.stop() 
                             menumus.play(-1)                          
                             done = 1
                            
                        
            
            pizarra.Dibujar(1)
            self.comentario.Dibujar(1)
            self.blogo.Dibujar(1)
            if xs.IDIOMA == 0:
                self.fuente2.Dibujar("Prueba Nº %s : "%self.pruebact,185,175,1,0)
            else : self.fuente2.Dibujar("  Test No %s : "%self.pruebact,185,175,1,0)
            self.ftitulo.Dibujar(self.titulos[self.prueba[self.pruebact-1]],200,200,1,0)
            
            
            if self.bcont[0].Colisiona(raton):
                if self.sonar == 1:
                        clack.play()
                        self.sonar = 0
                self.bcont[1].Dibujar(1)               
                self.DibujarPe(self.prueba[self.pruebact-1])    
                caracolhabla.Animar(200)
                
            else : 
                self.bcont[0].Dibujar(1)
                self.txta[self.prueba[self.pruebact-1]] = 0 
                self.txti[self.prueba[self.pruebact-1]] = ""
                caracol.Animar(200)
                self.sonar = 1
            if self.bvolver[0].Colisiona(raton):
                if self.sonar2 == 1:
                        clack.play()
                        self.sonar2 = 0
                self.bvolver[1].Dibujar(1)                
            else : self.bvolver[0].Dibujar(1);self.sonar2 = 1
            
            
            
            raton.Dibujar()
            
                    
        pass        
            

    
