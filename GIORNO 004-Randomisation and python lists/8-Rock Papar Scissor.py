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


mia_scelta = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if mia_scelta == 0:
    print(rock)
elif mia_scelta == 1:
    print(paper)
else:
    print(scissors)

print ("Computer chose:")

scelta_pc = random.randint(0,2)

if scelta_pc == 0:
    print(rock)
elif scelta_pc == 1:
    print(paper)
else:
    print(scissors)

if mia_scelta == 0 and scelta_pc == 1:
    print("YOU LOST")
elif mia_scelta == 1 and scelta_pc == 0:
    print("YOU WON")
elif mia_scelta == 1 and scelta_pc == 2:
    print("YOU LOST")
elif mia_scelta == 2 and scelta_pc == 1:
    print("YOU WON")
elif mia_scelta == 0 and scelta_pc == 2:
    print("YOU WON")
elif mia_scelta == 2 and scelta_pc == 0:
    print("YOU LOST")
else:
    print ("DRAW")