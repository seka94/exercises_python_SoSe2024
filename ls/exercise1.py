
def cagr_berechnung(AK, EK, t):
  
    akabs = abs(AK)
    ekabs = abs(EK)
    tabs = abs(t)
    
    r = (ekabs/akabs)**(1/tabs)-1
    r = r * 100
    return r


cagr_berechnung(100, 700, 30)



AK = 120
t = 30 
CAGR = cagr_berechnung(100, 700, 30)
EK = AK * (1 + CAGR)**t

print(EK)