import random
puntajeN=0
puntajeB=0
listaKN=""
posicionKN=""
listaKB=""
posicionKB=""

uno=['  ','  ','  ','  ','  ','  ','  ','  ']
dos=['  ','  ','  ','  ','  ','  ','  ','  ']
tres=['  ','  ','  ','  ','  ','  ','  ','  ']
cuatro=['  ','  ','  ','  ','  ','  ','  ','  ']
cinco=['  ','  ','  ','  ','  ','  ','  ','  ']
seis=['  ','  ','  ','  ','  ','  ','  ','  ']
siete=['  ','  ','  ','  ','  ','  ','  ','  ']
ocho=['  ','  ','  ','  ','  ','  ','  ','  ']

def posicionRey(jugador,lista,posicion,tipoPieza):
    global listaKN
    global posicionKN
    global listaKB
    global posicionKB

    if (tipoPieza=="K"):
        if (jugador=="N"):
            listaKN=lista
            posicionKN=posicion
        else:
            listaKB=lista
            posicionKB=posicion

def asignoTablero(jugador,cantidadPiezas,tipoPieza):
    global uno
    global dos
    global tres
    global cuatro
    global cinco
    global seis
    global siete
    global ocho
    
    i=1

    while(i<=cantidadPiezas):
        bandera=True
        while(bandera):
            lista=random.randint(1,8)
            posicion=random.randint(0,7)
            if (lista==1):
                if (uno [posicion]!='  '):
                    continue
                else:
                    uno [posicion]=tipoPieza+jugador
                    bandera=False
            elif (lista==2):
                if (dos [posicion]!='  '):
                    continue
                else:
                    dos [posicion]=tipoPieza+jugador
                    bandera=False
            elif (lista==3):
                if (tres [posicion]!='  '):
                    continue
                else:
                    tres [posicion]=tipoPieza+jugador
                    bandera=False
            elif (lista==4):
                if (cuatro [posicion]!='  '):
                    continue
                else:
                    cuatro [posicion]=tipoPieza+jugador
                    bandera=False
            elif (lista==5):
                if (cinco [posicion]!='  '):
                    continue
                else:
                    cinco [posicion]=tipoPieza+jugador
                    bandera=False
            elif (lista==6):
                if (seis [posicion]!='  '):
                    continue
                else:
                    seis [posicion]=tipoPieza+jugador
                    bandera=False
            elif (lista==7):
                if (siete [posicion]!='  '):
                    continue
                else:
                    siete [posicion]=tipoPieza+jugador
                    bandera=False
            elif (lista==8):
                if (ocho [posicion]!='  '):
                    continue
                else:
                    ocho [posicion]=tipoPieza+jugador
                    bandera=False
                    
        posicionRey(jugador,lista,posicion,tipoPieza)
        i=i+1

def puntaje(jugador,tipoPieza,cantidadPiezas):
    global puntajeN
    global puntajeB

    if (tipoPieza=="P"):
        pieza=1
    if (tipoPieza=="C"):
        pieza=3
    if (tipoPieza=="A"):
        pieza=3
    if (tipoPieza=="T"):
        pieza=5
    if (tipoPieza=="Q"):
        pieza=9
    if (tipoPieza=="K"):
        pieza=4

    parcial=cantidadPiezas*pieza
    if (jugador=="N"):
        puntajeN=puntajeN+parcial
    else:
        puntajeB=puntajeB+parcial

def pieza(jugador,tipoPieza):
        cantidadPiezas=0
        
        if (tipoPieza=="P"):
            cantidadPiezas=random.randint(0,8)
            
        elif (tipoPieza=="C"):
            cantidadPiezas=random.randint(0,2)
            
        elif (tipoPieza=="A"):
            cantidadPiezas=random.randint(0,2)
            
        elif (tipoPieza=="T"):
            cantidadPiezas=random.randint(0,2)
            
        elif (tipoPieza=="Q"):
            cantidadPiezas=random.randint(0,1)
            
        elif (tipoPieza=="K"):
            cantidadPiezas=1
           
            
        puntaje(jugador,tipoPieza,cantidadPiezas)
        asignoTablero(jugador,cantidadPiezas,tipoPieza)

pieza("N","P")
pieza("B","P")
pieza("N","C")
pieza("B","C")
pieza("N","A")
pieza("B","A")
pieza("N","T")
pieza("B","T")
pieza("N","Q")
pieza("B","Q")
pieza("N","K")
pieza("B","K")

print("")

lista=[uno,dos,tres,cuatro,cinco,seis,siete,ocho]
for i in range (8):    
    print(lista [i])

print("")
print ("Puntaje negras: "+ str(puntajeN))
print ("Puntaje blancas: "+ str(puntajeB))
