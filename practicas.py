from xs import *
import xs
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
from graficos import pizarra,clack,click,comentario,caracol,caracolhabla,menumus


puntuacion.cargarPuntos()

class Practicas:
    def Cargar(self):
        self.blogo = Graficos("img/practicas/%s/logo.png"%xs.IDIOMA)
        self.blogo.Posicion(pantalla.Ancho()/2,100)
        self.bvolver = Graficos("img/practicas/%s/volver.png"%xs.IDIOMA)
        self.bvolver.Posicion(100,pantalla.Alto()-80)
        self.bvolver1 = Graficos("img/practicas/%s/volver1.png"%xs.IDIOMA)
        self.bvolver1.Posicion(100,pantalla.Alto()-80)
        self.bpruebas = Graficos("img/practicas/%s/pruebas.png"%xs.IDIOMA)
        self.bpruebas.Posicion(pantalla.Ancho()/4,200)
        if xs.IDIOMA == 0:
            self.titulos = ["Algebra","Signo","Contar Dinero","Contar Monedas","Lógica","Buscar Pareja"]+\
                           ["Buscar Única","Memorizar Número","Memorizar Fichas","Simón"]
        else : self.titulos = ["Algebra","Sing","Count Money","Count Coins","Logic","Search the Pair"]+\
                              ["Search the Only","Memorize Number","Memorize Cards","Simon"]

    def __init__(self):
        xs.modo = 0
        self.animar = 0
        pantalla.Color((200,200,200))


        self.Cargar()

        self.Pruebas = [Calculo,Calculo2,Monedas,Monedas2,Prueba5,Parejas,Carta,Memorizar,ParejasHide,Simon]

        self.savance = clack
        self.sonar = list(range(11))
        for x in self.sonar : self.sonar[x] = 0


        self.texto = Fuentes("fonts/tiza.ttf",26)
        self.texto.Color((255,0,0))
        self.fuente = Fuentes("fonts/fuente.ttf",12)
        self.fuente.Color((255,255,255))
        self.ftitulo = Fuentes("fonts/fuente.ttf",20)
        self.ftitulo.Color((255,150,0))
        self.boton = {}
        self.oboton = {}



        posx = pantalla.Ancho()/8
        posx2 = pantalla.Ancho()/8
        for n in range(1,11):
            if n < 6 :
                self.boton[n] = Graficos("img/practicas/%d.png"%n,posx,275)
                self.oboton[n] = Graficos("img/practicas/_%d.png"%n,posx,275)
                posx+=40
            else :
                self.boton[n] = Graficos("img/practicas/%d.png"%n,posx2,325)
                self.oboton[n] = Graficos("img/practicas/_%d.png"%n,posx2,325)
                posx2+=40


        self.CargarP()
        self.Dibujar()
    def CargarP(self):
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
            self.txt[8] = "Memoriza cartas en 5 segundos."
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


    def Dibujar(self):
        done = 0
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
                        for n in self.boton:
                                if self.boton[n].Colisiona(raton):
                                    click.play()
                                    menumus.fadeout(1000)
                                    prueba = self.Pruebas[n-1]()
                                    del prueba
                                    Musica.stop()
                                    menumus.play(-1)
                                    break
                        if self.bvolver.Colisiona(raton):
                            done = 1



            pizarra.Dibujar(1)
            self.blogo.Dibujar(1)
            comentario.Dibujar(0)
            self.bpruebas.Dibujar(1)

            if self.animar == 0:
                    caracol.Animar(200)
            else :

                caracolhabla.Animar(200)
            if self.bvolver.Colisiona(raton):
                if self.sonar[10] == 1:
                                self.savance.play()
                                self.sonar[10] = 0
                self.bvolver1.Dibujar(1)
                self.DibujarP(10)
            else :
                self.bvolver.Dibujar(1)
                self.sonar[10] = 1
                self.txta[10] = 0
                self.txti[10] =""
            self.animar = 0
            for n in self.boton:
                if self.boton[n].Colisiona(raton):

                    if self.sonar[n-1] == 1:
                        self.savance.play()
                        self.sonar[n-1] = 0

                    self.oboton[n].Dibujar(1)
                    self.ftitulo.Dibujar(self.titulos[n-1],320,190,1)
                    self.DibujarP(n-1)
                    if xs.IDIOMA == 0:
                        self.fuente.Dibujar("Puntuación Máxima : ",368,273,1)
                    else : self.fuente.Dibujar("Best Score : ",420,273,1)
                    self.texto.Dibujar(int(puntuacion.puntuaciones[n-1]),506,280,1,1)
                    self.animar = 1
                else :
                    self.boton[n].Dibujar(1)
                    self.sonar[n-1] = 1
                    self.txta[n-1] = 0
                    self.txti[n-1] =""




            raton.Dibujar()
            Update()


