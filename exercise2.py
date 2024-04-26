
import math

# Schreiben Sie eine Funktion, die zwei Argumente x und y
# annimmt und schreibt "x ist duch y teilbar", wenn x durch
# y teilbar ist, ansonsten schreibt 
#"x ist nicht durch y teilbar"
#

def teilbar(x,y):
    
    tr = x%y # Hier wird mit dem Modulo-Operator der Restwert ermittelt.
     
    if tr == 0: # Hier wird geschaut, ob der Restwert null is
        print ("x ist durch y teilbar")
               
    else:
        
        if tr != 0:
            
            print ("x ist nicht durch y teilbar")
 

# Hier kommt die Lösung von bramm

def teilbarLösung(x, y):
    if y == 0:
        print ("x ist nicht möglich durch Null zu teilen")
    elif x == y:
        print ("x und y sind gleich")
    else: 
        if x%y == 0:
            print ("x ist durch y teilbar")
        else: 
            print ("x ist nicht durch y teilbar")

#teilbar(14,3)               


teilbarLösung(2,0)

