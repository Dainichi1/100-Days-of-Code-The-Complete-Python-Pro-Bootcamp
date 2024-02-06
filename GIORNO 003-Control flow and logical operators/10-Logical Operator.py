print ("Benvenuti alle Montagne Russe!")
altezza = int(input("Quanto sei alto in centimetri?"))
bill = 0

if altezza >= 120:
    print("Puoi salire!")
    età = int(input("Quanti anni hai?"))
    # minore di 12 anni
    if età < 12:
        bill = 5
        print("Il prezzo per i bambini è 5 euro.")
    # tra 12 e 18 anni
    elif età <= 18:
        bill = 7
        print("Il prezzo per gli adolescenti è 7 euro.")
    # età compresa tra 45 e 55
    elif età >= 45 and età <= 55:
        print("Biglietto gratis!")
    #maggiore di 18 anni
    else:
        bill = 12
        print("Il prezzo per gli adulti è 12 euro.")
        
    vuoi_foto = input ("Vuoi una foto? Y o N.")
    if vuoi_foto == "Y":
        bill += 3
    print (f"Il prezzo finale è: {bill}")
        
else:
    print("Non puoi salire!")