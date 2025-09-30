import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
image_lst=[rock,Paper,Scissors]

user_choice=int(input("Enter your choice:0/1/2 : "))

if user_choice>=0 and user_choice<=2:
    print(image_lst[user_choice])

    computer_choice = random.randint(0, 2)
    print(image_lst[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice > user_choice:
        print("Computer win")
    elif computer_choice == user_choice:
        print("It's a draw")
else:
    print("You entered the wrong choice")