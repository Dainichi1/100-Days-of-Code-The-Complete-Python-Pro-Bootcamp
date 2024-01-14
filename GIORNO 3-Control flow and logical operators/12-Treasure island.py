print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

prima_decisione = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if prima_decisione == "left":
    seconda_decisione = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if seconda_decisione == "wait":
        terza_decisione = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if terza_decisione == "red":
            print ("It's a room full of fire. Game over.")
        elif terza_decisione == "yellow":
            print ("You found the trasure. You win")
            print( '''  _,-""._                       
        _,-",~@);%~`-._               
        \\""""""------"-...___         
         |""""""------/|      |     
         |      |HHHHH||      |       
         |""""""------||      |       
         |      _____ ||      |        
         |     : ___ :||      |        
         |     :|GSN|:||      |         
         |     :|___|:||      |        
         |     :""""":||      |          
         |"""""-------||      |         
         || ,~@);~.  |||      |        
         ||~  ===  ~ |||      |        
         |"""""-------||      |         
         |"""""-------||      |         
         || ,~@);~.  |||      |       
         ||~  ===  ~ |||      |       
         |"""""-------||      |      
        /""""""-------\\....___\      
      """""""---------....___: ''')
        elif terza_decisione == "blue":
            print ("You enter a room full of beasts. Game over.")
        else:
            print ("You chose a door that doesen't exists. Game over.")
    else:
        print("Attacked by trout.Game Over")
else:
    print ("Fall into a hole.Game Over.")


