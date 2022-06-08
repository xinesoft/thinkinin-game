import pygame
from xs import  *
from pygame.locals import *
grafico = Graficos("img/raton.png",100,100)

posicionnueva=[0,0]
posicionr=[0,0,0,0]
posicion = pygame.mouse.get_pos()
activar = 0
while(1):
    
     
    for event in pygame.event.get():                

        if event.type == QUIT :
                    sys.exit()
        if event.type == MOUSEMOTION:
                    raton.Posicionar()
               
        if event.type == KEYDOWN :                   
       
            if event.key == K_ESCAPE:
                            self.salir = 1
        if event.type == MOUSEBUTTONDOWN:
                mousebutton = pygame.mouse.get_pressed()
                if mousebutton[0] :
                   posicion = pygame.mouse.get_pos()
                   activar = 1
        if event.type == MOUSEBUTTONUP:
                posicionr = [posicion,[posicionnueva[0]-posicion[0],posicionnueva[1]-posicion[1]]]
                
                posicionnueva[:2] = [0,0]
    
    
    
    if activar == 1:
        posicionnueva[:2] = pygame.mouse.get_pos() 
        pygame.draw.rect(pantalla.screen,[255,255,255],[posicion,[posicionnueva[0]-posicion[0],posicionnueva[1]-posicion[1]]],1)               
   
   
    if grafico.rect.colliderect(posicionr):        
       grafico.Mover(1,1)
        
        
        
    grafico.Dibujar()    
               
    
    raton.Dibujar()
    Update()
    
        
                   
                    