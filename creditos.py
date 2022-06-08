from xs import *

def Ver():
    pantalla.Color((200,200,200))
    Update()
    logo = Graficos("img/menu/intro.png",pantalla.Ancho()/2,pantalla.Alto()/2.5)
    texto = Fuentes("fonts/tiza.ttf",40)
    logo.Dibujar(1)
    Update()
    timer = Timer(8000)
    timer2 = Timer(3000)   
    
    while not timer.End():
        for event in pygame.event.get():              
                if event.type == MOUSEMOTION:
                    raton.Posicionar()
        logo.Dibujar(1)
        if timer2.End():
           texto.Dibujar("PRESENTA...",350,350,1) 
        raton.Dibujar()
        Update()
    
    
    

    
    