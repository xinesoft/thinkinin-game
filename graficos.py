from xs import *
pizarra = Graficos("img/menu/bpizarra.png")
pizarra.Posicion(pantalla.Ancho()/2,pantalla.Alto()/2)
comentario = Graficos("img/menu/comentario.png",300,175)
comentario.Alpha(175)
        
caracolhabla = Graficos("img/caracol/hablar/0.png",300,275)
for n in range(1,13):
    caracolhabla.AddFrame("img/caracol/hablar/%s.png"%n)
            
caracol = Graficos("img/caracol/mover/0.png",300,275)
for n in range(1,11):
    caracol.AddFrame("img/caracol/mover/%s.png"%n)
def Musica(): 
    menumus = Sonido("musica/intro.ogg")
    click = Sonido("musica/click.ogg")
    clack = Sonido("musica/clack.ogg")   
    
menumus = Sonido("musica/intro.ogg")
click = Sonido("musica/click.ogg")
clack = Sonido("musica/clack.ogg")
