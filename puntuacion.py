examen = 0.0

def cargarPuntos():
    global file
    file = open("img/opciones/scores","r")
    global puntuaciones 
    puntuaciones = file.readlines()  
      
     
    file.close()

def salvarPunto(indice,puntos):
    puntuaciones[indice] = str(puntos)+"\n"

    file = open("img/opciones/scores","w")
    for x in range(len(puntuaciones)):
        file.write(puntuaciones[x])
    file.close()
    

def Borrar():
    file = open("img/opciones/scores","w")
    for x in range(10):
        file.write("0\n")    
    file.close()    
    file =  open("img/opciones/examen","w")
    file.write("0\nnombrE")
    cexamen = 0
    cnombre = "nombrE"
    file.close()
    cargarPuntos()
    cExamen()
    
def cExamen():
    global cexamen
    global cnombre
    try:
        file = open("img/opciones/examen","r")
        cexamen = float(file.readline())
        
        cnombre = file.readline()        
        
        file.close()
    except:
        file =  open("img/opciones/examen","w")
        file.write("0\nnombrE")        
        cexamen = 0
        cnombre = "nombrE"
        file.close()

def sExamen(puntos,nombre):
    file =  open("img/opciones/examen","w")
    file.write(str(puntos)+"\n")   
    file.write(nombre)
    file.close()
        
        
    
    

