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



is_on = True
while is_on:
    cross_road = input(
        'You\'re at a cross road. where do you want to go? Type "left" or "right"\n').lower()
    if cross_road == "left":
        lake = input(
            'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim acroos.\n').lower()
        if lake == "wait":
            doors_color = input(
                "you arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose?\n").lower()
            if doors_color == "yello":
                print("You chose a door that doesn't exist. Game Over!")
            elif doors_color == "red":
                print("It's a room full of fire. Game Over!")
            elif doors_color == "blue":
                print("You enter a room of beasts. Game Over!")
            else:
                print("You chose a door that doesn't exist. Game Over!")
        elif lake == "swim":
            print("You get attacked by an angry trout. Game Over!")
        else:
            print("You type another way. Please try again!")
    else:
        print("You fell into a hole. Game over!")
    if input("You again play this game? (Type 'y' or 'n'): ") == 'y':
        is_on = False