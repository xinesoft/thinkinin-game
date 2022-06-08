from xs import *
import graficos

def Ver():        
    Update()
    logo = Graficos("img/menu/creditoses.png",pantalla.Ancho()/2,pantalla.Alto()/2)   
    logo2 = Graficos("img/menu/intro.png",pantalla.Ancho()/2,pantalla.Alto()/2.5) 
    logo.Dibujar(1)
    Update()
    timer = Timer(7000)    
    while not timer.End():
        for event in pygame.event.get():              
                if event.type == MOUSEMOTION:
                    raton.Posicionar()
        logo.Dibujar(1)     
        raton.Dibujar()
        Update()
    timer = Timer(3000)
    while not timer.End():
        for event in pygame.event.get():              
                if event.type == MOUSEMOTION:
                    raton.Posicionar()
        logo2.Dibujar(1)  
        
        raton.Dibujar()
        Update()
    