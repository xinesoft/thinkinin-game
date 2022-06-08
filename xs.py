import pygame,sys
from pygame.locals import *
from random import choice

if not pygame.font:
    print("Warning: fonts disabled")
if not pygame.mixer:
    print("Warning: sound disabled")
class Pantalla:

   def __init__(self,res,arg):

       try:
           self.screen = pygame.display.set_mode(res,arg)
       except:
           print("No se ha podido Cargar la pantalla")
           sys.exit()
       self.color = (0,0,0)
       self.cambio = -1
       self.screen.fill(self.color)
       self.res = res

   def Cambio(self):
       self.cambio = -self.cambio
       if self.cambio == -1 :
           pantalla = Pantalla((640,480), pygame.DOUBLEBUF|pygame.OPENGL)
       elif self.cambio == 1:
           pantalla = Pantalla((640,480), pygame.FULLSCREEN|pygame.RLEACCEL)
   def Ancho(self):
       return self.res[0]
   def Alto(self):
       return self.res[1]
   def Color(self,color):
       self.color = color

   def actualizar(self):
       pygame.display.update()
       pygame.display.flip()
       self.screen.fill(self.color)




class Fuentes :
    def __init__(self,file,size = 20,r = 0,g=0,b=0):

        try:
            self.fuente = pygame.font.Font(file, size)
        except:
            print("No se ha encontrado el archivo : %s")
            sys.exit()
        self.color = [r,g,b]

    def SetColor(self,r,g,b):
        self.color = [r,g,b]
    def Color(self,color):
        self.color = color

    def Dibujar(self,texto,posx=0,posy=0,antialias = False,centrado = 0):
        self.surface = self.fuente.render(str(texto),antialias,self.color)
        self.rect = self.surface.get_rect()
        if centrado == 1 :
            self.rect[:2] = [posx-self.rect[2]/2,posy-self.rect[3]/2]


        elif centrado == 0:
            self.rect[:2] =[posx,posy]



        pantalla.screen.blit(self.surface,self.rect)


class Timer:
    def __init__(self,tic) :
        self.ticks = tic
        self.ResetTimeBase()

    def ResetTimeBase(self) :
        self.ini_milisegundos=pygame.time.get_ticks()

    def  CurrentTime(self) :
        self.fin_milisegundos=pygame.time.get_ticks()
        return self.fin_milisegundos-self.ini_milisegundos


    def End(self):
        if self.CurrentTime() >= self.ticks :
            return 1
        else : return 0
    def Ending(self):
        if self.CurrentTime() == self.ticks :
            return 1
        else : return 0
    def EndLoop(self):
                if self.CurrentTime() >= self.ticks:
                    self.ResetTimeBase()
                    return 1
                else : return 0

    def EsperarFPS(self) :
        self.frametime=self.CurrentTime()
        while self.frametime<self.ticks :
            self.frametime=self.CurrentTime()
        self.ResetTimeBase()

