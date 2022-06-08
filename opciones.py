from xs import *
import xs
import puntuacion
from graficos import pizarra,click,clack
import graficos



class Opciones:
    def __init__(self):        
        
        self.Recargar()
        
        self.savance = graficos.clack
        
        self.tvolumen = Fuentes("fonts/tiza.ttf",40)
        self.tvolumen.Color((255,102,0))
        self.sonar = [1,1,1,1,1,1]
        self.borrar = -1
        self.idioma = xs.IDIOMA
        self.volumen = xs.Volumen
        self.opcion1 = Opcion[0]
        
        self.Dibujar()
    def Recargar(self):
        self.blogo = Graficos("img/opciones/%s/logo.png"%xs.IDIOMA)
        self.blogo.Posicion(pantalla.Ancho()/2,100)
        self.bpantalla = Graficos("img/opciones/%s/pcompleta1.png"%xs.IDIOMA,pantalla.Ancho()/5*2,190),\
        Graficos("img/opciones/%s/pcompleta2.png"%xs.IDIOMA,pantalla.Ancho()/5*2,190)
        self.bvolumen = Graficos("img/opciones/%s/volumen0.png"%xs.IDIOMA,pantalla.Ancho()/5*2,240),\
        Graficos("img/opciones/%s/volumen1.png"%xs.IDIOMA,pantalla.Ancho()/5*2,240)

        self.bleng = Graficos("img/opciones/%s/lenguaje0.png"%xs.IDIOMA,pantalla.Ancho()/5*2,290),\
        Graficos("img/opciones/%s/lenguaje1.png"%xs.IDIOMA,pantalla.Ancho()/5*2,290)
        
        self.bborrar = Graficos("img/opciones/%s/bdatos0.png"%xs.IDIOMA,pantalla.Ancho()/5*2,340),\
        Graficos("img/opciones/%s/bdatos1.png"%xs.IDIOMA,pantalla.Ancho()/5*2,340)
        
        self.baplicar = Graficos("img/opciones/%s/aplicar0.png"%xs.IDIOMA,pantalla.Ancho()/2,390),\
        Graficos("img/opciones/%s/aplicar1.png"%xs.IDIOMA,pantalla.Ancho()/2,390)
        
        self.bvolver = Graficos("img/opciones/%s/volver0.png"%xs.IDIOMA,100,390),\
        Graficos("img/opciones/%s/volver1.png"%xs.IDIOMA,100,390)

        self.idiom = Graficos("img/opciones/espanol.png",pantalla.Ancho()/5*3.5,290),\
        Graficos("img/opciones/ingles.png",pantalla.Ancho()/5*3.5,290)
        
        self.sino1 = Graficos("img/opciones/%s/si.png"%xs.IDIOMA,pantalla.Ancho()/5*3.5,190),\
        Graficos("img/opciones/%s/no.png"%xs.IDIOMA,pantalla.Ancho()/5*3.5,190)
        self.sino2 =Graficos("img/opciones/%s/si.png"%xs.IDIOMA,pantalla.Ancho()/5*3.5,340),\
        Graficos("img/opciones/%s/no.png"%xs.IDIOMA,pantalla.Ancho()/5*3.5,340)
        
    def AplicarDatos(self):
        conf = open("img/opciones/setup.conf","w")                
        if self.borrar == 1:
            puntuacion.Borrar()
            self.borrar = -1
        conf.write(str(self.opcion1)+str(self.idioma)+str(self.volumen))
               
        if xs.IDIOMA != self.idioma:
            xs.IDIOMA = self.idioma
            self.Recargar()
             
        if self.opcion1 != Opcion[0]:
            if self.opcion1 == 0:
                pantalla = Pantalla((640,480),pygame.DOUBLEBUF|pygame.RLEACCEL)
            elif self.opcion1 == 1:
                pantalla = Pantalla((640,480),pygame.RLEACCEL|pygame.FULLSCREEN)
        Opcion[0]= self.opcion1
        xs.Volumen = self.volumen
        graficos.Musica()
        graficos.menumus.stop()
        graficos.menumus.play(-1)
        Musica.set_volume(float(self.volumen)/100)
        conf.close()
        del conf
        
    def Dibujar(self):
        salir = 0
        while not salir:
            for event in pygame.event.get():
               
                if event.type == MOUSEMOTION:
                    raton.Posicionar()                    
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE :
                        salir = 1
                if event.type == MOUSEBUTTONDOWN:                   
                        mousebutton = pygame.mouse.get_pressed()
                        if self.bpantalla[0].Colisiona(raton):
                            click.play()
                            if self.opcion1 == 1:
                                self.opcion1 = 0
                            elif self.opcion1 == 0:
                                self.opcion1 = 1
                        if self.baplicar[0].Colisiona(raton):
                                graficos.click.play()
                                self.AplicarDatos()
                        if self.bvolver[0].Colisiona(raton): 
                                graficos.click.play()
                                salir = 1
                        if self.bleng[0].Colisiona(raton):
                                graficos.click.play()
                                if self.idioma == 1:
                                    self.idioma = 0
                                elif self.idioma == 0:
                                    self.idioma = 1
                        if self.bborrar[0].Colisiona(raton):
                            graficos.click.play()
                            self.borrar = -self.borrar
                        if mousebutton[0] :
                            if self.bvolumen[0].Colisiona(raton):
                                graficos.click.play()
                                if self.volumen >= 0 and self.volumen < 100:
                                    self.volumen += 10
                                    Volumen = self.volumen
                        elif mousebutton[2]:
                            if self.bvolumen[0].Colisiona(raton):
                                graficos.click.play()
                                if self.volumen > 0 and self.volumen <= 100:
                                    self.volumen -= 10
                                    Volumen = self.volumen
                            
            pizarra.Dibujar(1)
            self.blogo.Dibujar(1)
            
            if self.bpantalla[0].Colisiona(raton):
                if self.sonar[0] == 1:
                    self.savance.play()
                    self.sonar[0]= 0
                self.bpantalla[1].Dibujar(1)
                    
            else: 
                self.bpantalla[0].Dibujar(1)
                self.sonar[0] = 1
            
            if self.bvolumen[0].Colisiona(raton):
                if self.sonar[1] == 1:
                    self.savance.play()
                    self.sonar[1]= 0
                self.bvolumen[1].Dibujar(1)
            else:
                self.bvolumen[0].Dibujar(1)
                self.sonar[1]=1
                
            if self.bleng[0].Colisiona(raton):                
                if self.sonar[5] == 1:
                    self.savance.play()
                    self.sonar[5]= 0
                self.bleng[1].Dibujar(1)
            else:  
                self.bleng[0].Dibujar(1)
                self.sonar[5]=1
                
            if self.bborrar[0].Colisiona(raton):                
                if self.sonar[2] == 1:
                    self.savance.play()
                    self.sonar[2]= 0
                self.bborrar[1].Dibujar(1)
            else:  
                self.bborrar[0].Dibujar(1)
                self.sonar[2]=1
            
                        
            if self.baplicar[0].Colisiona(raton):
                if self.sonar[3] == 1:
                    self.savance.play()
                    self.sonar[3]= 0
                self.baplicar[1].Dibujar(1)
            else: 
                 self.baplicar[0].Dibujar(1)
                 self.sonar[3]=1
            
            if self.bvolver[0].Colisiona(raton):
                if self.sonar[4] == 1:
                    self.savance.play()
                    self.sonar[4]= 0
                self.bvolver[1].Dibujar(1)
            else:  
                self.bvolver[0].Dibujar(1)
                self.sonar[4]=1
            
            self.tvolumen.Dibujar(self.volumen,pantalla.Ancho()/5*3.5,240,1,1)  
            if self.opcion1 == 1:         
                self.sino1[0].Dibujar(1)
            else : self.sino1[1].Dibujar(1)

            if self.idioma == 1:
                self.idiom[1].Dibujar(1)
            else : self.idiom[0].Dibujar(1)
            
            if self.borrar == -1 :
                self.sino2[1].Dibujar(1)
            else : self.sino2[0].Dibujar(1)
            raton.Dibujar()
  
            Update()
            
