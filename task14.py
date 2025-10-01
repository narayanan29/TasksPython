import random
from artssss import vs,logo
from game_data import data

#create a format information about the account
def format_data(account):
    account_name=account['name']
    account_des=account['description']
    account_country=account['country']
    return f"{account_name} is {account_des} from {account_country}"

def check_Answer(guess,a_follower_count,b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"

score=0
is_game_over=False
print(logo)
b_account=random.choice(data)
#generate random two accounts
while not is_game_over:
    a_account = b_account
    b_account = random.choice(data)
    if a_account == b_account:
        b_account=random.choice(data)

    print(f"Compare A: {format_data(a_account)}")
    print(vs)
    print(f"Against B: {format_data(b_account)}")

    guess = input("Who has more followers?:A/B : ")
    #clear the screen
    print("\n"*30)
    print(logo)

    a_follower_count = a_account['follower_count']
    b_follower_count = b_account['follower_count']
    is_correct = check_Answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right !Current point {score}")
    else:
        print(f"Sorry that wrong final point {score}")
        is_game_over=True

