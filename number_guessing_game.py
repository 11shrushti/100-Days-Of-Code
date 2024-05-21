
logo=""" ______                                                   __      __                                                          __                                 
 /      \                                                 |  \    |  \                                                        |  \                                
|  $$$$$$\ __    __   ______    _______   _______        _| $$_   | $$____    ______         _______   __    __  ______ ____  | $$____    ______    ______        
| $$ __\$$|  \  |  \ /      \  /       \ /       \      |   $$ \  | $$    \  /      \       |       \ |  \  |  \|      \    \ | $$    \  /      \  /      \       
| $$|    \| $$  | $$|  $$$$$$\|  $$$$$$$|  $$$$$$$       \$$$$$$  | $$$$$$$\|  $$$$$$\      | $$$$$$$\| $$  | $$| $$$$$$\$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\      
| $$ \$$$$| $$  | $$| $$    $$ \$$    \  \$$    \         | $$ __ | $$  | $$| $$    $$      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$    $$| $$   \$$      
| $$__| $$| $$__/ $$| $$$$$$$$ _\$$$$$$\ _\$$$$$$\        | $$|  \| $$  | $$| $$$$$$$$      | $$  | $$| $$__/ $$| $$ | $$ | $$| $$__/ $$| $$$$$$$$| $$            
 \$$    $$ \$$    $$ \$$     \|       $$|       $$         \$$  $$| $$  | $$ \$$     \      | $$  | $$ \$$    $$| $$ | $$ | $$| $$    $$ \$$     \| $$            
  \$$$$$$   \$$$$$$   \$$$$$$$ \$$$$$$$  \$$$$$$$           \$$$$  \$$   \$$  \$$$$$$$       \$$   \$$  \$$$$$$  \$$  \$$  \$$ \$$$$$$$   \$$$$$$$ \$$            
                                                                                                                                                                  
                                                                                                                                                                  
                                                                                                                                                                  """
  
# Global variables can be accessed by any function
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print(logo)
import random 
for _ in range(1):
    answer = random.randint(1,100)
    print(answer)

# make a function to for teh difficulty level
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level== "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Choose within the given options.")       

def game():
    # use a funtion to compare withn the answer and the user input
    def check_answer(answer,guessed_number, turns):
        """Checks the guessed number to the answer . And updates the turn values after each worng answer."""
        if guessed_number<answer:
            print("Too low.")
            return turns-1
        elif guessed_number> answer:
            print("Too high")
            return turns-1
        else:
            print(f"You got it ! The answer was {answer}")  
    
                    

    print("Welcome to the NUmber Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")

    turns = set_difficulty()
   

    guessed_number = 0
    # gussed number by the user
    while guessed_number != answer:
        print(f"You have {turns} attempts remaining to guess the number.")        
        guessed_number = int(input("Make a guess: ")) 
        # calling the function
        turns = check_answer(answer,guessed_number,turns)
game()                    