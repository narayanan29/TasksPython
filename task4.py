
print("welcome to TREASURE ISLAND")
print("Your mission is to find the treasure....")
choice1=input("You're in the cross road ,Where did you want to go? Type 'left' or 'right' \n").lower()
if choice1=='left':
    choice2=input("You're in the lake there is island in the mid of the lake "
                  "type 'wait' wait for boat"
                  "type 'swim' to swim across the lake").lower()
    if choice2=='wait':
        choice3=input("You're arrived in the island "
                      "There is house with three doors"
                      "'yellow','red','blue'"
                      "which door did you select? ").lower()
        if choice3=='red':
            print("You won the treasure ha ha aha ah aha")
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
            /______/______/______/______/______/______/______/______/______/______/[TomekK]
            *******************************************************************************

            ''')
        elif choice3=='yellow':
            print("You opened the lion door you killed")
        elif choice3=='blue':
            print("you opened the hell door you lose")
        else:
            print("You Entered the wrong value you lose")
    else:
        print("The lake is full of crocodile you killed")
else:
    print("You choose wrong way you lose")