class Graficos(Timer):

    def __init__(self ,file,posx = 0,posy = 0):
        self.surface = {}
        self.frame = 0
        self.frameact = 0
        self.ini_milisegundos=pygame.time.get_ticks()

        try:
            self.surface[0] = pygame.image.load(file)
        except:
            print("No se ha podido encontrar el archivo %s"%file)
            sys.exit()


        self.rect =  self.surface[0].get_rect()
        self.rect[:2] = [posx,posy]
        self.posix = posx
        self.posiy = posy

    def AddFrame(self,file):
        self.frame += 1

        try :
            self.surface[self.frame] = pygame.image.load(file)
        except :
            print("No se ha podido encontrar el archivo :",file)
            sys.exit()

    def CurrentTime(self) :
        self.fin_milisegundos=pygame.time.get_ticks()
        return self.fin_milisegundos-self.ini_milisegundos

    def Animar(self,vel):
        self.frametime=self.CurrentTime()
        if self.frametime < vel:
             self.frametime=self.CurrentTime()
        else:
            self.ini_milisegundos=pygame.time.get_ticks()
            if self.frameact >= self.frame:
                self.ini_milisegundos=pygame.time.get_ticks()
                self.frameact = 0
            else:
                self.ini_milisegundos=pygame.time.get_ticks()
                self.frameact += 1

        pantalla.screen.blit(self.surface[self.frameact],self.rect)



    def PosicionIX(self):
        return self.posix

    def PosicionIY(self):
        return self.posiy

    def Transparencia(self,color):
        self.surface[self.frame].set_colorkey(color)

    def Alpha(self,value):
        self.surface[self.frame].set_alpha(value,pygame.RLEACCEL)

    def Dibujar(self,arg =False):

        if arg == True :
           self.rect[:2] = [self.posix-self.rect[2]/2,self.posiy-self.rect[3]/2 ]


        pantalla.screen.blit(self.surface[self.frame],self.rect)

    def Mover(self,posx,posy):
        self.rect.move_ip(posx,posy)

    def ObtenerPos(self):
        return self.rect[:2]

    def ObtenerX(self):
        return self.rect[0]

    def ObtenerY(self):
        return self.rect[1]

    def ObtenerW(self):
        return self.rect[3]

    def ObtenerH(self):
        return self.rect[4]
    def Posicion(self,posx,posy):
        self.rect[:2] = [posx,posy]
        self.posix = posx
        self.posiy = posy
    def PosicionX(self,posx):
        self.rect[0] = posx

    def PosicionY(self,posy):
        self.rect[1] = posy

    def MoverX(self,vel):
        self.rect.move_ip(vel,0)

    def MoverY(self,vel):
        self.rect.move_ip(0,vel)


    def Distanciax(self,otro):
       return abs(self.ObtenerX()-otro.ObtenerX())

    def Distanciay(self,otro):
       return abs(self.ObtenerY()-otro.ObtenerY())

    def Colisiona(self,otro):
          return self.rect.colliderect(otro.rect)


class Raton :


    def __init__(self):

            self.ratonmask = Graficos("img/menu/raton.png")
            self.raton = Graficos("img/menu/mask.png")

            self.rect = self.raton.rect



            self.ratonmask.Transparencia((0,255,0))



    def Dibujar(self):

                    self.ratonmask.Dibujar()

    def Posicionar(self):

                self.rect[:2] = pygame.mouse.get_pos()
                self.ratonmask.Posicion(self.rect[0],self.rect[1])
                #self.raton.Posicion(self.rect[0],self.rect[1])
pygame.mixer.init(44100,-16,2, 1024 * 3)
class Sonido :
    def __init__(self,file):
        try:
            self.sonido = pygame.mixer.Sound(file)
        except:
            print("No se ha podido encontrar el archivo :",file)
            sys.exit()

    def play(self,loop = 0):
        self.sonido.set_volume(float(Volumen)/100)
        if loop == 0 :
            self.sonido.play()
        else : self.sonido.play(loop)
    def fadeout(self,time):
        self.sonido.fadeout(time)
    def stop(self):
        self.sonido.stop()

Musica = pygame.mixer.music


try :
    fconf = open("img/opciones/setup.conf","r")

    Opcion = [None,None,None]

    opcion = fconf.readline()
    Opcion[0] = int(opcion[:1])
    Opcion[1] = int(opcion[1:2])
    Opcion[2] = int(opcion[2:])
    fconf.close()
except :
    fconf = open("img/opciones/setup.conf","w")
    fconf.write("00100")
    Opcion = [None,None,None]

    Opcion[0] = 0
    Opcion[1] = 0
    Opcion[2] = 100


if Opcion[0] == 0:
    completa = (pygame.DOUBLEBUF|pygame.RLEACCEL)
else:
    completa = (pygame.RLEACCEL|pygame.FULLSCREEN)

IDIOMA = Opcion[1]

if Opcion[2] < 0 or Opcion[2] > 100:
    Volumen = 50
else: Volumen = Opcion[2]
Musica.set_volume(float(Volumen)/100)



del fconf

FPS = pygame.time.Clock()
def Update():

    FPS.tick(60)



    pantalla.actualizar()


pygame.init()
pygame.display.set_caption(":: XineSoft :: Thinkin'in Game.")
icon = pygame.image.load("img/menu/icono.gif")
icon.set_colorkey((255,255,255))
pygame.display.set_icon(icon)
raton =  Raton()


pantalla = Pantalla((640,480),completa )
pygame.mouse.set_visible(0)
fps = Timer(30)


modo = 0
