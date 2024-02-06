import random

amici = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# lunghezza della lista: in questo caso è 4
lunghezza_amici = len(amici)

# numero a caso tra 0 e 4
randomizzazione = random.randint(0 , lunghezza_amici - 1)

# prende il nome all'interno della lista corrispondente al numero randomico uscito
persona_che_paghera = amici[randomizzazione]

print (persona_che_paghera + " pagherà il conto oggi!")