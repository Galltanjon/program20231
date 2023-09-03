"""Aritmetisk följd där differensen mellan två element är konstant. 
Variabeln a1 är första elementet i följden, differensen är d, 
godtyckligt element i följden är an och summan är san.
a1, d och n söks"""

a1 = int(input("Vad är det första talet i talföljden? "))
d = int(input("Vad är talföljdens differens? "))
n = int(input("Hur många element ska beräknas? "))

an = int(a1 + d * (n - 1))
san = int(n * ((a1 + an) / (2))) 

print("\nSista elementet i talföljden har värdet", an)
print("Summan av talföljden blir", san)