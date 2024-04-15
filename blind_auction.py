print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
import os
print("Wlecome to the secret auction program.")

def find_highest_bid(bidding_record):
        highest_bid = 0
        for bidder in bidding_record:
            biddding_amount =bidding_record[bidder]
            if biddding_amount>highest_bid:
                highest_bid=biddding_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")
bidding_finished = False
while not bidding_finished:
    user_name = input("What is your name?\n")
    bid_price = int(input("what is your bid price?\n$"))
    
    name_bid ={}
    name_bid[user_name]=bid_price
    answer = input("Are there any other bidders?Type 'yes' or 'no'\n")
    if answer == 'yes':
        os.system('cls')
    elif answer =='no':
        bidding_finished = True
        find_highest_bid(name_bid)

    