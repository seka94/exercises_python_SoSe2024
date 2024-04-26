## Schreiben Sie eine Funktion namens steigungs_funktion(), die die Steigung der druch zwei 
# Punkte verlaufen Geraden berechnet. Die funktion nimmt deine Liste mit vier Element als Argument.
# De ersten beiden Elemente sind die x-y-Koordinaten des ersten Punktees und das dritte und vierte Element dfer liste..


def steigung_funktion(x1, y1, x2, y2):
   
 #   meineListe = [x1, y1, x2, y2]
    
    x0 = x1 - x2
    y0 = y1 - y2
    
    if x0 == 0:
        print ("Die Steigung ist nicht definiert")
        
    elif y0 == 0:
        print ("Die Gerade ist waagrecht")
        
    else: 
        m = x0/y0
        print ("Die Gerade hat eine Steigung von", m)




# Hier kommt die MusterLösung

def steigungfunktion1(liste):
  
    x1 = liste[0]
    y1 = liste[1]
    x2 = liste[2]
    y2 = liste[3]
    
    delta_x = x2-x1
    delta_y = y2-y1
    
    if delta_x == 0:
        print ("Die Steigung ist nicht definiert")
    
    else:
        steigung = delta_y/delta_x
        print (steigung)
    
    

        
steigungfunktion1([4, 4, 8, 4])