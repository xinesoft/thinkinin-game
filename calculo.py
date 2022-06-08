import sys
import panel,xs
from xs import *
from random import randint
from comienzo import Comienzo
import graficos
import record
import puntuacion

class Calculo:
    def __init__(self):
        Musica.load(choice(["musica/musica1.ogg","musica/musica2.ogg","musica/musica3.ogg"]))
        self.puntuacion = 0
        self.signoc = ""   
        self.signoc2 = ""     
        self.RMAX = 2
        self.segundos = 60
        self.dificultad = 0
        self.sonar = 1
        self.resultadomac = 0
        self.salire = 0
        salir = 0
        
        self.sclick = graficos.click
        pantalla.Color((200,200,200))
        
        self.panel = panel.Panel()
        
        self.tiza = Fuentes("fonts/tiza.ttf",50)
        self.tiza.SetColor(255, 255, 255)
        self.tiza2 = Fuentes("fonts/tiza.ttf",30)
        self.tiza2.SetColor(255, 255, 255)
        self.fuente3 = Fuentes("fonts/fuente.ttf",40)
        self.fuente3.SetColor(255,0,0)
                
        self.pizarra = Graficos("img/menu/pizarra.png",pantalla.Ancho()/2,142)
       
        
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
        
    def __del__(self):
        del self.panel
        del self.tiza
        del self.tiza2
        del self.fuente3
        del self.pizarra
        del self.segund 
        del self.timer4       
        
    def DibujarTiza(self):
        if self.comienzo.segundo == 0:
            if(self.dificultad == 1):
                self.tiza.Dibujar(self.num3,pantalla.Ancho()/2-165,175,1,1)
                self.tiza.Dibujar(self.signoc2,pantalla.Ancho()/2-115,175,1,1)
                self.tiza.Dibujar(self.num1,pantalla.Ancho()/2-65,175,1,1)
                self.tiza.Dibujar(self.signoc,pantalla.Ancho()/2-15,175,1,1)
                self.tiza.Dibujar(self.num2,pantalla.Ancho()/2+35,175,1,1)
                self.tiza.Dibujar("=",pantalla.Ancho()/2+75,175,1,1)
                self.tiza.Dibujar(self.resuljug,pantalla.Ancho()/2+140,175,1,1)
            elif (self.dificultad == 0):
                self.tiza.Dibujar(self.num1,pantalla.Ancho()/2-100,175,1,1)
                self.tiza.Dibujar(self.signoc,pantalla.Ancho()/2-50,175,1,1)
                self.tiza.Dibujar(self.num2,pantalla.Ancho()/2,175,1,1)
                self.tiza.Dibujar("=",pantalla.Ancho()/2+50,175,1,1)
                self.tiza.Dibujar(self.resuljug,pantalla.Ancho()/2+105,175,1,1)







    def Dibujar(self):   
            if self.comienzo.segundo == 0:     
                raton.Dibujar()
            Update()
                 


            for event in pygame.event.get():
                

                if event.type == QUIT :
                    sys.exit()
                if event.type == MOUSEMOTION:
                    raton.Posicionar()
                if self.comienzo.segundo == 0:
                        if event.type == KEYDOWN :
                            self.ActualizarKBoton()
                            if event.key == K_ESCAPE:
                                        self.salir = 1
                                        if xs.modo == 1:
                                            self.salire = 1
                        if event.type == MOUSEBUTTONDOWN:
                            
                            mousebutton = pygame.mouse.get_pressed()
                            if mousebutton[0] :
                                self.ActualizarMBoton()
                        if event.type == MOUSEBUTTONUP or event.type == KEYUP:
                            self.sonar = 1
            
            
            self.panel.Dibujar()
            self.pizarra.Dibujar(1)
            self.DibujarTiza()
            
        
                                
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
        
           
            if self.puntuacion < 5 :
                self.dificultad = 0
                self.RMAX = 1
                if self.resultadomac < 0 : self.RMAX = 2
            else :
                self.dificultad = 1
                self.RMAX = 2
                if self.resultadomac < 0 : self.RMAX = 3
            self.resuljug = "_"



            self.primer = 1
            self.num1 = randint(0,10)
            self.num2 = randint(0,10)
            self.num3 = randint(0,10)
            self.resultadomac = 0
            self.signo = randint(0,3)
            self.signo2 = randint(0,2)
            if self.dificultad == 0:
                if self.signo == 0:
                    self.resultadomac = self.num1 + self.num2
                    self.signoc = "+"
                if self.signo == 1 :
                    self.resultadomac = self.num1 - self.num2
                    self.signoc = "-"
                if self.signo == 2 :
                    self.resultadomac = self.num1 * self.num2
                    self.signoc = "x"
                if self.signo == 3 :
                    self.signoc = ":"
                    while self.num2 == 0:
                            self.num2 = randint(1,10)
                    while self.num1 % self.num2 != 0 :
                            
                             self.num1 = randint(1,10)
                             self.num2 = randint(1,10)
                    while self.num2 == 0:
                            self.num2 = randint(1,10)
                        
                    self.resultadomac = self.num1 / self.num2
                   
                   
                    
                  

            elif self.dificultad == 1:
                self.signo = randint(0,2)
                if self.signo2 == 0:
                    if self.signo == 0:
                        self.resultadomac = self.num3 + self.num1 + self.num2
                        self.signoc = "+"
                    if self.signo == 1:
                        self.resultadomac = self.num3 + self.num1 - self.num2
                        self.signoc = "-"
                    if self.signo == 2:
                        self.resultadomac = self.num3 + self.num1 * self.num2
                        self.signoc = "x"

                    self.signoc2 = "+"
                if self.signo2 == 1:
                    
                        if self.signo == 0:
                            self.resultadomac = self.num3 - self.num1 + self.num2
                            self.signoc = "+"
                        if self.signo == 1:
                            self.resultadomac = self.num3 - self.num1 - self.num2
                            self.signoc = "-"
                        if self.signo == 2:
                            self.resultadomac = self.num3 - self.num1 * self.num2
                            self.signoc = "x"
    
                        self.signoc2 = "-"                  
                    
              
                if self.signo2 == 2:
                    
                        if self.signo == 0:
                            self.resultadomac = self.num3 * self.num1 + self.num2
                            self.signoc = "+"
                        if self.signo == 1:
                            self.resultadomac = self.num3 * self.num1 - self.num2
                            self.signoc = "-"
                        if self.signo == 2:
                            self.resultadomac = self.num3 * self.num1 * self.num2
                            self.signoc = "x"
    
                        self.signoc2 = "x"       
        

            
            self.resulmac = str(self.resultadomac)
            if self.resultadomac < 0:
                self.NuevaPregunta()
            
    
    def Resultado(self):

        if self.resulmac != self.resuljug:
            if self.puntuacion > 0: self.puntuacion-=1

        else : self.puntuacion+=1
    
    def ActualizarKBoton(self):
        
        keydown = pygame.key.get_pressed()
                
        if self.puntuacion < 5 :
            
                
                self.RMAX = 1
                if self.resultadomac < 0 or self.resultadomac == 100 : self.RMAX = 2
        else :
                
                self.RMAX = 2
                if self.resultadomac < 0 : self.RMAX = 3
        if self.sonar == 1:
            for n in range(256,267):
                if keydown[n]:
                    self.sclick.play()
                    self.sonar = 0
            if keydown[271]:
                self.sclick.play()
                self.sonar = 0
                
        if len(self.resuljug) <= self.RMAX:
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
            self.resuljug = "_"
            self.primer = 1
            
        if  keydown[K_KP_ENTER]:
            self.Resultado()
            self.NuevaPregunta()

    def ActualizarMBoton(self):
        
        
                
        if self.puntuacion < 5 :
            
                
                self.RMAX = 1
                if self.resultadomac < 0 or self.resultadomac == 100 : self.RMAX = 2
        else :
                
                self.RMAX = 2
                if self.resultadomac < 0 : self.RMAX = 3
        if self.sonar == 1:
            for n in range(12):
                if self.panel.boton[n].Colisiona(raton):
                    self.sclick.play()
                    self.sonar = 0
        
        if len(self.resuljug) <= self.RMAX:
            if self.panel.boton[9].Colisiona(raton):
                
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-0"

                    else  : self.resuljug = "0"
                    self.primer = 0   
                else : self.resuljug+="0"
            elif self.panel.boton[0].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-1"

                    else  : self.resuljug = "1"
                    self.primer = 0   
                else : self.resuljug+="1"
            elif self.panel.boton[1].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-2"

                    else  : self.resuljug = "2"
                    self.primer = 0   
                else : self.resuljug+="2"
            elif self.panel.boton[2].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-3"

                    else  : self.resuljug = "3"
                    self.primer = 0   
                else : self.resuljug+="3"
            elif self.panel.boton[3].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-4"

                    else  : self.resuljug = "4"
                    self.primer = 0   
                else : self.resuljug+="4"
            elif self.panel.boton[4].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-5"

                    else  : self.resuljug = "5"
                    self.primer = 0   
                else : self.resuljug+="5"
            elif self.panel.boton[5].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-6"

                    else  : self.resuljug = "6"
                    self.primer = 0   
                else : self.resuljug+="6"
            elif self.panel.boton[6].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-7"

                    else  : self.resuljug = "7"
                    self.primer = 0   
                else : self.resuljug+="7"
            elif self.panel.boton[7].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-8"

                    else  : self.resuljug = "8"
                    self.primer = 0   
                else : self.resuljug+="8"
            elif self.panel.boton[8].Colisiona(raton):
                if self.primer :
                    if self.resultadomac < 0:
                        self.resuljug = "-9"

                    else  : self.resuljug = "9"
                    self.primer = 0   
                else : self.resuljug+="9"           
           

        if self.panel.boton[10].Colisiona(raton):
            self.resuljug = "_"
            self.primer = 1
            
        if self.panel.boton[11].Colisiona(raton):
            self.Resultado()
            self.NuevaPregunta()
        
    def DibujarResultado(self):
          
        if xs.modo == 0:
          record.Cargar(0,self.puntuacion) 
        else:
          if self.puntuacion >= 25 : self.resex = 2.0
          else : self.resex = float(self.puntuacion*2)/25 
          puntuacion.examen += self.resex
                   
        self.salir = 1
         
          
