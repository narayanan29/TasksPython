print('''                     .-------------.
                    _______________ ___________

                          )_______(
                          |"""""""|_.-._,.---------.,_.-.
                          |       | | |               | | 
                          |       |_| |_             _| |
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         _________
                       .-------------.
                      _______________''')

def find_highest_bidder(bidding_dictionary):
    winner=""
    highest=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest:
            highest=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of {highest}")
bids={}
run_bid=True
while run_bid:
    name=input("Type your name:")
    price=int(input("Type your price : "))
    bids[name]=price
    bid_continue=input("Are there any other bidders? type 'yes' or 'no' : ").lower()
    if bid_continue == "no":
        run_bid=False
        find_highest_bidder(bids)
    if bid_continue == "yes":
        print("\n"*50)

