import random

amici = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

lunghezza_amici = len(amici)

randomizzazione = random.randint(0 , lunghezza_amici - 1)

persona_che_paghera = amici[randomizzazione]

print (persona_che_paghera + " pagherà il conto oggi!")