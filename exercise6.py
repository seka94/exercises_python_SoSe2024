
a = 1
r = 0.5
s = 0
k = 0
Grenzwert = 1/(1-r)
Epsilon = 0.00000000000000000000000000000000001


while True:
    s += a * r**k
    k += 1
    print(s, end = " ")
    
    if (Grenzwert - s) < Epsilon:
       break
        
