
def buchstaben_zählen(Wort):
    
     y = 0    
     liste =list(Wort)
     x = len(liste)
     print(x)
     
     for char in liste:
         if char.isalpha():
            y += 1

     print(y)
    
    
buchstaben_zählen("Hallo, Berlin!!!!")

#exercise 8


def vokon_zählen(WWort):
    
    vo = 0
    ko = 0
    
    vokale = ("aeiou")
    konsonanten = ("bcdfghjklmnpqrstvwxyzäöüß")
   
    w = WWort
    lw = w.lower()
    
    
    for i in lw:
        if i.isalpha():
           if i in vokale:
               vo +=1
        
           if i  in konsonanten:
               ko +=1
               
    
           
           
    print(lw)
    
    print("Es gibt in dem Wort", WWort, vo, "Vokale und", ko, "Konsonanten")
    
    print(f"""Es gibt in dem Wort "{WWort}" {vo} Vokale und {ko} Konsonanten. """)

vokon_zählen("HI,&%/ BerliN!!")
    
    
    