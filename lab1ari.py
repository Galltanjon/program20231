"""Aritmetisk följd där differensen mellan två element är konstant. 
Input från användare: första elementet a1, differensen d, antal element n.
Utifrån dessa kan vi få ut värdet an på element n, samt talföljdens summa san"""

element1 = int(input("Vad är det första talet i talföljden? "))
differens = int(input("Vad är talföljdens differens? "))
antal_element = int(input("Hur många element ska beräknas? "))

element_n = int(element1 + differens * (antal_element - 1))
summa_element = int(antal_element * ((element1 + element_n) / (2))) 

print("\nSista elementet i talföljden har värdet:", element_n)
print("Summan av talföljden är:", summa_element)