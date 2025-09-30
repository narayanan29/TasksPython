logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
def deal_card():
    #Here is to deal with two cards
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(card):
    #Here to calculate the total score
    if sum(card) == 21 and len(card)==2:
        return 0
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare_score(co_score,us_score):
    if co_score == us_score:
        return "Match Draw "
    if co_score == 0:
        return "Oponent get a blackJack,you lose"
    if us_score == 0:
        return "You get a blackjack ,You Win"
    if us_score > 21:
        return "You went over you Lose"
    if co_score >21:
        return "Oponent went over you Win"
    if us_score > co_score:
        return "You Win"
    else:
        return "you Lose"

def play_game():
    user_card=[]
    print(logo)
    computer_card=[]
    user_score=-1
    computer_score=-1
    is_game_over=False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your card is {user_card} and your score is {user_score}")
        print(f"Computer first card is {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over=True
        else:
            user_deal=input("Do you want to take card type'y'"
                            "Do you want to pass type 'n':")
            if user_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over=True
    while computer_score != 0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(f"Your final hand: {user_card} ,final_score:{user_score}")
    print(f"Computer final hand: {computer_card}, final_score:{computer_score}")
    print(compare_score(computer_score,user_score))


while input("Do you want to play blackJack game?(y/n): ")=="y":
    print("\n"*30)
    play_game()