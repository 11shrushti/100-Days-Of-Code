

import random
# Create a deal_card function to return the card values .Here ace is 11
def deal_card():
    """Returns a random card form the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card= cards.choice(cards)
    return card

# Deal with computer and user with 2 cards each with deal_ card
user_card =[]
computers_card=[]
for _ in range(2):
    user_card.append(deal_card) 
