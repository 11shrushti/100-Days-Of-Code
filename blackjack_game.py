
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
import os
import math

# random card selection
def card_selection():
    """Returns two random card from the deck"""
    deal_cards = random.sample([11,1,2,3,4,5,6,7,8,9,10,10,10,10],2)
    # Add the random selected cards 
    def add_cards():
        """It adds the random two selected cards """
        add =math.fsum(deal_cards)
        print(f"Your cards{deal_cards} , current score : {add}")
#Computers choice
def computer_cards():
    """Two cards for the computer"""
    deal_card = random.sample([11,1,2,3,4,5,6,7,8,9,10,10,10,10],2)   
    card = deal_card[0]
    print(f"Computer's first card:{card}")     