
# Create a logo of higher and lower game and the vs symbol
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """ _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)"""

# Write the game data to play the game
from game_data import data
import random
import os

def foramt_data(account):
    """Takes the acccout data and makes it into readable format"""
    account_name = account["name"]
    accont_descr = account["description"]
    account_country = account["country"]
    print(f"{account_name}, a {accont_descr}, from {account_country}")

def  check_answer(user_input,a_follower,b_follower):
    """Use if statement to check if the user input is correct."""
    if a_follower > b_follower:
        return user_input == "a"
    else:
        return user_input =="b"
        

scores = 0
account_b = random.choice(data)
# This is for the game to continue till the user input is true 
game_repeat_shoubld_continue = True

# use a loop to repeat the same game if it is a win
while game_repeat_shoubld_continue:
    # Generate the raandom accoun from the data
    # after the correct answer move the option of b to a 
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {foramt_data(account_a)}") 
    print(vs)    
    print(f"Against B : {foramt_data(account_b)}")

    #ask the user for the answer
    user_input = input("Who has more followers? Type'A' or 'B':  ").lower()

    # Compare the answer from the user and decide weather it is win or loss
    follower_a = account_a["follower_count"]
    follower_b = account_b["follower_count"]
    is_correct = check_answer(user_input,follower_a,follower_b)   
    ## clear the screen after every round
    os.system('cls')

    if is_correct:
        # need a  counter to keep a track of the wins
        scores += 1
        print(f"You are right!. Current score : {scores}")
    else:
        game_repeat_shoubld_continue = False
        print(f"Sorry, that's wrong. Your final score : {scores}")    



    
    

   

    