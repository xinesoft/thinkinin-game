from xs import *
import puntuacion,xs
from graficos import *
sonar = 1    
def Cargar(indice,punt):
    global logo
    global brecord
    global continuar
    global continuar2
    global pizarra
    global puntuacio
    global texto
    global pizarra
    global maximo
    global sonar
    sonar = 1
    if int(punt) > int(puntuacion.puntuaciones[indice]):
              puntuacion.salvarPunto(indice,punt)
              max = 1
    else : max = 0
    maximo = max
    logo = Graficos("img/resultado/%s/logo.png"%xs.IDIOMA,pantalla.Ancho()/2,100)
    brecord = Graficos("img/resultado/%s/record.png"%xs.IDIOMA,pantalla.Ancho()/2,pantalla.Alto()/2+20)
    continuar = Graficos("img/resultado/%s/continuar.png"%xs.IDIOMA,pantalla.Ancho()/2,370)
    continuar2 = Graficos("img/resultado/%s/_continuar.png"%xs.IDIOMA,pantalla.Ancho()/2,370)    
    texto = Fuentes("fonts/tiza.ttf",200)
    texto.Color((225,225,0))
    puntuacio = float(punt)
    Dibujar()
def Dibujar():   
    done = 0
    punt = 0
    activarc = 0
    sonar = 1
    while not done:
        for event in pygame.event.get():
           
            if event.type ==  MOUSEMOTION:
                raton.Posicionar()
            if event.type == MOUSEBUTTONDOWN:
                if continuar.Colisiona(raton) and activarc ==1:
                    click.play()
                    done = 1
            if event.type == MOUSEMOTION:
                raton.Posicionar()
                
                
        pizarra.Dibujar(1)
        logo.Dibujar(1)
        if punt < puntuacio :
            punt +=1
        else :
            if activarc == 0:               
                timer0 = Timer(1000) 
            activarc = 1
            
        texto.Dibujar(punt,pantalla.Ancho()/2,pantalla.Alto()/2+20,1,1)
        if activarc == 1:
            if timer0.End():
                if maximo == 1:
                    brecord.Dibujar(1)
                    
                
                
            
                if continuar.Colisiona(raton):
                    if sonar == 1:
                        clack.play()
                        sonar = 0
                    
                    continuar2.Dibujar(1)            
                else: continuar.Dibujar(1)   ;sonar = 1                       
        raton.Dibujar()
        pantalla.actualizar()    

def CargarE(punt):
    global logo
    global brecord
    global continuar
    global continuar2
    global pizarra
    global puntuacio
    global texto
    global pizarra
    global maximo
    global sonar
    global nombres
    sonar = 1
    if punt > puntuacion.cexamen:              
              max = 1
    else : max = 0
    maximo = max
    logo = Graficos("img/resultado/%s/logo.png"%xs.IDIOMA,pantalla.Ancho()/2,100)
    brecord = Graficos("img/resultado/%s/record.png"%xs.IDIOMA,pantalla.Ancho()/2,pantalla.Alto()/2+20)
    continuar = Graficos("img/resultado/%s/continuar.png"%xs.IDIOMA,pantalla.Ancho()/2,370)
    continuar2 = Graficos("img/resultado/%s/_continuar.png"%xs.IDIOMA,pantalla.Ancho()/2,370)    
    texto = Fuentes("fonts/tiza.ttf",200)
    texto.Color((225,225,0))
    nombres = Graficos("img/resultado/%s/nombre.png"%xs.IDIOMA,pantalla.Ancho()/2,200)
    print(punt)
    puntuacio = punt
    DibujarE()
    if max == 1:
        MeterNombre()
def MeterNombre():
    sonar = 1
    texto = Fuentes("fonts/tiza.ttf",75)
    texto.Color((225,225,0))
    done = 0
    nombre = ""
    while not done:
        
        for event in pygame.event.get():
           
            if event.type ==  MOUSEMOTION:
                raton.Posicionar()
            if event.type == MOUSEBUTTONDOWN:
                if continuar.Colisiona(raton) :
                    if len(nombre) >= 3:                            
                        click.play()
                        puntuacion.sExamen(puntuacio,nombre)
                        done = 1
            if event.type == MOUSEMOTION:
                raton.Posicionar() 
            if event.type == KEYDOWN:               
                if len(nombre) < 7:                                  
                     if event.key >= K_a and event.key <= K_z:                   
                                nombre += "%c"%event.key
                                break
                if event.key == K_BACKSPACE and len(nombre) != 0:
                    nombre = nombre[:-1]
                if event.key == K_RETURN and len(nombre) >= 3:
                    puntuacion.sExamen(puntuacio,nombre)
                    done = 1
                    
                
            
               
                                         
                    
                      
        pizarra.Dibujar(1)
        logo.Dibujar(1)
        nombres.Dibujar(1)
        if not len(nombre) == 0:
            texto.Dibujar(nombre,pantalla.Ancho()/2,pantalla.Alto()/2+40,1,1)  
        else : texto.Dibujar("_",pantalla.Ancho()/2,pantalla.Alto()/2+40,1,1) 
        
        if continuar.Colisiona(raton) and  len(nombre) >= 3:
            if sonar == 1:
                        clack.play()
                        sonar = 0
            continuar2.Dibujar(1)            
        else : continuar.Dibujar(1) ;sonar = 1 
        
        raton.Dibujar()        
        pantalla.actualizar()
        
def DibujarE():   
    done = 0
    punt = 0
    sonar = 1
    activarc = 0
    while not done:
        for event in pygame.event.get():
            
            if event.type ==  MOUSEMOTION:
                raton.Posicionar()
            if event.type == MOUSEBUTTONDOWN:
                if continuar.Colisiona(raton) and activarc ==1:
                    click.play()
                    done = 1
            if event.type == MOUSEMOTION:
                raton.Posicionar()
                
                
        pizarra.Dibujar(1)
        logo.Dibujar(1)
        if punt >= puntuacio:
            punt = puntuacio
        elif punt != puntuacio :
            punt +=0.1
     
        if activarc == 0:               
                timer0 = Timer(1000) 
                activarc = 1
            
        texto.Dibujar(punt,pantalla.Ancho()/2,pantalla.Alto()/2+20,1,1)
        if activarc == 1:
            if timer0.End() and punt >= puntuacio:
                if maximo == 1:
                    brecord.Dibujar(1)
                    
                
                
            
                if continuar.Colisiona(raton):
                    if sonar == 1:
                        clack.play()
                        sonar = 0
                    continuar2.Dibujar(1)            
                else: continuar.Dibujar(1)  ;sonar = 1                        
        raton.Dibujar()
        pantalla.actualizar() 

                   
