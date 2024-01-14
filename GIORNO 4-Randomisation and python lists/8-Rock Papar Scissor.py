import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
0
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    scelta = int(input("Cosa scegli: premi 0 per sasso, 1 per carta, 2 per forbici:\n"))
    if scelta in [0, 1, 2]:
        break
    else:
        print("Hai scelto un numero errato. Per favore, scegli 0, 1 o 2.")
        
if scelta == 0:
    print (rock)
elif scelta == 1:
    print (paper)
else:
    print (scissors)
    
print ("Il computer ha scelto: ")

random_integer = random.randint (0,2)

if random_integer == 0:
    print (rock)
elif random_integer == 1:
    print (paper)
else:
    print (scissors)

if scelta == 0 and random_integer == 0:
    print ("Pareggio!")
elif scelta == 0 and random_integer == 1:
    print ("Hai perso!")
elif scelta == 0 and random_integer == 2:
    print ("Hai vinto!")
elif scelta == 1 and random_integer == 1:
    print ("Pareggio!")
elif scelta == 1 and random_integer == 2:
    print ("Hai perso!")
elif scelta == 1 and random_integer == 0:
    print ("Hai vinto!")
elif scelta == 2 and random_integer == 2:
    print ("Pareggio!")
elif scelta == 2 and random_integer == 1:
    print ("Hai vinto!")
else:
    print ("Hai perso!")

