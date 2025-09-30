#humgman
#Final
import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
 /    |
      |
=========''']

word_lst=["hello","world","pyhton","Artificial","Intelligence","generative"]
chosen_wrd=random.choice(word_lst)
print(chosen_wrd)
live=0
         # step1
# guess=input("Guess a letter : ").lower()
# print(guess)
#
# for letter in chosen_wrd:
#     if letter == guess:
#         print("right")
#     else:
#         print("Wrong")

#                 #step2
# placeholder=""
# wrd_len=len(chosen_wrd)
# for i in range(wrd_len):
#     placeholder+="-"
# print(placeholder)
#
# guess=input("Guess a letter : ").lower()
# print(guess)
#
# password=""
# for letter in chosen_wrd:
#     if letter == guess:
#         password+=letter
#     else:
#         password+="-"
# print(password)
                #step3
correct_letter=[]
game_over=False
while not game_over:
    guess=input("Enter your guess:").lower()

    display=""
    for letter in chosen_wrd:
        if letter == guess:
            display+=guess
            correct_letter.append(letter)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="-"
    print(display)

    if guess not in chosen_wrd:
        live+=1
        if live==6:
            game_over=True
            print("You Lose")
    if "-" not in display:
        game_over=True
        print("you win")
    print(stages[live])





